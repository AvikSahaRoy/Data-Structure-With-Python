class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class Linkedlist:
    def __init__(self):
        self.start = None
        
    # -------------- Insert at last -------------------
    def insert_at_last(self, item):
        n = Node(item)
        if self.start == None:
            self.start = n
        else:
            t = self.start
            while(t.link != None):
                t = t.link
            t.link = n
        print(f"{n.info} is inserted at the last")

    # --------------- Traverse -------------------
    def traverse(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty")
        else:
            print("List is: ")
            while(t != None):
                print(t.info, end='->')
                t = t.link

    # ------------ Reverse list --------------------
    def Reverse(self):
        t = self.start
        l = []
        top = -1
        if t == None:
            print("List is empty")
            return
        while(t != None):
            l.append(t.info)
            t = t.link
            top += 1
        print("Reverse list is: ")
        while top != -1:
            g = l.pop(top)
            print(g, end='->')
            top-=1
            
    def list_reverse(self):
        prev = None
        current = self.start
        next = current.link

        while current:
            current.link = prev
            prev = current
            current = next
            if next:
                next = next.link
        self.start = prev
        print("List is Reversed")

l = Linkedlist()
while(True):
    print("\n<<-------- Single Linked List operations -------->>\n")
    print("  1. Insert at Last")
    print("  2. Traverse")
    print("  3. Reverse")
    print("  4. List Reverse")
    print("  5. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        item = int(input("Enter your value: "))
        l.insert_at_last(item)
    elif ch == 2:
        l.traverse()
    elif ch == 3:
        l.Reverse()
    elif ch == 4:
        l.list_reverse()
    elif ch == 5:
        break
    else:
        print("Invalid Input")