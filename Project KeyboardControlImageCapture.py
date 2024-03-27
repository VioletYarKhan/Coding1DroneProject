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
    if (eggbert.get_yaw() > yawEnd):
        eggbert.rotate_clockwise(yawEnd - yawStart)
    else:
        eggbert.rotate_counter_clockwise(yawStart - yawEnd)
    return ((1/36) * (math.fabs(yawStart - yawEnd)))


def goDistance(distCm):
    eggbert.set_speed(50)
    time.sleep((distCm * 0.95) / 50)
    eggbert.set_speed(0)


def toPose(x, y, rot):
    global pose
    print(math.degrees(math.atan((x - pose[0]) / (y - pose[1]))))

    angleToNewPose = math.degrees(math.atan((x - pose[0]) / (y - pose[1])))
    time.sleep(goToAngle(angleToNewPose, pose[2]))
    goDistance(math.sqrt((x - pose[0]) ^ 2) + (y - pose[1]) ^ 2)
    time.sleep(goToAngle(rot, pose[2]))
    pose = [x, y, rot]


def resetPose():
    global pose
    pose = [0, 0, 0]

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): eggbert.land()
    if kp.getKey("e"): eggbert.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    eggbert.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = eggbert.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(2)


