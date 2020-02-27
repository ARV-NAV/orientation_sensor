"""Python wrapper to parse the IMU binary data

    Module to read binary data outputted from the IMU and convert it to a usable python object
    Uses a predefined MatLab parser to parse through the binary data.
    The parsed data is converted into a dict containing all of the IMU data."""

# ================ Built-in Imports ================ #

from time import time

# ================ Third Party Imports ================ #

import matlab.engine as m_engine

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez"]

# ================ Global Variables ================ #

eng = m_engine.start_matlab()
filename = "sample_raw_data.bin"


def get_last_orientation() -> dict:
    """Get Last Orientation
        Grabs the last set of binary values from the binary file.
        Opens and reads the file through MatLab itself to then send it through the parser
        Documentation of the DsFileReader: https://www.mathworks.com/help/matlab/ref/matlab.io.datastore.dsfilereader-class.html

    @return: dict: data containing the orientations
    """
    fp = eng.matlab.io.datastore.DsFileReader(filename)
    eng.seek(fp, -1000, 'Origin', 'end-of-file')  # This is supposed to set the file pointer to the end of the file. it works on matlab, but not here
    ml_bin_arr = eng.read(fp, 1000)

    start_time = time()
    orientation = eng.parse_imu(ml_bin_arr)
    print("Parse time {0}s".format(time() - start_time))

    return orientation


if __name__ == "__main__":
    data = get_last_orientation()
    print(data)
