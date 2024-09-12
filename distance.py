import math

x1, x2 = input().split(',')
y1, y2 = input().split(',')
x1 = math.radians(float(x1))
x2 = math.radians(float(x2))
y1 = math.radians(float(y1))
y2 = math.radians(float(y2))
Distance = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) + \
                                math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print(Distance)
