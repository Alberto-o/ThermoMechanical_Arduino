from time import sleep
import serial
from subprocess import call

ser = serial.Serial('/dev/ttyACM1', 9600) # Establish the connection on a specific port

while True:
     fromArduino = ser.readline() # Read the newest output from the Arduino
     fromArduino = fromArduino.replace("\n", "")
#     print fromArduino
     if fromArduino == "1":
          call(["ls", "-l"])
     #     print "5 sent"
     # sleep(.5) # Delay for one tenth of a second
