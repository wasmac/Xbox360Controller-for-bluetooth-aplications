import time
import os
import serial

last_y = 0

def swap(x):
    x1 = x*(-1000)
    x1 = x1+1000
    x1 = x1/2
    x1 = x1+1000
    return int(x1)

port = "COM8"
ser = serial.Serial(port,9600)
try:
    ser.flushInput()
    print("Serial is open")
except:
    print('Error')
    exit()
try:
    while(1):
        time.sleep(0.1)
        with open(os.path.join(r'C:\Users\User\RTD_Xbox_Controller','numbs.txt'), 'r') as open_file:
            y1_prime= open_file.read()
            try:
                y1 = float(y1_prime)
                last_y1 = y1
            except:
                y1 = int(last_y1)
            y1 = swap(y1)
        print(y1)
        ser.write(b'%d\n' % y1)
except Exception:
    print('error')
else:
    print('Cannot open serial port')
