import serial
import argparse
import time #not sure if this is needed yet

parser = argparse.ArgumentParser(description="Send gcode files to a reprap running marlin") #define the parser
#parser.add_argument('-p','--port',help='the port of the printer',required=True)
#parser.add_argument('-f','--file',help='location of the gcode file',required=True)
#args = parser.parse_args()
#print(args) #for testing purposes
#start serial communication


#Top TODO:
#1.  Identify why M117 works in terminal by not here.  (pyserial details... probably one of the options below)
#2.  Successfully send M117 Hello with python
#3.  Switch code to M28/M29 File Upload
#4 (independent) Stream a file as input (benchy.gcode, etc.)
#5.  git merge marlin (whiteboard tomorrow)

#Sound good?
#looks pretty good, I am trying to run this on an ubuntu vm right now
#Nice.  But windows will still control the serial port if it's the VM host.
#(better dev tools in ubuntu though!)  Oh wow - we can type at the same time!!! :)
# think virtualbox does some weird shinanigans with the port and emulating a usb hub or something Yeah we can! Thats so cool!
#heheh - that would be the *Windows* port of VirtualBox of course :)
#maybe, is virtualbox opensource?
#Yes it is....Oracle controls it, but the sourcecode is open
#brb (actually, I'll switch to matrix for non-notes)


ser = serial.Serial() #("COM8", 115200, write_timeout=None) #comment by tom
ser.port = "COM8"
ser.baudrate = 256000 #115200
ser.writeTimeout = None
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = True #disable software flow control
ser.rtscts = False #disable hardware flow control (RTS/CTS)
ser.dsrdtr = False #disable hardware flow control (DSR/DTR)

try:
    ser.open()
    if ser.isOpen():
        ser.write(bytes("M117 Hello World!\n", 'utf-8'))
        ser.flush()
        ser.close()
except Exception as e:
    print(e)
    exit()

print("complete")

#ser.write(b"\r\n\r\n") #wake the printer
#time.sleep(2) #wait for it
#ser.flushInput() #just a precaution
#ser.write(b"M117 Hello World!\r\n") #print a message
#ser.write()
#time.sleep(10)
#ser.write(bytes("M117 Hello World!", 'utf-8'))
#ser.write(b"M117 Hello world!\r\n")
#time.sleep(1)
#ser.close()

#I'm back! :)  But we can chat in matrix.
#hi
#trying to figure out a way for me to stay up stairs yet still be connected to the printer
#Ah, printer is in basement....right 
#was thinking of using something like mutagen, or maybe connecting to the dockpi (I actually just realized that dockpi runs linux which defeates the purpose)
#Yes....it will be good to troubleshoot Windows (although I'd still rather do it from a kvm guest :)
#but.... I don't know what mutagen is...will have to google/ddg...though X11 has had that ability built
#in for 4 decades+ :)
#Oh - thanks!  I may check that out and add it to the tool list :)
#you bet - I hope I won't owe consulting fees.
#phew :)
#So, mutagen? or basement?#hahh ok
#ok, I'm going to finish some dinner stuff
#brb

#looks like mutagen does not have a docker container



# import serial
# import time
# from datetime import datetime

# def command(ser, command):
#   start_time = datetime.now()
#   ser.write(str.encode(command)) 
#   time.sleep(1)

#   while True:
#     line = ser.readline()
#     print(line)

#     if line == b'ok\n':
#       break

# ser = serial.Serial('/dev/tty.usbserial-AG0KEQWV', 115200)
# time.sleep(2)
# command(ser, "G28\r\n")



# command(ser, "G28 X0 Y0 Z0\r\n") """