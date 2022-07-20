class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def insert_first(self, item):
        n = Node(item)
        n.link = self.start
        self.start = n

    def insert_last(self, item):
        n = Node(item)
        t = self.start
        if self.start == None:
            self.start = n
        else:
            while(t.link != None):
                t = t.link
            t.link = n

    def delete_first(self):
        t = self.start
        if self.start == None:
            print("list is empty")
        else:
            prev = t
            t = t.link
            self.start = t
            del(prev)

    def delete_last(self):
        t = self.start
        if self.start == None:
            print("list is empty")
        elif t.link == None:
            self.start = None
        else:
            while(t.link != None):
                prev = t
                t = t.link
            prev.link = None

    def traverse(self):
        if self.start == None:
            print("List  is empty")
        else:
            t = self.start
            print("List is: ")
            while(t != None):
                print(t.info,end=" ")
                t = t.link

l = SingleLinkedList()
while(True):
    print("\n<<-------- Single Linked List operations -------->>\n")
    print("  <<--- Insertion --->>")
    print("  1. Insert at Begining")
    print("  2. Display")
    print("  3. Insert at last")
    print("  4. delete first")
    print("  5. delete last")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        n = int(input("Enter your value: "))
        l.insert_first(n)
    elif ch == 2:
        l.traverse()
    elif ch == 3:
        n = int(input("Enter your value: "))
        l.insert_last(n)
    elif ch == 4:
        l.delete_first()
    elif ch == 5:
        l.delete_last()