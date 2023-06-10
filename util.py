# Importing the required modules
import numpy as np
import cv2


# Defining the function
def get_limit(color):
    # Reading the color as a numpy array since cv2.cvtColor expects an array like object
    col = np.uint8([[color]])
    # Converting BGR to HSV
    hsvcol = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)
    # Storing the HSV value in hsv variable
    hsv = hsvcol[0][0][0]

    # Getting the upper and lower limit
    # If hue is 0, subtracting from 0 hue value will result in subtraction from 255,
    # due to the cyclic nature of the hue values
    if hsv == 0:
        lowerlimit = np.array([hsv - 0, 100, 100], dtype=np.uint8)
    else:
        lowerlimit = np.array([hsv - 10, 100, 100], dtype=np.uint8)

    upperlimit = np.array([hsv + 10, 255, 255], dtype=np.uint8)

    return lowerlimit, upperlimit
