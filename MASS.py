#This is a Motion Activated Security System (MASS)
#This is the main file which will run the main loop and call each file when
#needed
#Author: Joshua Roberts

import Email
import DeviceDetector
import MotionDetector
import CameraInput
import Time
import GoogleDriveUploader
import thread
import sys

sharedDictionary = {"Device Detected": True, "Motion Detected": False}

def detectDevice():
    print("Ready to detect device...")
    while True:
        sharedDictionary["Device Detected"] = DeviceDetector.detectSpecificDevice()

def detectMotion():
    print("Ready to detect motion...")
    while True:
        sharedDictionary["Motion Detected"] = MotionDetector.detectMotion()

print("Running threads...")
thread.start_new_thread(detectDevice, ())
thread.start_new_thread(detectMotion, ())

print("Ready to run program...")
try:
    while True:
        if sharedDictionary["Motion Detected"] == True and sharedDictionary["Device Detected"] == False:
            #Listen for movement, start recording and send email
            print("INTRUDER ALERT")
            timeString = Time.getSplitTime()
            CameraInput.takeVideo(timeString)
            thread.start_new_thread(Email.sendEmail, (timeString,))
            thread.start_new_thread(GoogleDriveUploader.uploadVideo, (timeString,))
            print("You off to jail fool")
except KeyboardInterrupt:
    sys.exit(0)
