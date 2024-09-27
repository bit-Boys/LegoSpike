from hub import light_matrix
import runloop
import motor
from hub import port
import time
from hub import motion_sensor as s


LEFT = port.A
RIGHT = port.C
upDown = port.E

touch = 0
notTouch = 90

Scale = 2000 # The seconds the big line of B is drawn in, at 500 deg/sec, measure distance and change,

# 1 sec at 500 deg / sec is appriximatly 9 inches
# 2 sec is 18 in

motor.reset_relative_position(upDown, 0)
s.reset_yaw(0)



#def make_Lsemicircle(rad):
    # Move to origin, makes a left semicircle of rad radius

async def goDown():
    await motor.run_to_relative_position(upDown, touch, 150)

async def goUp():
    await motor.run_to_relative_position(upDown, notTouch, 150)


async def change_heading(goTo):
    await goUp()

    current_yaw = s.tilt_angles()[0]

    going = True
    while going:
        current_yaw = s.tilt_angles()[1]
        print('Current Yaw: ')
        print(current_yaw)
        print('Going to: ')
        print(goTo)

        if current_yaw < goTo + 12:
            motor.run_for_time(LEFT, 50, 250)# turn direction
            motor.run_for_time(RIGHT, 50, 250)
        elif current_yaw + 12 > goTo:
            motor.run_for_time(LEFT, 50, -250)# turn direction
            motor.run_for_time(RIGHT, 50, -250)
        else:
            going = False


async def main():
    

    await goUp()
        
    ## back line of B
    motor.run_for_time(LEFT, Scale, 500)  # Basic forward
    motor.run_for_time(RIGHT, Scale, -500)

    time.sleep(2.5)


    #first line out, 12 inches
    await change_heading(90)

    time.sleep(2)

    await change_heading(180)

    time.sleep(2)


    await change_heading(0)




runloop.run(main())
