import math

pi = math.acos(-1.0)

def to_rad(alpha):
    return alpha * pi / 180.0

def make_point(R, lat, lon):
    x = R * math.cos(to_rad(lat)) * math.cos(to_rad(lon))
    y = R * math.cos(to_rad(lat)) * math.sin(to_rad(lon))
    z = R * math.sin(to_rad(lat))
    return x, y, z

def dist(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))

data = open("input.txt").read().split()
idx = 0
R = float(data[idx]); idx += 1
lat = float(data[idx]); idx += 1
lon = float(data[idx]); idx += 1
A = make_point(R, lat, lon)
lat = float(data[idx]); idx += 1
lon = float(data[idx]); idx += 1
B = make_point(R, lat, lon)

D = dist(A, B)
alpha = 2 * math.asin(D / 2 / R)
print(f"{alpha * R:.2f}")