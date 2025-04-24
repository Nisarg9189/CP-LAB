class Matrix:
    def __init__(self, l):
        self.l = l

    def __add__(self, other):
        result = []
        for i in range(len(self.l)):
            row = []
            for j in range(len(self.l[0])):
                row.append(self.l[i][j] + other.l[i][j])
            result.append(row)
        return Matrix(result)
    
    def __mul__(self, other):
        result = []
        for i in range(len(self.l)):  
            row = []
            for j in range(len(other.l[0])):
                sum = 0
                for k in range(len(self.l[0])):  
                    sum += self.l[i][k] * other.l[j][k]
                row.append(sum)
            result.append(row)
        return Matrix(result)
    
    def transpose(self):
        for i in range(len(self.l)):
            for j in range(i+1, len(self.l)):
                self.l[i][j], self.l[j][i] = self.l[j][i], self.l[i][j] 

    def print_ans(self):
        for row in self.l:
            print(row)


l1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
l2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

m1 = Matrix(l1)
m2 = Matrix(l2)

# m3 = m1 + m2
# m3.print_ans()


# m4 = m1 * m2
# m4.print_ans()

m1.transpose()
m1.print_ans()

