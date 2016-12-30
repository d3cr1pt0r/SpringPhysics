import math

def getLength(vector):
    return math.sqrt(vector.x * vector.x + vector.y * vector.y)

def getNormalized(vector):
    return vector / getLength(vector)

def dotProduct(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y