#This file takes camera input via the gpio (General Purpose I/O)
#Author: Joshua Roberts
import os
import Constants

MILLISECONDS = 1000

def takeStillImage(time):
    "Takes the input from the camera in the form of a still image"
    systemCommand = "raspistill -o " + str(time) + ".jpg"
    os.chdir(Constants.IMAGES_DIR)
    os.system(systemCommand)
    os.chdir(Constants.HOME_DIR)

def takeVideo(time):
    "Takes a video of a specified length"
    videoLength = CONSTANTS.VIDEO_LENGTH * MILLISECONDS
    systemCommand = "raspivid -o " + str(time) + ".mp4 -t " + str(videoLength)
    os.chdir(Constants.VIDEOS_DIR)
    os.system(systemCommand)
    os.chdir(Constants.HOME_DIR)
 
