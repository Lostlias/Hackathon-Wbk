import os
from ultralytics import YOLO
import cv2
import torch
import math 
import pathlib
from pathlib import Path
pathlib.PosixPath = pathlib.WindowsPath

def capture_screenshot(img, count):
    screenshot_path = f"screenshots/screenshot_{count}.png"
    cv2.imwrite(screenshot_path, img)
    print(f"Screenshot saved: {screenshot_path}")

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = torch.hub.load("d:\\KIT\\HackAThonWBK24\\Yolo\\yolov5", "custom", path="d:\\KIT\\HackAThonWBK24\\Yolo\\yolov5\\runs\\train\\exp\\weights\\best.pt", source="local")

# object classes
classNames = ["emptybox", "fullbox"]

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Run inference
    results = model(img)

    # coordinates
    boxes = results.xyxy[0]  # Access the bounding boxes

    for box in boxes:
        # bounding box
        x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])

        # put box in cam
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # confidence
        confidence = math.ceil((box[4]*100))/100
        print("Confidence --->", confidence)

        # class name
        cls = int(box[5])
        print("Class name -->", classNames[cls])

        # object details
        org = (x1, y1 - 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 2

        cv2.putText(img, f"{classNames[cls]} {confidence}", org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord(' '):  # Change ' ' to ord(' ') for spacebar
        capture_screenshot(img, len(os.listdir("screenshots")) + 1)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2
import torch
import math
import os

# Create a directory to store screenshots if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load("d:\\KIT\\HackAThonWBK24\\Yolo\\yolov5", "custom", path="d:\\KIT\\HackAThonWBK24\\Yolo\\yolov5\\runs\\train\\exp\\weights\\best.pt", source="local")


# Object classes
classNames = ["emptybox", "fullbox"]

# Function to capture and save screenshots
def capture_screenshot(img, count):
    screenshot_path = f"screenshots/screenshot_{count}.png"
    cv2.imwrite(screenshot_path, img)
    print(f"Screenshot saved: {screenshot_path}")

# Start webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

while True:
    success, img = cap.read()
    if not success:
        break

    # Perform inference
    results = model(img)

    # Extract bounding boxes and class labels
    boxes = results.xyxy[0]  # Access the bounding boxes

    for box in boxes:
        x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])

        # Draw bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Confidence
        confidence = math.ceil((box[4] * 100)) / 100
        print("Confidence:", confidence)

        # Class name
        cls = int(box[5])
        print("Class name:", classNames[cls])

        # Display object details
        org = (x1, y1 - 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 2
        cv2.putText(img, f"{classNames[cls]} {confidence}", org, font, fontScale, color, thickness)

    # Show the annotated frame
    cv2.imshow('Webcam', img)

    # Capture screenshot on spacebar press
    if cv2.waitKey(1) == ord(' '):  # Change ' ' to ord(' ') for spacebar
        capture_screenshot(img, len(os.listdir("screenshots")) + 1)

    # Exit on 'q' press
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

