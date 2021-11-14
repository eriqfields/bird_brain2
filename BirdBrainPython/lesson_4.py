from BirdBrain import Finch
from time import sleep 
bird = Finch()

print("execise1")
bird.setMotors(50,50)
sleep(1)
bird.stop()

print("execise2")
rightwheel = int(input("how fast should the right wheel go? "))
leftwheel = int(input("how fast should the left wheel go? "))
bird.setMotors(rightwheel,leftwheel)
sleep(5)
bird.stopAll()

print("execise3")
bird.setMotors(25,40)
sleep(2)
bird.setMotors(20,20)
sleep(1)
bird.setMotors(40,15)
sleep(4)
bird.setMotors(40,40)
sleep(2)
bird.setMotors(25,40)
sleep(3)
bird.setMotors(40,40)
sleep(2)
bird.stopAll()

print("execise4")
color = input("Please enter a letter:  ")
if (color =='g'):
    bird.setBeak(0,100,0)
else:
        print('Sorry that is not my favorite letter!')
sleep(1)
bird.stopAll()

print("execise5")
turn = input("Please enter a letter:  ")
if (turn == 'r'):
     bird.setMotors(70,50)
else:
            bird.setMotors(50,70)
sleep(1)
bird.stopAll()

print("execise6")
userResponse = input("Please enter a speed (-10 to 10):  ")
speed = int(userResponse)
if (speed >= -10) and (speed <= 10):
    bird.setMotors(speed,speed)
    sleep(1)
    bird.stopAll()
else:
        print("That speed is not vaild!")

print("execise7")
userResponse = input("Please enter a speed (0 to 50):  ")
speed = int(userResponse)
if (speed >= 0) and (speed <= 50):
    bird.setMotors(speed,speed)
    sleep(1)
else:
            bird.setMotors(50,0)
            sleep(1)
bird.stopAll()

print("execise8")
bird.setMotors(50,25)
bird.setTail(3,100,0,100)
sleep(1)
bird.setMove('B',20,35)
bird.setTail(1,0,100,0)
bird.setMove('F',20,35)
bird.stopAll()
bird.setMotors(90,10)
bird.setBeak(50,0,100)
sleep(8)
bird.stopAll()

            

