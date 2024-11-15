import bluetooth
import subprocess
import atexit

# Function to enable Bluetooth
def enable_bluetooth():
    try:
        subprocess.run(["sudo", "hciconfig", "hci0", "up"], check=True)
        print("Bluetooth device hci0 is now up.")
    except subprocess.CalledProcessError:
        print("Failed to turn on Bluetooth device hci0.")

# Function to disable Bluetooth
def disable_bluetooth():
    try:
        subprocess.run(["sudo", "hciconfig", "hci0", "down"], check=True)
        print("Bluetooth device hci0 is now down.")
    except subprocess.CalledProcessError:
        print("Failed to turn off Bluetooth device hci0.")

# Register the disable_bluetooth function to run at script exit
atexit.register(disable_bluetooth)

# Enable Bluetooth device hci0
enable_bluetooth()

# Retrieve the MAC address of the Bluetooth adapter on the server
server_mac_address = bluetooth.read_local_bdaddr()[0]
print(f"Server MAC Address: {server_mac_address}")

# Set up a Bluetooth RFCOMM server socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
try:
    server_sock.bind(("", 1))  # Bind to 1
    server_sock.listen(1)  # Listen for a single client connection

    # Display the port being used for client connections
    port = server_sock.getsockname()[1]
    print(f"Listening for connections on RFCOMM channel {port}")

    # Accept an incoming client connection
    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    try:
        while True:
            # Receive and display data from the client
            data = client_sock.recv(1024)
            if data:
                print(f"Received: {data.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_sock.close()  # Ensure client socket is closed

finally:
    server_sock.close()  # Ensure server socket is closed
