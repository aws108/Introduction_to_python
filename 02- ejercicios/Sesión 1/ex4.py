#!/usr/bin/python

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars avaible."
print "There are only", drivers, "drivers avaible."
print "There wil be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"

print "\r"

print type(cars),cars
print type(space_in_a_car), space_in_a_car
print type(drivers), drivers
print type(passengers), passengers
print type(cars_not_driven), cars_not_driven
print type(carpool_capacity), carpool_capacity
print type(average_passengers_per_car), average_passengers_per_car
