from djitellopy import tello

from time import sleep

eggbert = tello.Tello()
eggbert.connect()
print("Battery: " + str(eggbert.get_battery()))
i = 0


eggbert.takeoff()

eggbert.move_down(50)
while (i < 3):
    eggbert.move_forward(50)
    eggbert.rotate_counter_clockwise(60)
    i += 1

eggbert.rotate_counter_clockwise(60)
eggbert.move_forward(16)
eggbert.move_right(30)
eggbert.move_forward(16)
eggbert.move_left(30)

eggbert.land()
