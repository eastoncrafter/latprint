import serial
import time
import argparse

parser = argparse.ArgumentParser(description="Send gcode files to a reprap running marlin") #define the parser

parser.add_argument('-p','--port',help='the port of the printer',required=True)
parser.add_argument('-f','--file',help='location of the gcode file',required=True)
args = parser.parse_args()
print(args) #for testing purposes