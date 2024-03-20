from djitellopy import tello
import keyPressModule as kp
import time
import cv2



kp.init()
eggbert=tello.Tello()
eggbert.connect()
print("Battery: " + str(eggbert.get_battery()))
global img

eggbert.streamon()

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

    return [lr, fb, ud, yv]


while True:
    vals=getKeyboardInput()
    eggbert.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img=eggbert.get_frame_read().frame
    img=cv2.resize(img, (360,240))
    cv2.imshow("Image",img)
    cv2.waitKey(1)

