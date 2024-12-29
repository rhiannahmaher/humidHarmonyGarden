# Installation & Execution Guide

## Installation
1. Download files from repository.
2. Transfer main.py, humidity_sensor.py, sensor_listener.py, and blynk.py scripts to Raspberry Pi via USB.
3. Files can then be moved to selected folder on Raspberry Pi.

### Modifications (ThingSpeak, Blynk and Packet Tracer)
Before running the application, replace the placeholder API keys for both ThingSpeak and Blynk with your personal API key.

To do so, please see the following:
1. Navigate to humidity.py and replace the placeholder API key associated with "thingspeak_write_api_key" on line 16 with your personal ThingSpeak write API key.
2. Navigate to humidity.py and replace the placeholder channel URL associated with "thingspeak_channel_url" on line 17 with your persnal channel URL.
3. Navigate to blynk.py and replace the placeholder authorization token associated with "blynk_auth" on line 13 with your personal Blynk authorization token.
4. Navigate to sensor_listener.py and replace the placeholder API key associated with "thingspeak_write_api_key" on line 17 with your personal ThingSpeak write API key.
5. Navigate to sensor_listener.py and replace the placeholder channel URL associated with "thingspeak_channel_url" on line 18 with your personal ThingSpeak channel URL.
6. Navigate to sensor_listener.py and replace the placeholder authorization token associated with "blynk_auth" on line 21 with your personal Blynk authorization token.
7. Navigate to Packet Tracer and open the Programming tab on the SBC Board. Open pi_bridge.pi and replace the IP on line 8 with your Raspberry Pi's IP v4 address.

## Executing program
Once the dependencies are installed on the Raspberry Pi, and you have your Blynk and ThingSpeak accounts and API keys, ensure your Raspberry Pi is connected to the internet and the Sense HAT is correctly attached to the Raspberry Pi.

To execute the program, navigate to Packet Tracer. Open the Programming tab on the SBC Board and execute the program by selecting Run. Random soil moisture values will begin to generate.

Navigate to your Raspberry Pi and execute the main Python script, main.py using the following:
```bash
python main.py
``` 
The Raspberry Pi will begin listening for soil moisture data from Packet Tracer as well as generating humidity readings from Sense HAT.
