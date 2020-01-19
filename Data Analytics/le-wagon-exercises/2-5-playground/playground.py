# TODO: it's a playground, let's write some code (no unit tests to run here)
# New playground from Function
import math
pi = 3.14

def circle_math(radius):
    result = []
    result.append(pi * 2 * radius)
    result.append(pi * radius ** 2)
    result.sort()
    return result

## Test Cases for circle_math method
#values = circle_math(5)
#print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

#values = circle_math(6)
#print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

# Old Playground.py before Function
#pi = 3.14
#radius = 5
#r = f'The radius is set to {radius}'
#print(r)

#perimeter = 2 * pi * radius
#p = f'Perimeter of the circle is {round(perimeter,1)}'
#print(p)

#area = pi * (radius ** 2)
#a = f'Area of the disk is {area}'
#print(a)
def yell(word):
      return f"{word.upper()}!!!"

print(yell("hello"))