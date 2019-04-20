#This file will control the PIR (Passive Infra Red) motion sensor
#Author: Joshua Roberts
import RPi.GPIO as GPIO
import Constants

GPIO.setmode(GPIO.BCM)
GPIO.setup(Constants.PIR_PIN, GPIO.IN)

def detectMotion():
    "A function to detect motion returning true if it has"
    if GPIO.input(Constants.PIR_PIN):
        return True
    return False

