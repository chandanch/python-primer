"""
    Named tuples are used in place of data classes.
    A Data class is a class which has only properties but no methods in it.
"""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "dec"])

p1 = Point(x=1, y=2, dec=100)
p2 = Point(x=1, y=2, dec=100)

print(p1.dec, p2.dec)