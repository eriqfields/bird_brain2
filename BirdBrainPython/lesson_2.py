from BirdBrain import Finch
bird = Finch()

print("exercise1")
print("Distance: ", bird.getDistance())

print("exercise2")
print("print the Right Light: ", bird.getLight('R'))
print("print the Left Light: ", bird.getLight('L'))
print("print the Button A: ", bird.getButton('A'))
print("print the Orientation: ", bird.getOrientation())

print("exercise3")
print(type(bird.getDistance()))

print("exercise4")
currentDistance = bird.getDistance()
print(currentDistance)
print(2*currentDistance)
print(4*currentDistance)

print("exercise5")
currentDifferernce = bird.getDifference()
print(currentDifferene)
print(2*currentDiffernece)
print(4*currentDiffernece)
