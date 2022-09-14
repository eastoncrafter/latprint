import serial
import time
import checksum
#import argparse #not yet


#ser = serial.Serial('COM8', 250000)#might be 250000 #opens serial comms
#time.sleep(1)
#ser.flushInput() #flush input buffer
#time.sleep(10)


linenumberlast = 0
#ser.write(b"M117 Link established, writing gcode\r")
time.sleep(2)
#ser.write(b"M28 testpr.gco\r")
time.sleep(2)
f = open('test.gcode', 'r') #opens file to write to
for line in f: #writes to file
    #ser.write(line.encode())
    linenumberlast = linenumberlast + 1
    print(checksum.getsum(inputcommand=line, lineno=linenumberlast)) #temporary, while debugging
    #ser.write(checksum.getsum(inputcommand=line).encode())
#ser.write(b"M29\r") #ends gcode write
f.close() #closes file