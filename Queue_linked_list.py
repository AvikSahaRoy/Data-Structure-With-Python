# Linked list representation of Queue :-----------
class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class QLinkedlist:
    def __init__(self):
        self.front = None
        self.rear = None

    # ------------- Insertion ------------------------
    def Insertion(self):
        item = int(input("Enter your value: "))
        n = Node(item)
        if (self.front == None) and (self.rear == None):
            self.front = n
            self.rear = n
        else:
            self.rear.link = n
            self.rear = n
        print(f"{n.info} is inserted")

    # ------------- Deletion ------------------------
    def Deletion(self):
        n = self.front
        if self.front == None:
            print("Queue is empty")
            return
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.link
        print(f"{n.info} is deleted")

    # ------------- Traverse ------------------------
    def Traverse(self):
        if (self.front == None) and (self.rear == None):
            print("Queue is empty")
        else:
            t = self.front
            print("Queue is: ")
            while t != None:
                print(t.info, end=" ")
                t = t.link

l = QLinkedlist()
while(True):
    print("\n<<--- Queue Linked List operations ---->>\n")
    print("   1. Insertion")
    print("   2. Deletion")
    print("   3. Traverse")
    print("   4. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        l.Insertion()
    elif ch == 2:
        l.Deletion()
    elif ch == 3:
        l.Traverse()
    elif ch == 4:
        break
    else:
        print("Invalid input")
