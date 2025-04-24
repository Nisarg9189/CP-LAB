class Solid:
    
    def __init__(self, radius, solid_type, dimensions, matirial):
        self.radius = radius
        self.solid_type = solid_type.lower()
        self.dimensions = dimensions
        self.matirial = matirial
    
    def volume(self):
        type = self.solid_type
        dimensions = self.dimensions
        
        if type == 'cube':
            side = dimensions.get('side', 0)
            return side ** 3
        elif type == 'sphere':
            r = dimensions.get('radius', 0)
            return (4/3) * 3.14 * r ** 3
        elif type == 'cylinder':
            r = dimensions.get('radius', 0)
            h = dimensions.get('height', 0)
            return 3.14 * r ** 2 * h
        
    def surface_area(self):
        type = self.solid_type
        dimensions = self.dimensions
        
        if type == 'cube':
            side = dimensions.get('side', 0)
            return 6 * side**2
        elif type == 'sphere':
            r = dimensions.get('radius', 0)
            return 4 * 3.14 * r**2
        elif type == 'cylinder':
            r = dimensions.get('radius', 0)
            h = dimensions.get('height', 0)
            return 2 * 3.14 * r * (r + h)
    
    def __str__(self):
        return f"Solid Type: {self.solid_type}, Material: {self.matirial}, Dimensions: {self.dimensions}"
    
s1 = Solid(5, 'cube', {'side': 5}, 'steel')
print(s1.volume())
print(s1.surface_area())
print(s1)