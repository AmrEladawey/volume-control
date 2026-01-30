from email.mime import image
import cv2
import time
import numpy as np
import HandTrackingModule as htm
from pycaw.pycaw import AudioUtilities 

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) >= 9:  # Check if we have at least 9 landmarks
        # Get coordinates of index finger tip and thumb tip (Normalized to pixel values)
        x1, y1 = int(lmList[8][1] * wCam), int(lmList[8][2] * hCam)
        x2, y2 = int(lmList[4][1] * wCam), int(lmList[4][2] * hCam)

        # cv2.line(image, start_point, end_point, color, thickness)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # Draw circles at the tips to make it look cleaner
        cv2.circle(img, (x1, y1), 10, (255, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 255, 0), cv2.FILLED)
        length = np.hypot(x2 - x1, y2 - y1)
        
        # Map length to volume (0-300 pixels = 0.0-1.0 volume)
        vol = np.interp(length, [20, 300], [0, 1])
        vol = np.interp(length, [20, 300], [0, 1])
        volume.SetMasterVolumeLevelScalar(vol, None)
        
        # Display on screen
        cv2.putText(img, f'Vol: {int(vol*100)}%', (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime != 0 else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 90), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break