# Script listens for events from Packet Tracera dn reads moisture data.
# Moisture data is then transferred to ThingSpeak and Blynk for data logging

import socket
import threading
import datetime
import requests
import BlynkLib
from time import sleep
from sense_hat import SenseHat

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

thingspeak_write_api_key = "WCI036N97YKBCC11"
thingspeak_channel_url = "https://api.thingspeak.com/update"

# Blynk authentication token
blynk_auth = "WNvDqX_B3rDIaDe_EcfJVX2y8GsDUMxS"

# Initialise Blynk instance
blynk = BlynkLib.Blynk(blynk_auth)

def send_moisture_to_thingspeak(moisture):
    payload = {
        "api_key": thingspeak_write_api_key,
        "field2": moisture
    }

    response = requests.get(thingspeak_channel_url, params=payload)

    if response.status_code == 200:
        print("Moisture data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

class SensorListener:
    def __init__(self, host="0.0.0.0", port=5000, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.running = False
        self.callback = None

    def start(self):
        self.running = True
        threading.Thread(target=self._listen, daemon=True).start()

    def stop(self):
        self.running = False

    def _listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind((self.host, self.port))
            print(f"UDP Listener started on {self.host}:{self.port}")
            print("")
            while self.running:
                try:
                    data, address = server.recvfrom(self.buffer_size)

                    # Displays current time/date for each reading to console
                    current_datetime = datetime.datetime.now()
                    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

                    print("Reading soil moisture...")
                    print(f"Time of reading: {datetime_string}")
                    print(f"Received data: {data.decode()} from {address}")
                    if self.callback:
                        self.callback(data.decode())
                    print()
                except Exception as e:
                    print(f"Error receiving data: {e}")
            print("UDP Listener stopped.")

def handle_data(data):
    try:
        # Returns numeric moisture data from Packet Tracer
        moisture_str = data.split(":")[1].strip().replace("%", "") # Splits "Moisture levels: {moisture}" by ":" and returns the numeric data only
        moisture = float(moisture_str)
        print(f"Processing data: Moisture level: {moisture}%")

        # Moisture data is transferred to ThingSpeak
        send_moisture_to_thingspeak(moisture)

        # MOisture data is transferred to Blynk (V1)
        blynk.virtual_write(1, moisture)
        # Parameters log events on Blynk for low/high moisture readings
        if moisture > 80:
            blynk.log_event("high_moisture_event", f"High Soil Moisture Detected! Moisture Level: {moisture}%")
        elif moisture < 40:
            blynk.log_event("low_moisture_event", f"Low Soil Moisture Detected! Moisture Level: {moisture}%")

    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    listener = SensorListener(port=5000)
    listener.callback=handle_data
    listener.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()