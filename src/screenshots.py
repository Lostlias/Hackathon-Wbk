import cv2
import os

# Create a directory to store screenshots if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Function to capture and save screenshots
def capture_screenshot(img, count):
    screenshot_path = f"screenshots/screenshot_{count}.png"
    cv2.imwrite(screenshot_path, img)
    print(f"Screenshot saved: {screenshot_path}")

while True:
    success, img = cap.read()
    if not success:
        break

    # Show the frame from webcam
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
