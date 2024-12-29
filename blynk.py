# Script takes humidity data from humidity_sesnor.py and transfers it to Blynk server

from sense_hat import SenseHat
import BlynkLib
from time import sleep
from humidity_sensor import get_humidity

# Initialise SenseHat
sense = SenseHat()
sense.clear()

# Blynk authentication token
blynk_auth = "WNvDqX_B3rDIaDe_EcfJVX2y8GsDUMxS"

# Initialise Blynk instance
blynk = BlynkLib.Blynk(blynk_auth)

# Registers handler for virtual pin V2 (switch) write event on Blynk
# Button/switch values assigned demhumidifier status
@blynk.on("V2")
def handle_v2_write(value):
    button_value = value[0]

    if button_value == "0":
        print("Dehumidifier status: OFF")
    elif button_value == "1":
        print("Dehumidifier status: ON")

# Main loop keeps Blynk connection alive and processes events
def run():
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.virtual_write(2, 0) # Dehumidifier (V2) is set to OFF at the start of the application
            blynk.run()

            humidity = get_humidity()
            blynk.virtual_write(0, humidity) # Humidity data is transferred to Blynk (V0)

            # Parameters log events associated with high/low humidity
            # Dehumidifier/switch (V2) status is changed depending on humidity data
            if humidity > 50:
                print("Dehumidifier status: ON")
                blynk.virtual_write(2, 1)
                blynk.log_event("high_humidity_event", f"High Humidity Detected! Humidity Level: {humidity}%")
                sleep(14) # Dehumidifier is kept ON
                print("Dehumidifier status: OFF")
                blynk.virtual_write(2, 0) # Dehumidifier is then switched back off
            elif humidity < 30:
                blynk.virtual_write(2,0)
                blynk.log_event("low_humidity_event", f"Low Humidity Detected! Humidity Level: {humidity}%")
            else:
                blynk.virtual_write(2, 0)
            sleep(1)
    except KeyboardInterrupt:
        print("Blynk application stopped.")

if __name__ == "__main__":
    run()