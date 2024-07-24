# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:15:00 2024

@author: ABC
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc

# Create a MediaPipe Hands object
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

sensi=0.45

# Loop over the video frames
while True:

    # Capture a frame
    success, img = cap.read()

    hands,frame = detector.findHands(img) 
    
    # Find the hand and its landmarks
    if (not hands):
        title='No data'
    else:    
        hands1=hands[0]
        x1,y1,z1=hands1['lmList'][4]
        x2,y2,z2=hands1['lmList'][8]
        
        distance,temp,frame=detector.findDistance((x1,y1), (x2,y2), img=frame)
        # Print the distance
            
        
        bright=(distance*sensi)
        bright=bright*(int(not(bool(bright//100))))+100*(int(bool(bright//100)))
        sbc.set_brightness(bright)
        print("Brightness level: ",bright)
 
    cv2.imshow("Video",frame)
    if (cv2.waitKey(1)&0xFF in [ord("q"), ord("Q")]) :
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()