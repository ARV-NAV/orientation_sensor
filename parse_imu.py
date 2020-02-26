import datetime
import os
import matlab.engine as mEngine
import array
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
    fileContent = file.read();

data = eng.parse_imu(fileContent)
print(data)
