import socket
import threading
from sense_hat import SenseHat

class SensorListener:
    def __init__(self, host='0.0.0.0', port=5000, buffer_size=1024):
        # Initialize the UDP Listener
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.running = False
        self.callback = None

    def start(self):
        # Start in a separate thread
        self.running = True
        threading.Thread(target=self._listen, daemon=True).start()

    def stop(self):
        # Stop the UDP listener
        self.running = False

    def _listen(self):
        # Internal method to listen for UDP packets and handle them
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind((self.host, self.port))
            print(f"UDP Listener started on {self.host}:{self.port}")
            while self.running:
                try:
                    data, address = server.recvfrom(self.buffer_size)
                    print(f"Received data: {data.decode()} from {address}")
                    if self.callback:
                        self.callback(data.decode())
                except Exception as e:
                    print(f"Error receiving data: {e}")
            print("UDP Listener stopped.")


def handle_data(data):
    # Handle the humidity data
    print(f"Processing humidity data: {data}")
    humidity = float(data)
    if humidity > 80:
        print("Warning: High humidity!")
    elif humidity < 20:
        print("Warning: Low humidity!")
    else:
        print(f"Humidity is normal: {humidity}%")

if __name__ == "__main__":
    # Initialize SenseHat
    sense = SenseHat()
    # Initialize the listener for UDP communication
    listener = SensorListener(port=5000)
    listener.callback = handle_data
    listener.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()