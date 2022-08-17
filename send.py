import serial
import time
import argparse
import time #not sure if this is needed yet

parser = argparse.ArgumentParser(description="Send gcode files to a reprap running marlin") #define the parser
parser.add_argument('-p','--port',help='the port of the printer',required=True)
parser.add_argument('-f','--file',help='location of the gcode file',required=True)
args = parser.parse_args()
print(args) #for testing purposes
#start serial communication
ser = serial.Serial(args.port, 115200)
ser.write("\r\n\r\n") #wake the printer
time.sleep(2) #wait for it
ser.flushInput() #just a precaution
