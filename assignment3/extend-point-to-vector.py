# Task 5:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # calc. euclid distance for 2D
    def euclidean_dist(self, other):
        return math.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
        
    
class Vector(Point):
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, new):
        return Vector(self.x + new.x, self.y + new.y)

point1 = Point(10, 20)
point2 = Point(30, 40)
str1 = point1.__str__()
str2 = point2.__str__()   
print(f"POINT 1: {str1}")
print(f"POINT 2: {str2}") 
print(f"Are points equal?: {point1 == point2}")
print(f"Euclidean distance: {point1.euclidean_dist(point2):.2f}")
vector1 = Vector(50, 60)
vector2 = Vector(70, 80)
print(f"VECTOR 1: {vector1}")
print(f"VECTOR 2: {vector2}")
print(f"Add Vectors: {vector1 + vector2}")