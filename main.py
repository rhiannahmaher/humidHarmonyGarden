# main.py script is used to run all scripts together

import threading
import time
from sense_hat import SenseHat
from blynk import run as blynk_humidity_run
from sensor_listener import handle_data, SensorListener
from humidity_sensor import run as humidity_run

def main():
    print("")
    print("Starting HumidHarmony Garden...")
    print("HumidHarmony Garden will begin monitoring air humidity and soil moisture...")
    print("")

    # Threading has been used to esure all scripts run in conjunction and do not block
    # each other when running 

    # First thread runs humidity reading from RaspPi/data transfer to ThingSpeak
    humidity_thread = threading.Thread(target=humidity_run)
    humidity_thread.start()

    # Second thread runs soil moisture reading from Packet Tracer to RaspPi/data transfer >    
    listener = SensorListener(port=5000) # Moved from sensor_listener.py as they were orig>    
    listener.callback = handle_data
    moisture_thread = threading.Thread(target=listener.start)
    moisture_thread.start()

    # Third thread transfers humidity data from RaspPi to Blynk
    blynk_humidity_thread = threading.Thread(target=blynk_humidity_run)
    blynk_humidity_thread.start()

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Shutting down HumidHarmony Garden...")
        listener.stop()
        humidity_thread.join() # Stops threading processes [Ref 2]
        moisture_thread.join()
        blynk_humidity_thread.join()

if __name__ == "__main__":
    main()