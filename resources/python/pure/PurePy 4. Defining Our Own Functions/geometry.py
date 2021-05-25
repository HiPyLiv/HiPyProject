import math

def area_of_circle(radius):
    return math.pi * radius**2


def area_of_triangle(sideA, sideB, angle=90):
    '''
    Takes two sides of a triangle and the angle
    between them (measured in degrees).
    Returns area of triangle.
    If no angle is given, is equivalent to
    base * height / 2
    '''
    angle = math.radians(angle)
    return sideA*sideB*math.sin(angle) / 2


def pythagorean_theorem(a=None, b=None, c=None):
    '''
    Takes two sides of a right-angle triangle
    as keyword arguments.
    (c is hypotenuse)
    and returns length of other side.
    Example:
    >>> pythagorean_theorem(a=3, b=4)
        5.0
    '''
    if a and b:
        return math.sqrt(a**2 + b**2)
    elif a and c:
        return math.sqrt(c**2 - a**2)
    elif b and c:
        return math.sqrt(c**2 - b**2)
    else:
        print("Not enough information given")
        return None

def ngon_area():
    return area
