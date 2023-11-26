import cv2
import sys
from typing import List


def check_cameras(max_cameras=10) -> List[int]:
    """Check for available cameras.

    Args:
        max_cameras (int, optional): Max amount of cameras to check for. Defaults to 10.

    Returns:
        List[int]: Index list of available Cameras.
    """
    available_cameras = []
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for Windows
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

# Check for available cameras
cameras = check_cameras()
print(f"Available Cameras: {cameras}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")
else:
    print("Webcam is online.")
    try:
        while True:
            # Capture frame-by-frame
            ret, img = cap.read()
            
            # If frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting...")
                break
                
            cv2.imshow('Camera', img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        