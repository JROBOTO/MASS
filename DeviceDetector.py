#Device Detector to detect when the specific phone is present
#Author: Joshua Roberts
import nmap
import Constants

networkScanner = nmap.PortScanner()
device = Constants.LOCAL_NETWORK_PORT

def detectSpecificDevice():
    "Detect whether a certain device is nearby"
    networkScanner.scan(device)
    for detectedDevice in networkScanner.all_hosts():
        if str(detectedDevice) == device:
            return True
        
    return False

