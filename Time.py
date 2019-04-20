#Get the current time
#Author: Joshua Roberts
import time

def getTime():
    "This function returns the time in a formatted string"
    localTime = time.asctime(time.localtime(time.time()))
    return localTime

def getSplitTime():
    "This function returns a parsed time to be used as a file label"
    timeStamp = getTime()
    timeStampArray = str(timeStamp).split()
    newTimeStamp = timeStampArray[0] + "-" + timeStampArray[1] + "-" + timeStampArray[2] + "-" + timeStampArray[3] + "-" + timeStampArray[4]
    return newTimeStamp

