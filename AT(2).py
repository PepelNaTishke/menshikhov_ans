import math

def make_point(R, lat, lon):
    return (
        R * math.cos(math.radians(lat)) * math.cos(math.radians(lon)),
        R * math.cos(math.radians(lat)) * math.sin(math.radians(lon)),
        R * math.sin(math.radians(lat))
    )

R, lat1, lon1, lat2, lon2 = map(float, input().split())

A = make_point(R, lat1, lon1)
B = make_point(R, lat2, lon2)

D = math.dist(A, B)
alpha = 2 * math.asin(D / 2 / R)
print(f"{alpha * R:.2f}")