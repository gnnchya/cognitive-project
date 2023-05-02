import cv2
import numpy as np

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Define the lower and upper bounds of the color to be detected
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask by thresholding the HSV image using the lower and upper bounds
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Apply morphological operations to the mask to remove noise and smooth the edges of the detected objects
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.erode(mask, kernel, iterations=1)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)


    # Find contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            # Approximate the contour
            approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt, True), True)

            # If the contour has 3 vertices, it is a triangle
            if len(approx) == 3:
                cv2.drawContours(frame, [approx], 0, (0, 0, 255), 2)
                cv2.putText(frame, "Triangle", (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # If the contour has 4 vertices, it is a rectangle
            elif len(approx) == 4:
                # cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
                cv2.putText(frame, "Rectangle", (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


            # Draw contours on the original image
            cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)

            # Show the result
            cv2.imshow('m', mask)
            cv2.imshow("result", frame)

    # Wait for a key press and exit the loop if "q" is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()