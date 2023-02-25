import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

# Set up the servo motors
pan_pin = 17
tilt_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)
pan_servo = GPIO.PWM(pan_pin, 50)
tilt_servo = GPIO.PWM(tilt_pin, 50)

# Pi camera
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

#  haarcascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# center of the  frame
frame_center = (320, 240)

# Define the angle range of the servo motors
pan_range = (0, 180)
tilt_range = (0, 180)

# Function to move the pan servo motor
def move_pan(angle):
    duty_cycle = angle / 18 + 2
    pan_servo.ChangeDutyCycle(duty_cycle)

# move the tilt servo motor
def move_tilt(angle):
    duty_cycle = angle / 18 + 2
    tilt_servo.ChangeDutyCycle(duty_cycle)

# Main loop
while True:
    # Read a frame from the camera
    ret, frame = camera.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a face is detected, move the servo motors to center the face
    if len(faces) > 0:
        # Get the coordinates of the first face detected
        (x, y, w, h) = faces[0]

        # Calculate the center of the face
        face_center = (x + w//2, y + h//2)

        # Calculate the difference between the face center and the frame center
        delta_x = face_center[0] - frame_center[0]
        delta_y = face_center[1] - frame_center[1]

        # Calculate the angle to move the pan and tilt servo motors
        pan_angle = int(np.interp(delta_x, [-320, 320], list(pan_range)))
        tilt_angle = int(np.interp(delta_y, [-240, 240], list(tilt_range)))

        # Move the servo motors to center the face
        move_pan(pan_angle)
        move_tilt(tilt_angle)

    # Show the frame with the detected face
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()
