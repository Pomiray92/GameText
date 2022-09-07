import math

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius**2) * (height)
    return vol

if __name__ == "__main__":
    print(cylinder_volume(2, 4))