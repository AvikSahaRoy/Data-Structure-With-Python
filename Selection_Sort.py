class Selection_Sort:
    def __init__(self):
        self.n = int(input("Enter how many value you want to input: "))
        self.l = []
        for i in range(self.n):
            temp = int(input(f"Enter your {i} value: "))
            self.l.append(temp)

    def Process(self):      
        for j in range(0, self.n):
            for k in range(j+1, self.n):
                if self.l[j] > self.l[k]:
                    self.l[j], self.l[k] = self.l[k], self.l[j]
        print(self.l)

if __name__ == "__main__":
    s = Selection_Sort()
    s.Process() 