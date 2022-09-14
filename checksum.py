#lineno = "1"
#command = "M117 Hello World!\r\n"
from functools import wraps, reduce

def checksum(command):
        return reduce(lambda x, y: x ^ y, map(ord, command))


def getsum(inputcommand, lineno = 0):
        # Only add checksums if over serial (tcp does the flow control itself)
        prefix = "N" + str(lineno) + " " + inputcommand
        commandoutput = prefix + "*" + str(checksum(command=prefix))
        return commandoutput
            #if "M110" not in command:
            #    self.sentlines[lineno] = command

#send(self, "M117 Link established, writing gcode")
#print(getsum("M117 Link established, hiwriting gcode"))