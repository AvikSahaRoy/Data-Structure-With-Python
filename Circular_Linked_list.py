class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class CircularLinkedlist:
    def __init__(self):
        self.start = None
        
    # Insert at begining -----------------
    def insert_begining(self, item):
        n = Node(item)
        t = self.start
        if self.start == None:
            self.start = n
            self.start.link = self.start
        else:
            while t.link != self.start:
                t = t.link
            t.link = n 
            n.link = self.start
            self.start = n
        print(f"{item} is inserted at the begining")

    # Insert at last -------------------
    def insert_last(self, item):
        n = Node(item)
        t = self.start
        if self.start == None:
            self.start = n
            self.start.link = self.start
        else:
            while(t.link != self.start):
                t = t.link
            t.link = n
            n.link = self.start
        print(f"{n.info} is inserted at the last")

    # Delete at start -------------------
    def delete_start(self):
        t = self.start
        n = self.start
        if self.start == None:
            print("list is empty")
        elif self.start.link == self.start:
            self.start = None
            print(f"{n.info} deleted Successfully at the begining")
        else:
            while t.link != self.start:
                t = t.link
            self.start = self.start.link
            t.link = self.start           
            print(f"{n.info} deleted Successfully at the begining")

    # Delete at end -------------------
    def delete_last(self):
        t = self.start
        if self.start == None:
            print("list is empty")
        elif t.link == self.start:
            self.start = None
            print(f"{t.info} item deleted Successfully at the Last")
        else:
            while(t.link != self.start):
                prev = t
                t = t.link 
            print(f"{t.info} item deleted Successfully at the last")
            prev.link = t.link

    # Display List -------------------
    def Traverse(self):
        t = self.start
        if self.start == None:
            print("List is empty")
            return
        else:
            print("List is: ")
            while(t != None):
                print(t.info, end=" ")
                t = t.link
                if (t == self.start):
                    break

    # Reverse list --------------------
    def Reverse(self):
        t = self.start
        l = []
        top = -1
        if t == None:
            print("List is empty")
            return
        while(t.link != self.start):
            l.append(t.info)
            t = t.link
            top += 1
        l.append(t.info)
        top += 1
        print("Reverse list is: ")
        while top != -1:
            g = l.pop(top)
            print(g, end=' ')
            top-=1

l = CircularLinkedlist()
while(True):
    print("\n<<-------- Circular Linked List operations -------->>\n")
    print("  <<--- Insertion --->>")
    print("  1. Insert at Begining")
    print("  2. Insert at Last\n")

    print("  <<--- Deletion --->>")
    print("  3. Delete at Begining")
    print("  4. Delete at Last\n")

    print("  <<--- Traversion --->>")
    print("  5. Traverse")
    print("  6. Revarse")
    print("  7. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        n = int(input("Enter your value: "))
        l.insert_begining(n)

    elif ch == 2:
        n = int(input("Enter your value: "))
        l.insert_last(n)

    elif ch == 3:
        l.delete_start()

    elif ch == 4:
        l.delete_last()

    elif ch == 5:
        l.Traverse()

    elif ch == 6:
        l.Reverse()

    elif ch == 7:
        break
    else:
        print("Invalid Input")




# ----------------------------------------------------

# class Node:
#     def __init__(self, item):
#         self.info = item
#         # self.link = None

# class CircularLinkedlist:
#     def __init__(self, item):
#         n = Node(item)
#         self.start = n
#         self.start.link = self.start
#         # self.start = None
#         # self.start.link = self.start

#     # Insert at begining -----------------
#     def insert_begining(self, item):
#         n = Node(item)
#         t = self.start
#         while t.link != self.start:
#             t = t.link
#         t.link = n 
#         n.link = self.start
#         self.start = n
#         print(f"{item} is inserted at the begining")

#     # Insert at last -------------------
#     def insert_last(self, item):
#         n = Node(item)
#         t = self.start
#         while t.link != self.start:
#             t = t.link
#         t.link = n
#         n.link = self.start
#         print(f"{item} is inserted at the last")

#     # Delete at start -------------------
#     # def delete_start(self):
#     #     t = self.start
#     #     # self.start.link = t.link
#     #     while t.link != self.start:
#     #         self.start = self.start.link
#     #         self.start.link = self.start


#     # Display List -------------------
#     def Traverse(self):
#         t = self.start
#         print("List is: ")
#         while(True):
#             print(t.info, end=" ")
#             t = t.link
#             if (t == self.start):
#                 break

# n = int(input("Enter a value first: "))
# l = CircularLinkedlist(n)
# while(True):
#     print("\n<<-------- Circular Linked List operations -------->>\n")
#     print("  <<--- Insertion --->>")
#     print("  1. Insert at Begining")
#     print("  2. Insert at Last\n")

#     print("  <<--- Deletion --->>")
#     print("  3. Delete at Begining")
#     print("  4. Delete at Last\n")

#     print("  <<--- Traversion --->>")
#     print("  5. Traverse")
#     print("  6. Revarse")
#     print("  7. Exit\n")

#     ch = int(input("Enter your Choice: "))
#     if ch == 1:
#         n = int(input("Enter your value: "))
#         l.insert_begining(n)

#     elif ch == 2:
#         n = int(input("Enter your value: "))
#         l.insert_last(n)

#     elif ch == 3:
#         l.delete_start()

#     elif ch == 5:
#         l.Traverse()

#     elif ch == 7:
#         break
#     else:
#         print("Invalid Input")

