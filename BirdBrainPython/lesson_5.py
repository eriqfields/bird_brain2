from BirdBrain import Finch
from time import sleep 
bird = Finch()

'''
print("exercise1")
if bird.getButton('A') or bird.getButton('B'):
    print(bird.getButton('A'))
    print(bird.getButton('B'))
    bird.setBeak(0,100,0)
else:
        bird.setBeak(100,0,0)
sleep(1)
bird.stopAll()

print("exercise2")
if bird.getButton('B'):
    bird.setMove('B',10,20)
else:
        bird.setMove('F',10,20)
sleep(1)
bird.stopAll()
'''
print("exercise4")
while bird.getDistance() > 30 :
    print(bird.getDistance())
    bird.setBeak(100,0,0)
    bird.setMove('F',10,20)

print(bird.getDistance())
bird.stopAll()

