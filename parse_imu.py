"""Python wrapper to parse the IMU binary data
    Module to read binary data outputted from the IMU and convert it to a usable python object
    Uses a predefined MatLab parser to parse through the binary data.
    The parsed data is converted into a dict containing all of the IMU data."""

# ================ Built-in Imports ================ #

from time import time


# ================ Third Party Imports ================ #

import matlab.engine as m_engine
import pprint
import numpy as np

# ================ Authorship ================ #

__author__ = "Chris Patenaude"
__contributors__ = ["Chris Patenaude", "Gabriel Michael", "Gregory Sanchez"]

# ================ Global Variables ================ #

pp = pprint.PrettyPrinter(indent = 2)
eng = m_engine.start_matlab()
filename = "sample_raw_data.bin"
timestamped_file = "IMU_timestamped_test_data.bin"


def get_last_orientation() -> dict:
    """Get Last Orientation
        Grabs the last set of binary values from the binary file.
        Opens and reads the file through MatLab itself to then send it through the parser
        Documentation of the DsFileReader: https://www.mathworks.com/help/matlab/ref/matlab.io.datastore.dsfilereader-class.html
    @return: dict: data containing the orientations
    """
    # print(eng.seek(fp, 100, 'RespectTextEncoding', True, 'end-of-file', True))

    start_time = time()
    """Keys of the orientation ditc
     'units': { 'attitude': { 'compensated_angular_rate': { 'X': 'rads/sec',
                                                         'Y': 'rads/sec',
                                                         'Z': 'rads/sec',
                                                         'valid': '1=valid, 0=invalid'},
                           'gps_timestamp': { 'time_of_week': 'seconds',
                                              'valid': '1=valid, 0=invalid',
                                              'week_number': 'n/a'},
                           'heading_update_source_state': { 'heading': 'radians',
                                                            'heading_1_sigma_uncertainty': 'radians',
                                                            'source': '0=no source, 1=Magnetometer, 4=External',
                                                            'valid': '1=valid, 0=invalid'},
                           'linear_acceleration': { 'X': 'm/sec^2',
                                                    'Y': 'm/sec^2',
                                                    'Z': 'm/sec^2',
                                                    'valid': '1=valid, 0=invalid'},
                           'orientation_euler_angles': { 'pitch': 'radians',
                                                         'roll': 'radians',
                                                         'valid': '1=valid, 0=invalid',
                                                         'yaw': 'radians'}}}}
    """
    orientation = eng.parse_imu(timestamped_file, eng.logical(1))
    print("Parse time {0}s".format(time() - start_time))

    test_dict = {'heading':np.asarray(orientation['attitude']['heading_update_source_state']['heading']),
                 'pitch':np.asarray(orientation['attitude']['orientation_euler_angles']['pitch']),
                 'roll':np.asarray(orientation['attitude']['orientation_euler_angles']['roll']),
                 'yaw':np.asarray(orientation['attitude']['orientation_euler_angles']['yaw']),
                 'valid_heading':np.asarray(orientation['attitude']['orientation_euler_angles']['valid']),
                 'valid_orientation':np.asarray(orientation['attitude']['orientation_euler_angles']['valid']),
                 'nuc_time':np.asarray(orientation['attitude']['nuc_time'])
    }
    return test_dict


def get_last_valid_orientation(orientation_data: dict) -> dict:
    i = 0
    while (i < 9):
        if(orientation_data['valid_heading'][0][9 - i] == 1 and orientation_data['valid_orientation'][0][9 - i] == 1):
            valid_data = {'heading':np.asarray(orientation_data['heading'][0][i]),
                          'pitch':np.asarray(orientation_data['pitch'][0][i]),
                          'roll':np.asarray(orientation_data['roll'][0][i]),
                          'yaw':np.asarray(orientation_data['yaw'][0][i]),
                          'nuc_time':np.asarray(orientation_data['nuc_time'][0][i]) }
            return valid_data
        else:
            i+=1




if __name__ == "__main__":
    data = get_last_orientation()
    #pp.pprint(data)

    valid = get_last_valid_orientation(data)

    pp.pprint(valid)
