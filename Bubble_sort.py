class Bubble_Sort:
    def __init__(self):
        self.n = int(input("how many values: : "))
        self.l = []
        for i in range(self.n):
            temp = int(input(f"Enter your {i} value: "))
            self.l.append(temp)

    def Process(self):      
        for j in range(0, self.n-1):
            for k in range(0, self.n-j-1):
                if self.l[k] > self.l[k+1]:
                    self.l[k], self.l[k+1] = self.l[k+1], self.l[k]
        print(self.l)

if __name__ == "__main__":
    s = Bubble_Sort()
    s.Process()