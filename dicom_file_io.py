'''
Created on 2026 Feb 27

@author: Zilong
'''

import pydicom
import cv2
import numpy as np

# File path.
file_path = r"data\samples\CT\I200.dcm"

if __name__ == "__main__":
    print("DICOM image file input and output.")
    
    # Read the specified DICOM files as a dataset data structure.
    ds = pydicom.read_file(file_path)
    
    # Print the dataset of DICOM file header.
    print(ds)
    
    # Convert the DICOM dataset to numpy data format.
    image = ds.pixel_array
    print("max = " + str(np.max(image)))
    print("min = " + str(np.min(image)))
    # image = (image.astype(np.int32) - 32768).astype(np.int16)  # Calibrate the bias of the gray image.
    
    cv2.imshow("CT", image)
    
    key = cv2.waitKey(0)  # 等待按键命令, 1000ms 后自动关闭
    # destroyAllWindows()