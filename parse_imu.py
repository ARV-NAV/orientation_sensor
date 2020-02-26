import datetime
import os
import matlab.engine as mEngine
import pprint

pp = pprint.PrettyPrinter(indent=2)
t1 = datetime.datetime.now()
eng = mEngine.start_matlab()
t2 = datetime.datetime.now()
delta = t2-t1
print("Engine build time (ms):", delta.total_seconds() * 1000) 


filename = "sample_raw_data.bin"

fileContent = None
with open(filename, mode='rb') as file:
    file.seek(-1000, os.SEEK_END)
    fileContent = file.read()

t1 = datetime.datetime.now()
test = eng.parse_imu(fileContent)
t2 = datetime.datetime.now()
delta = t2-t1
print("Parse time - first parse (ms):", delta.total_seconds() * 1000) 

with open(filename, mode='rb') as file:
    file.seek(-1000, os.SEEK_END)
    fileContent = file.read()

tt1 = datetime.datetime.now()
testt = eng.parse_imu(fileContent)
tt2 = datetime.datetime.now()
deltat = tt2-tt1
print("Parse time - second parse (ms):", deltat.total_seconds() * 1000) 

with open(filename, mode='rb') as file:
    file.seek(-1000, os.SEEK_END)
    fileContent = file.read()

tt1 = datetime.datetime.now()
testt = eng.parse_imu(fileContent)
tt2 = datetime.datetime.now()
deltat = tt2-tt1
print("Parse time - second parse (ms):", deltat.total_seconds() * 1000) 

# for key, value in test.iteritems():
#     print (key)


# # Packet data structure
# class Packet():
#     def __init__(self, descriptor, payload):
#         self.descriptor = descriptor
#         self.payload = payload


# # Retrieves a list of packets from binary data
# def findPackets(data):
#     packetList = []
#     for i in range(len(data)):
#         if data[i] == 0x75 and data[i+1] == 0x65:
#             packetDescriptor = data[i+2]
#             payloadLength = data[i+3]
#             payloadStart = i+4
#             payloadEnd = payloadStart + payloadLength

#             # print("Packet found - Header:",
#             #       str(hex(data[i])),
#             #       str(hex(data[i+1])),
#             #       str(hex(data[i+2])),
#             #       str(hex(data[i+3])))

#             newPacket = Packet(
#                 packetDescriptor,
#                 data[payloadStart:payloadEnd]
#             )
#             packetList.append(newPacket)
#     return packetList


# # Open raw data file
# with open(filename, mode='rb') as file:
#     fileContent = file.read()


#     t1 = datetime.datetime.now().time()
#     testList = findPackets(fileContent)
#     t2 = datetime.datetime.now().time()
#     print("Packets found:", str(len(testList)))
#     print("parsing time (ms):", str(t2.second - t1.second))

#     # for item in testList:
#     #     print(len(item.payload))
