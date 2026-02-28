'''
Created on 2026 Feb 27

@author: Zilong
'''

import pydicom




# File path.
file_path = ""


if __name__ == "__main__":
    # Read the specified DICOM files.
    ds = pydicom.read_file(file_path)
    ds.