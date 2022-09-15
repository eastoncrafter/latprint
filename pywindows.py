import serial
import time
import checksum
import string
#import argparse #not yet


ser = serial.Serial('COM8', 250000)#might be 250000 #opens serial comms

#ser.flushInput() #flush input buffer, don't know if this is needed yet
time.sleep(10)


linenumberlast = 0
ser.write(b"M117 Link established, writing gcode to testpr.gco\r")
time.sleep(2)
ser.write(b"M28 testpr.gco\r")
time.sleep(2)
f = open('CFFFP_3DBenchy.gcode', 'r') #opens file to write to
for line in f: #writes to file


#####serialmonitor

    bytesToRead = ser.inWaiting() # get the amount of bytes available at the input queue
    if bytesToRead:
        serialoutput = ser.read(bytesToRead) # read the bytes
        print(serialoutput.strip().decode('utf-8'))
#####end serialmonitor

    linenumberlast = linenumberlast + 1 #start at line 1
    nosemicolin = line.split(";", 1)[0]

    getsumfunc = nosemicolin.strip("\n")
    sendtoprinter = checksum.getsum(inputcommand=getsumfunc, lineno=linenumberlast)
    sendtoprinter = sendtoprinter + "\n" #use the checksum function to append checksum to send to printer
    #print(checksum.getsum(inputcommand=line, lineno=linenumberlast).strip()) #temporary, while debugging
    print(sendtoprinter) #temporary, while debugging
    ser.write(sendtoprinter.encode())
 

    
    time.sleep(0.1) #wait 100ms
    #ser.write(checksum.getsum(inputcommand=line).encode()) #old way
time.sleep(2)
ser.write(b"M29\r") #ends gcode write
time.sleep(2)
f.close() #closes file