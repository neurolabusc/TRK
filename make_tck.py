#Create a TCK format streamline
# python makeTCK.py
import numpy as np

def make_tck():
    # generate a TCK file with a single fiber

    # Header information
    #header = b'mrtrix tracks\n' + b'count: 2\n' + b'datatype: Float32LE\n' + b'END\n'
    header = b'mrtrix tracks\n' + b'count: 0000000918\n' + b'datatype: Float32LE\n' + b'voxel_sizes: (1.0, 1.0, 1.0)\n' + b'dimensions: (157, 189, 136)\n' + b'voxel_order: LPS\n' + b'file: . 142\n' + b'END\n'
    header = b'mrtrix tracks\n' + b'count: 0000000002\n' + b'datatype: Float32LE\n' + b'voxel_sizes: (1.0, 1.0, 1.0)\n' + b'dimensions: (157, 189, 136)\n' + b'voxel_order: LPS\n' + b'file: . 142\n' + b'END\n'

    # Fiber coordinates
    fiber = np.array([90, -126, -72, 0, 0, 0, 0, 22, 0, 0, 74, 0, np.nan, np.nan, np.nan,
                      90, 0, 0, 0, 0, 0, -90, 0, 0, -90, -90, 0, np.nan, np.nan, np.nan, np.inf, np.inf, np.inf], dtype=np.float32)

    # Open file for writing
    with open('track.tck', 'wb') as fid:
        # Write header and fiber coordinates to the file
        fid.write(header)
        fid.write(fiber.tobytes())

if __name__ == "__main__":
    make_tck()
