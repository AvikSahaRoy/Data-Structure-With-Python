class CircularQueue:
    def __init__(self, m):
        self.list = [0] * m
        self.max = m
        self.front = -1
        self.rear = -1

    def Insertion(self):
        if (self.rear + 1)%self.max == self.front:
            print("Queue is already full")
            return
        else:
            self.rear = (self.rear + 1)%self.max
            self.list[self.rear] = int(input("Enter the value: "))
            print("Value Inserted")

        if self.front == -1:
            self.front = 0
            return

    def Traverse(self):
        if self.list == [0] * self.max:
            print("Queue is empty")
            return
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front < self.rear:
            print("Queue is: ",self.list[self.front:self.rear+1])
        else:
            print("Queue is: ",self.list[self.front:self.max] + self.list[:self.rear+1])

    def Deletion(self):
        if self.front == -1:
            print("Queue is empty")
            return

        item = self.list[self.front]
        print(f"{item} is Deleted")

        if self.front == self.rear:
            self.front = - 1
            self.rear = - 1
        else:
            self.front = (self.front + 1)%self.max
            

n = int(input("Enter the size of the Queue: "))
obj = CircularQueue(n)
if __name__ == "__main__":
    while(True):
        print("\n----- CircularQueue Operations -----")
        print("1. Insertion")
        print("2. Traverse")
        print("3. Deletion")
        print("4. Exit\n")
        ch = int(input("Enter your Choice: "))
        if ch == 1:
            obj.Insertion()
        if ch == 2:
            obj.Traverse()
        if ch == 3:
            obj.Deletion() 
        if ch == 4:
            break
        else:
            print("Invalid Input")