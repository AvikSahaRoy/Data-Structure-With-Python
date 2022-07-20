class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class Linkedlist:
    def __init__(self):
        self.start = None
        self.top = -1

    # -------------- Insert at last -------------------
    def insert_at_last(self, item):
        n = Node(item)
        if self.top == -1:
            self.start = n
            self.top+=1
        else:
            t = self.start
            while(t.link != None):
                t = t.link
            t.link = n
            self.top += 1
        print(f"{n.info} is inserted at the last")

    # ---------------- Delete last --------------------
    def delete_last(self):
        t = self.start
        if self.top == -1:
            print("Stack is empty please insert some value first")
        elif self.top == 0:
            self.start = None
            print(f"{t.info} item deleted Successfully at the Last")
            self.top -= 1
        else:
            while(t.link != None):
                prev = t 
                t = t.link 
            print(f"{t.info} item deleted Successfully at the last")
            prev.link = None
            self.top -= 1

    # --------------- Traverse -------------------
    def traverse(self):
        t = self.start
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack is: ")
            while(t != None):
                print(t.info, end='->')
                t = t.link

l = Linkedlist()
while(True):
    print("\n<<-------- Stack Linked List operations -------->>\n")
    print("  1. Insert at Last")
    print("  2. Delete at Last")
    print("  3. Traverse")
    print("  4. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        item = int(input("Enter your value: "))
        l.insert_at_last(item)
    elif ch == 2:
        l.delete_last()
    elif ch == 3:
        l.traverse()
    elif ch == 4:
        break
    else:
        print("Invalid Input")