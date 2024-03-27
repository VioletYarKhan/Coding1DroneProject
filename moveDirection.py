from djitellopy import tello

from time import sleep

eggbert = tello.Tello()
eggbert.connect()
print("Battery: " + str(eggbert.get_battery()))




eggbert.takeoff()
eggbert.send_rc_control(0, 50, 0, 0)
sleep(2)
eggbert.send_rc_control(0, 0, 0, 180)
sleep(2)
eggbert.send_rc_control(0, 100, 0, 0)
sleep(7)
eggbert.send_rc_control(0, 0, 0, 0)
eggbert.land()

