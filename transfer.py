import argparse
import os
import binproto2 as mbp


parser = argparse.ArgumentParser(description='Send files over a serial port to Marlin')
parser.add_argument('source', help='source path')
parser.add_argument('destination', nargs='?', help='destination path')
parser.add_argument("-p", "--port", default="COM8", help="serial port to use")
parser.add_argument("-b", "--baud", default="115200", help="baud rate of serial connection")
parser.add_argument("-d", "--blocksize", default="512", help="defaults to autodetect")
parser.add_argument("-r", "--reset", action='store_true', help="Reset after transfer (firmware flash)")
parser.add_argument("-t", "--test", action='store_true', help="Benchmark the serial link without storing the file")
parser.add_argument("-c", "--compression", action='store_true', help="Enable compression")
parser.add_argument("-x", "--timeout", default="1000", help="Communication timout, lossy/slow connections need higher values")

args = parser.parse_args()

protocol = mbp.Protocol(args.port, args.baud, args.blocksize, int(args.timeout))
echologger = mbp.EchoProtocol(protocol)

protocol.connect()

#filetransfer = mbp.FileTransferProtocol(protocol, None, ConsoleLogger())
#filetransfer.copy(args.source, args.destination or os.path.basename(args.source), args.compression, args.test)

#protocol.disconnect()

protocol.send_ascii("M117 Hello world!")
#filetransfer.abort()
protocol.shutdown()
