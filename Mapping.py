from djitellopy import tello
import keyPressModule as kp
from time import sleep


# Parameters
fSpeed = 117/10  # Forward speed in cm/second    (15 cm/s)
aSpeed = 360/10  # Angular speed in degrees/second
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval
#


kp.init()
eggbert = tello.Tello()
eggbert.connect()
print("Battery: " + str(eggbert.get_battery()))

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

    if kp.getKey("q"): eggbert.land
    if kp.getKey("e"): eggbert.takeoff


    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    eggbert.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


