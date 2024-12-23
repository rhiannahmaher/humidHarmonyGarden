from sense_hat import SenseHat
import time
import random
import datetime

sense = SenseHat()

GREEN = (0, 255, 0)

### Randomises humidity levels to show use of different readings during presentation
### def read_simulated_humidity():
###    return random.uniform(0, 100)

# Reads humidity levels from SenseHat
def read_humidity():
    humidity = sense.get_humidity()
    ### humidity = read_simulated_humidity()

    current_datetime = datetime.datetime.now()
    datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Time of reading: {datetime_string}")
    print(f"Humidity: {humidity:.2f} %")

# Checks the humidity level and prints the appropriate message
    if humidity < 30:
        print("Low humidity levels... Notifying user.")
    elif 30 <= humidity <= 50:
        print("Optimal humidity levels... No action required.")
    elif humidity > 50:
        print("High humidity levels... Notifying user and switching on dehumidifier for 1 hour.")

        # LEDs on SenseHat turn on to signify dehumidifier has been switched on
        sense.clear(GREEN)
        # LEDs on SenseHat turn off to signify dehumidifer has been switched off after 1 hour
        time.sleep(10)
        sense.clear()

def run():
    while True:
        read_humidity()
        print() # Prints blank line between readings
        time.sleep(10) # In real life the humidity would be read every hour (time.sleep(3600)

if __name__ == "__main__":
    run()