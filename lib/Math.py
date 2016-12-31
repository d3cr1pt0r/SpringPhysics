import math

def getLength(vector):
    return math.sqrt(vector.x * vector.x + vector.y * vector.y)

def getDistance(v1, v2):
    return abs(getLength(v1-v2))

def getNormalized(vector):
    return vector / getLength(vector)

def dotProduct(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y