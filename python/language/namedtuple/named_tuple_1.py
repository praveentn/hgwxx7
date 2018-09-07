from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
Car
# <class '__main__.Car'>

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
# 'red'

my_car.mileage
# 3812.4

# We get a nice string repr for free:
my_car
# Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'
#AttributeError: "can't set attribute"
