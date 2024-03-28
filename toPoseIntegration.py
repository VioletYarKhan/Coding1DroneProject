import threading

from djitellopy import tello
import keyPressModule as kp
import time
import cv2
import math



kp.init()
eggbert = tello.Tello()
eggbert.connect()
# x, y, rot
pose = [0, 0, 0]
print("Battery: " + str(eggbert.get_battery()))
global img

eggbert.streamon()


def goToAngle(yawEnd, yawStart):
    # Find shortest rotation direction
    if (eggbert.get_yaw() > yawEnd):
        eggbert.rotate_clockwise(yawEnd - yawStart)
    else:
        eggbert.rotate_counter_clockwise(yawStart - yawEnd)
    return ((1/36) * (math.fabs(yawStart - yawEnd)))


def goDistance(distCm):
    eggbert.move_forward(distCm)
    time.sleep(distCm / 50)

def toPose(x, y, rot):
    global pose
    print(math.degrees(math.atan2((x - pose[0]) / (y - pose[1]))))
    # Calculate angle to new pose in degrees
    angleToNewPose = math.degrees(math.atan((x - pose[0]) / (y - pose[1])))
    # Rotate to new angle
    time.sleep(goToAngle(angleToNewPose, pose[2]))
    # Move to new position
    goDistance(math.sqrt((x - pose[0]) ^ 2) + (y - pose[1]) ^ 2)
    # Rotate to desired final orientation
    time.sleep(goToAngle(rot, pose[2]))
    # Update pose
    pose = [x, y, rot]

def resetPose():
    global pose
    pose = [0, 0, 0]

def getImg():
    while True:
        img = eggbert.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Image", img)
        cv2.waitKey(2)

imgCap = threading.Thread(target=getImg, args=(1,))
imgCap.start()


# Example usage
resetPose()
toPose(100, 0, 90)
toPose(0, 0, 0)