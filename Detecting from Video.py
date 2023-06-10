# Importing the required libraires
import cv2
from util import get_limit
from PIL import Image

# Getting the Video
cap = cv2.VideoCapture("data/ballon.mp4")

# Asking user for the color using BGR color code
bgr_color = input("Enter the BGR color value (e.g., 0 0 255 for red): ")
bgr_color = [int(val) for val in bgr_color.split()]

# If answered wrong amount of values, the default yellow color will be selected
if len(bgr_color) != 3:
    print("Invalid BGR color value entered. Using default yellow.")
    bgr_color = [0, 255, 255]

# Uncomment the Optional code to save the output video
# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():

    ret, frame = cap.read()  # Reading the frame

    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Converting BGR 2 HSV

    lower_limit, upper_limit = get_limit(color=bgr_color)  # Getting lower and upper limit from get_limit function

    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)  # Creating mask based on limits

    mask_ = Image.fromarray(mask)  # Converting mask array to an Image using PIL library

    bbox = mask_.getbbox()  # Getting bounding box

    if bbox is not None:
        x1, y1, x2, y2 = bbox  # Getting the box co-ordinates

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)  # Drawing the rectangle

    cv2.imshow('Result', frame)  # Showing the frame

    #saving the output
    #out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#realse the output variable
#out.release()
cap.release()
cv2.destroyAllWindows()
