#lineno = "1"
#command = "M117 Hello World!\r\n"
from functools import wraps, reduce

def checksum(command):
        return reduce(lambda x, y: x ^ y, map(ord, command))


def send(command, lineno = 0):
        # Only add checksums if over serial (tcp does the flow control itself)
        prefix = "N" + str(lineno) + " " + command
        command = prefix + "*" + str(checksum(command=command))
            #if "M110" not in command:
            #    self.sentlines[lineno] = command

#send(self, "M117 Link established, writing gcode")
print(checksum("M117 Link established, writing gcode"))