import imutils
from imutils.video import VideoStream
import time
import cv2
import RPi.GPIO as GPIO
#Start feed (2 seconds to not overrun RAM of rasppi)
vs = VideoStream(src=0).start()
time.sleep(2.0)
firstFrame = None
#servo setup
servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(0)
print("Meow")

#Note: Per frame cycle, check RAM capacity of RPi before using Note2: Functional
while True:
        frame = vs.read()
        #Gray Screen
        frame = imutils.resize(frame, width=500) #Resize frame to fit window
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Render gray for frame delta
        gray = cv2.GaussianBlur(gray, (21, 21), 0) #Erase detail change for bad webcam
        if firstFrame is None: #Render screen gray for firstframe
                firstFrame = gray
                continue
        #Absolute Difference computation
        cnts = None #reset contours per loop
        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] #Thresh computation DO NOT TOUCH I HAVE NO IDEA WHAT IS GOING ON
        thresh = cv2.dilate(thresh, None, iterations=2) #Dilate to fill in holes, fixed.
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, #Find contours AKA chamges
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        if cnts:
                print("Motion detected")
                p.ChangeDutyCycle(1)
                time.sleep(0.8)
                p.ChangeDutyCycle(0)
                print("Cooldown started.")
                time.sleep(15) #Change this line to adjust the cooldown
                print("Cooldown over.")
                #Add further actions (motor, etc) here
#Cleanup
vs.stop()
cv2.destroyAllWindows()
