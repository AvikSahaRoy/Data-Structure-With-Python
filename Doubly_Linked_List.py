class Node:
    def __init__(self, item):
        self.prev = None
        self.info = item
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None

    # Insert first ------------------>>>
    def insert_begining(self, item):
        n = Node(item)
        if self.start == None:
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n
        print(f"{n.info} is inserted at the begining")

    # Insert last ------------------>>>
    def insert_last(self, item):
        n = Node(item)
        if self.start == None:
            self.start = n
        else:
            t = self.start
            while(t.next != None):
                t = t.next
            t.next = n
            n.prev = t
        print(f"{n.info} is inserted at the last")

    # Delete first ------------------>>>
    def delete_first(self):
        n = self.start
        if self.start == None:
            print("Linked list is empty")
            return
        else:
            self.start = self.start.next
            print(f"{n.info} deleted Successfully at the begining")

    # Delete last ------------------>>>
    def delete_last(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty")
            return
        elif t.next == None:
            self.start = None
            print(f"{t.info} item deleted Successfully at the Last")
        else:
            while(t.next != None):
                t = t.next
            g = t.prev
            g.next = None
            print(f"{t.info} item deleted Successfully at the Last")

    # Display list ------------------>>>
    def traverse(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty")
        else:
            print("List is: ")
            while(t != None):
                print(t.info, end=' ')
                t = t.next

    # Reverse list ------------------>>>
    def reverse(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty")
            return
        else:
            print("Reverse List is: ")
            while(t.next != None):
                t = t.next
            while(t != None):
                print(t.info, end=" ")
                t = t.prev


l = DoublyLinkedList()
while(True):
    print("\n<<-------- Doubly Linked List operations -------->>\n")
    print("  1. Insert at Begining")
    print("  2. Insert at Last")
    print("  3. Delete at Begining")
    print("  4. Delete at Last")
    print("  5. Display")
    print("  6. Reverse\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        n = int(input("Enter your value: "))
        l.insert_begining(n)
    elif ch  == 2:
        n = int(input("Enter your value: "))
        l.insert_last(n)
    elif ch == 3:
        l.delete_first()
    elif ch == 4:
        l.delete_last()
    elif ch == 5:
        l.traverse()
    elif ch == 6:
        l.reverse()

