# HumidHarmony Garden 
The HumidHarmony Garden is an integrated system that monitors indoor air humidity, soil moisture levels, and alerts the homeowner to optimize plant care and maintain a healthy indoor environment for both plants and people.

## Description 
Key functions of HumidHarmony Garden include:
1. Soil Moisture Monitoring: Tracks moisture levels of indoor plants. Notifies the homeowner via Blynk and ThingSpeak alerts when moisture falls outside the 40%-80% range.
2. Indoor Humidity Monitoring: Records air humidity levels. App and email alerts are sent to the homeowner when humidity falls below 30%, with the home's dehumidifier automatically controlled when levels exceed 50%.

### Key Features
1. Real-time Data Recording: Utilizes Raspberry Pi Sense HAT for humidity tracking and Packet Tracer for simulated soil moisture data.
2. Data Logging: Transfers data to ThingSpeak and Blynk for visual tracking.
3. Critical Alerts: Sends notifications/email alterts for abnormal moisture (below 40% or above 80%) and humidity levels (below 30% or above 50%).
4. Automated Home Device Control: Automatically activates the dehumidifier when high humidity is detected.

## Dependencies
The following include the program's dependencies/prerequisites that must be installed before running the application.

### Raspberry Pi Sense HAT
Raspberry Pi Sense HAT has been used to measure humidity for project.

#### sense-hat package
sense-hat library allows interaction with the Raspberry Pi Sense HAT to collect humidity data from its sensor.

Installation:
```bash
sudo apt-get install sense-hat
```

### Blynk dependencies
Blynk dependencies allow interaction with the Raspberry Pi and Blynk for data logging, real-time monitoring, and notification alerts.

Installation:
```bash
sudo pip3 install https://bit.ly/3C0PMVY
```

### requests package
This library is used to make HTTP requests for communicating with ThingSpeak and Blynk APIs.

Installation:
```bash
sudo pip3 install requests
```
### Standard Python libraries
The following packages have been implemented in the project, all of which are included in Python's library and do not need to be installed:
- time
- datetime
- socket
- threading

### Required Accounts & API Keys
Before running the project, you will need to create accounts on Blynk and ThingSpeak, as these services are essential for monitoring and controlling your devices.

## Blynk
1. Go to the [Blynk web site](https://blynk.io/) and create an account.
2. Create a new template for project and add the following datastreams:
    - Name: Humidity
    - Pin: V0
    - Data Type: Double
    - Units: Percentage, %
    - Min: 0
    - Max: 100

    - Name: Soil Moisture
    - Pin: V1
    - Data Type: Double
    - Units: Percentage, %
    - Min: 0
    - Max: 100

    - Name: Dehumidifier
    - Pin: V2
    - Data Type: Integer
    - Units: None
    - Min: 0
    - Max: 1
3. Add two gauges to the Web Dashboard, one connected to V0 and labelled "Humidity" and the other connected to V1 and labelled "Soil Moisture".
4. Add one switch to the Web Dashboard, connected to V2 ad labelled "Dehumidifier".
5. Charts can be added as an additional step, connected to V0 (Humidity) and V1 (Soil Moisture) to view data trends.

## ThingSpeak
1. Go to the [ThingSpeak web site](https://thingspeak.mathworks.com/) and create an account.
2. Create a new channel with the following input:
    - Field 1: Humidity
    - Field 2: Soil Moisture

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

## Issues/Limitations
- Soil moisture data has been simulated in Packet Tracer. There is a limitation of real sensor data for this aspect of the program.
- ThingSpeak and Blynk platforms have usage limits on free accounts, which can cause issues with frequent data logging.
- Program could better implement security features such as using a switch and TCP protocols.

## Authors
ex. Rhiannah Maher
ex. 20085527@mail.wit.ie

## Libraries and Tools
- Raspberry Pi: Serves as the core hardware platform for running the HumidHarmony Garden system. Manages humidity sensor, listens and reads soil moisture data and simulates controlling the dehumidifier by displaying green LEDs. [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- Sense HAT: Reads humidity in real time and acts as the simulated dehumidifier by displaying green LEDs. [Sense HAT Documentation](https://www.raspberrypi.com/documentation/accessories/sense-hat.html)
- Python 3.0: The primary programming language used for the program, enabling communication with hardware components, data processing, and integration with Blynk and ThingSpeak. [Python Documenation](https://www.python.org/)
- Packet Tracer: Used for testing without physical hardware to simulate the soil moisture sensor. [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer)
- Blynk: Cloud-based IoT platform used for real-time monitoring via a mobile or web application, providing notifications and live sensor data logging. [Blynk web site](https://blynk.io/)
- ThingSpeak: Cloud-based IoT platform used for real-time monitoring via a web application, providing email alerts and live sensor data logging. [ThingSpeak web site](https://thingspeak.mathworks.com/)

## References
- Logic for constructing datetime strings: [How to Get Current Date and Time using Python](https://www.geeksforgeeks.org/get-current-date-and-time-using-python/)
- Logic for creating statements during Blynk events: [Events](https://docs.blynk.io/en/getting-started/events-tutorial?_gl=1*evpn25*_ga*MTY0NjgwODIxNi4xNzMzNjgwMzc1*_ga_L7QGLC416F*MTczNTQyMDgzNC4xMy4xLjE3MzU0MjI0NDUuMC4wLjA.*_ga_E376ZQ635Y*MTczNTQyMDgzMS4xMS4xLjE3MzU0MjI0NDUuMC4wLjA.)
- Logic for reading numeric data from Packet Tracer: [Remove all whitespace in a string](https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string)
- Logic for reading numeric data from Packet Tracer: [Python: Split, strip, and join in one line](https://stackoverflow.com/questions/12381408/python-split-strip-and-join-in-one-line)
- Logic for threading used: [Multithreading in Python](https://www.geeksforgeeks.org/multithreading-python-set-1/)
- Random uniform logic: [Python Random uniform() Method](https://www.w3schools.com/python/ref_random_uniform.asp)

## Further Learning/Resources
- Introduction to Blynk: [Introduction](https://docs.blynk.io/en)
- Introduction to ThingSpeak: [An Introduction to ThingSpeak](https://www.codeproject.com/Articles/845538/An-Introduction-to-ThingSpeak)
- Packet Tracer Tutorials: [Official Packet Tracer Tutorials](https://tutorials.ptnetacad.net/)
- Setting up the Raspberry Pi Sense HAT: (Getting started with the Sense HAT)[https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat]