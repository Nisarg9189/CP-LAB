class Str:
    
    def __init__(self, string):
        self.string = string
    
    def __iadd__(self, other):
        self.string += other.string
        return self
    
    def tolower(self):
        return Str(self.string.lower())
    
    def toupper(self):
        upper_string = ''.join([chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in self.string])
        return Str(upper_string)

    def Output(self):
        print(self.string)
    
s1 = Str('hello')
s2 = Str('world')
s1 += s2
s1.Output()  
s1.tolower().Output()  
s1.toupper().Output()  