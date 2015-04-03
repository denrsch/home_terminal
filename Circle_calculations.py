#calculating the area of a circle with input requests

import math 
radius_input = input("What size is the radius? ")
r = int(radius_input)

circle = math.pi * r * r

print "The area of the circle is %s" % (circle)

#calculating the area of a rectangle with a user prompt

width_input = input("how wide is your rectangle? ")
width = int(width_input)

length_input = input("how long is your rectangle? ")
length = int(length_input)

rectangle = length * width

print "looks like the area of your rectangle is %s" % (rectangle)