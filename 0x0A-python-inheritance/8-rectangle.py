#!/usr/bin/python3
from base_geometry import BaseGeometry
from rectangle import Rectangle

r = Rectangle(3, 5)

print(r)  # Output: <rectangle.Rectangle object at 0x7f6f488f7eb8>
print(dir(r))  # Output: List of attributes and methods of the Rectangle object

try:
    print("Rectangle: {} - {}".format(r._Rectangle__width, r._Rectangle__height))  # Output: [AttributeError] 'Rectangle' object has no attribute 'width'
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)  # Output: [TypeError] height must be an integer
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
