from djitellopy import tello

import cv2

eggbert=tello.Tello()
eggbert.connect()
print("Battery: " + str(eggbert.get_battery()))

eggbert.streamon()

while True:
    img=eggbert.get_frame_read().frame
    img=cv2.resize(img, (360,240))
    cv2.imshow("Image",img)
    cv2.waitKey(1)
