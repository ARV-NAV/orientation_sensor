import sys
import argparse

# Add mscl library to path variable
sys.path.append('/usr/share/python3-mscl/')
import mscl

# Construct Command Line Args
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", required=True, type=str,
                help="id of the Serial COM Port")
ap.add_argument("-b", "--baud", default=921600, type=int,
                help="baud rate of the Serial COM Port. Default to 921600.")
args = vars(ap.parse_args())

# Debug MSCL Version
print("Using MSCL Version:", str(mscl.MSCL_VERSION))

# creates a connecion to the physical port
try:
    print("Trying to connect to serial port '" + args["port"] + "'...")
    connection = mscl.Connection.Serial(args['port'], args['baud'])
    print("Serial Port connection successful!")
except RuntimeError as e:
    print("Failure: Serial Port Connection:", e)
    exit()

try:
    print("Building internal node object ...")
    # creates an internal node object to interface with internal sensor device
    node = mscl.InternalNode(connection)
    print("Internal node build.")
except RuntimeError as e:
    print("Failure: Internal node:", e)
    exit()

# Test Connection
success = node.ping()
if (success):
    print("Device connection established.")
else:
    print("Device connection failed. Exiting...")
    exit()
