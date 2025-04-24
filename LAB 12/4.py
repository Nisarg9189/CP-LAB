import math

class Shape:
    def __init__(self, shape_type, dimensions, material=None):
        """
        shape_type: str - e.g., 'square', 'circle', 'triangle', 'hexagon'
        dimensions: dict - shape-specific dimensions
        material: optional str - like 'wood', 'metal', etc.
        """
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        self.material = material

    def area(self):
        s = self.shape_type
        d = self.dimensions

        if s == 'square':
            side = d.get('side', 0)
            return side * side
        elif s == 'circle':
            r = d.get('radius', 0)
            return math.pi * r * r
        elif s == 'equilateral triangle':
            side = d.get('side', 0)
            return (math.sqrt(3) / 4) * side * side
        elif s == 'regular hexagon':
            side = d.get('side', 0)
            return (3 * math.sqrt(3) / 2) * side * side
        else:
            raise ValueError("Unsupported shape type")

    def perimeter(self):
        s = self.shape_type
        d = self.dimensions

        if s == 'square':
            side = d.get('side', 0)
            return 4 * side
        elif s == 'circle':
            r = d.get('radius', 0)
            return 2 * math.pi * r
        elif s == 'equilateral triangle':
            side = d.get('side', 0)
            return 3 * side
        elif s == 'regular hexagon':
            side = d.get('side', 0)
            return 6 * side
        else:
            raise ValueError("Unsupported shape type")

    def __str__(self):
        return f"Shape Type: {self.shape_type}, Material: {self.material}, Dimensions: {self.dimensions}"

# Example usage
s1 = Shape('square', {'side': 5}, 'wood')
print(s1.area()) 
print(s1.perimeter()) 
print(s1)  # Output: Shape Type: square, Material: wood, Dimensions: {'side': 5}
