# Import the necessary libraries
import cv2  # OpenCV library for computer vision tasks
import numpy as np  # NumPy library for numerical operations

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # Use the default camera (0) to capture frames

# Loop runs as long as capturing has been initialized
while True:

    # Read frames from the camera
    ret, frame = cap.read()

    # Convert the color space from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of red color in HSV
    # Hue: represents the color, Saturation: represents the intensity of the color, Value: represents the brightness
    # The lower_red and upper_red arrays represent the lower and upper boundaries of the red color range in HSV.
    # These values can be adjusted to detect different colors by changing the range in HSV.
    lower_red = np.array([0, 120, 70])  # Lower boundary of red color
    upper_red = np.array([10, 255, 255])  # Upper boundary of red color

    # Create a mask to threshold the HSV image to detect red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

   
     # Apply bitwise AND operation to extract only the red regions from the original frame
    # performs a bitwise AND operation between the original frame (frame) and the mask we created earlier (mask).
    # This operation keeps only the pixels that have a value of 1 (white) in both the original frame and the mask.
    # As a result, all pixels except those corresponding to red regions in the original frame will become black (0,0,0).
    # The result of this operation, stored in res, will be an image where only the red regions from the original frame are retained,
    # and the rest is blacked out.
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original image
    cv2.imshow('Original', frame)

    # Find edges in the input image using the Canny edge detection algorithm
    # Canny edge detection algorithm detects edges in the image by looking for areas of rapid intensity change.
    edges = cv2.Canny(frame, 100, 200)

    # Display the edges in a separate window
    cv2.imshow('Edges', edges)

    # Wait for a key press. If the 'Esc' key (ASCII code 27) is pressed, exit the loop
    k = cv2.waitKey(5) & 0xFF
    if k == 32:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
