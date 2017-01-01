import math

def getLength(v):
    return math.sqrt(v.x * v.x + v.y * v.y)

def getDistance(v1, v2):
    return abs(getLength(v1-v2))

def getNormalized(v):
    return v / getLength(v)

def dotProduct(v1, v2):
    return v1.x * v2.x + v1.y * v2.y