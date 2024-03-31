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
pose2D = [0, 0, 0]
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

def toPose2D(x, y, rot):
    global pose2D
    # Calculate angle to new pose in degrees
    angleToNewPose = math.degrees(math.atan2((x - pose2D[0]), (y - pose2D[1])))
    # Rotate to new angle
    time.sleep(goToAngle(int(angleToNewPose), pose2D[2]))
    # Move to new position
    goDistance(math.sqrt((x - pose2D[0]) ^ 2) + (y - pose2D[1]) ^ 2)
    # Rotate to desired final orientation
    time.sleep(goToAngle(rot, pose2D[2]))
    # Update pose
    pose2D = [x, y, rot]

def resetPose2D():
    global pose2D
    pose2D = [0, 0, 0]

def background():
    while True:
        img = eggbert.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Image", img)
        cv2.waitKey(2)
        if kp.getKey("z"): eggbert.land()
        if kp.getKey("x"): eggbert.emergancy()

back = threading.Thread(target=background, args=(1,))
back.start()


# Example usage
eggbert.takeoff()
resetPose2D()
toPose2D(100, 0, 90)
toPose2D(0, 0, 0)
eggbert.land()