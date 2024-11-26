import max30102
import hrcalc
from bluetooth_sender import BluetoothSender

m = max30102.MAX30102()

# Use receiver's Bluetooth MAC address
SERVER_ADDRESS = "2C:CF:67:03:0B:FE"
sender = BluetoothSender(SERVER_ADDRESS)

try:
    sender.connect()
    
    # 100 samples are read and used for HR calculation in a single loop
    while True:
        ir = m.read_sequential()

        # Calculate heart rate and IPM
        hr, hr_valid, ipm, hrstd, rmssd = hrcalc.calc_hr_and_ipm(ir)
        data_to_send = f"Heart Rate: {hr} bpm (Valid: {hr_valid}), Impulse Per Minute: {ipm}, Heart Rate STD: {hrstd}, RMSSD: {rmssd}"
        print(data_to_send)
        # Send data over bluetooth
        sender.send_data(data_to_send)


finally:
        sender.disconnect()