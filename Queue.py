class Queue:
    def __init__(self, m):
        self.list = [0] * m
        self.max = m
        self.front = -1
        self.rear = -1

    def Insertion(self):
        if self.rear == self.max - 1:
            print("Queue is already full")
            return
        else:
            self.rear += 1
            item = int(input("Enter the value: "))
            self.list[self.rear] = item
            print(f"{item} Inserted Successfully")

        if self.front == -1:
            self.front = 0
            return

    def Traverse(self):
        if self.list == [0] * self.max:
            print("Queue is empty")
        elif self.front == -1:
            print("Queue is empty")
        else:
            print("Queue is:",self.list[self.front:])

    def Deletion(self):
        if self.front == -1:
            print("Queue is empty")
            return
        else:
            item = self.list[self.front]
            print(f"{item} Deleted Successfully")

        if self.front == self.rear:
            self.front = - 1
            self.rear = - 1
        else:
            self.front += 1
            return

n = int(input("Enter the size of the Queue: "))
obj = Queue(n)
if __name__ == "__main__":
    while(True):
        print("\n----- Queue operations -----")
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