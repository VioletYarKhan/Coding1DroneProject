import threading

from djitellopy import tello
import keyPressModule as kp
import time
import math
i = 0


kp.init()
eggbert = tello.Tello()
eggbert.connect()
# x, y, rot
pose2D = [0, 0, 0]
print("Battery: " + str(eggbert.get_battery()))
global img

eggbert.streamon()


def goToAngle(yawEnd, yawStart):
    # Find the shortest rotation direction
    yawDist = float(yawEnd - yawStart)
    if (yawDist > 0):
        eggbert.rotate_clockwise(int(math.fabs(yawDist)))
    else:
        eggbert.rotate_counter_clockwise(int(math.fabs(yawDist)))

def toPose2D(x, y, rot):
    global pose2D
    # Calculate angle to new pose in degrees
    angleToNewPose = int(math.degrees(math.atan2((x - pose2D[0]), (y - pose2D[1]))))
    print(angleToNewPose)
    # Rotate to new angle
    goToAngle(int(angleToNewPose), pose2D[2])
    # Move to new position
    eggbert.move_forward(int(math.sqrt((x - pose2D[0]) ** 2) + (y - pose2D[1]) ** 2))
    # Rotate to desired final orientation
    goToAngle(int(rot), int(pose2D[2]))
    # Update pose
    pose2D = [x, y, rot]

def resetPose2D():
    global pose2D
    pose2D = [0, 0, 0]

# Example usage

