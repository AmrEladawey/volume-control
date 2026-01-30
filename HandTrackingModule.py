import cv2
import mediapipe as mp
import time

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.results = None  # Initialize results

        self.mpHands = mp.solutions.hands # Hands object
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                         max_num_hands=self.maxHands,
                                         min_detection_confidence=self.detectionCon,
                                         min_tracking_confidence=self.trackCon) # Hands instance
        self.mpDraw = mp.solutions.drawing_utils # Draw the points/lines
    
    def findHands(self, img, draw=True): # Find hands and draw landmarks
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Change the color space (BGR->RGB)
        self.results = self.hands.process(imgRGB) # Process the RGB image to find hands

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_landmarks,
                                                self.mpHands.HAND_CONNECTIONS) # Draw the landmarks and connections
        return img
    
    def findPosition(self, img, handNo=0, draw=True): # Find position of landmarks
        lmList = []
        if self.results.multi_hand_landmarks and handNo < len(self.results.multi_hand_landmarks):
            myHand = self.results.multi_hand_landmarks[handNo]

            for landmark_id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape # Getting the dimensions of the image
                cx, cy = int(lm.x * w), int(lm.y * h) # Converting the landmark coordinates to pixel values
               
                lmList.append([landmark_id, lm.x, lm.y]) # Append id and normalized coordinates
                
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED) # Draw circle at each landmark
        
        return lmList

def main(draw_landmarks=True):
    pTime = 0
    cap = cv2.VideoCapture(0) # Video object
    detector = handDetector()

    while True: # working loop
        success, img = cap.read() # Read frame from camera
        img = detector.findHands(img, draw=draw_landmarks)
        lmList = detector.findPosition(img, draw=draw_landmarks)


        cTime = time.time()
        fps = 1 / (cTime - pTime) if pTime != 0 else 0
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)  
        
        if not success:
            break
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
if __name__ == "__main__":
    main()