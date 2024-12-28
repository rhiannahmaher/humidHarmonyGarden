# Script reads humidity from SenseHat and dislays humidity data to console.
# Data is then transferred to ThingsSpeak for data logging.

from sense_hat import SenseHat
import time
import random
import datetime
import requests

sense = SenseHat()
sense.clear()

green = (0, 255, 0)

# ThingSpeak settings
thingspeak_write_api_key = "WCI036N97YKBCC11"
thingspeak_channel_url = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_humidity_to_thingspeak(humidity):
    payload = {
        "api_key": thingspeak_write_api_key,
        "field1": humidity
    }

    response = requests.get(thingspeak_channel_url, params=payload)

    if response.status_code == 200:
        print("Humidity data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

# Reads humidity levels from SenseHat
def get_humidity():
    humidity = sense.get_humidity()
    humidity = round(humidity, 2)
    return humidity

# Takes humidity data to be used for printed statements to console
def read_humidity():
    humidity = get_humidity()

    current_datetime = datetime.datetime.now() # [Ref 3]
    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print("Reading humidity...")
    print(f"Time of reading: {datetime_string}")
    print(f"Humidity: {humidity:.2f} %")

    # Checks the humidity level and prints the appropriate message
    if humidity < 30:
        print("Low humidity levels... Notifying user.")
    elif 30 <= humidity <= 50:
        print("Optimal humidity levels... No action required.")
    elif humidity > 50:
        print("High humidity levels... Notifying user and switching on dehumidifier")
        # LEDs on SenseHat turn on to signify dehumidifier has been switched on
        sense.clear(green)

    time.sleep(15) # 15 secs represents dehumidifer being switched on for 1 hour
    sense.clear() # Dehumidifier is switched back off [no LEDs on SenseHat]
    return humidity

def run():
    while True:
        humidity = read_humidity()
        send_humidity_to_thingspeak(humidity)
        print()

if __name__ == "__main__":
    run()