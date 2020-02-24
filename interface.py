import mscl
import sys
import argparse
from utils import debug

# Add mscl library to path variable
sys.path.append('/usr/share/python3-mscl/')

# Construct Command Line Args
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", required=True, type=str,
                help="id of the Serial COM Port")
ap.add_argument("-b", "--baud", required=True, type=int,
                help="baud rate of the Serial COM Port")
ap.add_argument("-d", "--debug", type=bool, default=False,
                help="set to 'true' to display debug info")
args = vars(ap.parse_args())

# helper function to toggle debug messages
def debug(msg, value):
    if (args["debug"]):
        print(msg, value)


# Debug MSCL Version
debug("Using MSCL Version: ", mscl.MSCL_VERSION)

# creates a connecion to the physical port
connection = mscl.Connection.Serial(args['port'], args['baud'])

# creates an internal node object to interface with internal sensor device
node = mscl.InternalNode(connection)

# Test Connection
if(args["debug"]):
    success = node.ping()
    if (success):
        print("Device connection established.")
    else:
        print("Device connection failed. Exiting...")
        exit()
