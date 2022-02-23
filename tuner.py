#importing modules
from scipy.fft import fft
import serial, time
import numpy as np

# To open a serial port to comunicate with Arduino Uno
print("Opening serial port in COM3...")
arduino_uno = serial.Serial(port='COM3',baudrate=9600, timeout=0.2)
while True:
    option = input("Enter '1' to request signal: ")
    if option=='1':
        break
arduino_uno.write(('1').encode('utf-8'))
print("\nSignal requested succesfully!\n")
print("Reading line")
rawString = arduino_uno.readline()
print(rawString)
print("Closing port...")
arduino_uno.close()
# To request Arduino the acoustic signal

# To get the fundamental frequency of the signal