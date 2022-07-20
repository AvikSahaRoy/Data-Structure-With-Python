class Node:
    def __init__(self, item):
        self.info = item
        self.link = None

class Linkedlist:
    def __init__(self):
        self.start = None
    # ----------- Insert Start -------------

    # Insert at begining -------------------
    def insert_at_begining(self, item):
        n = Node(item)
        n.link = self.start
        self.start = n
        print(f"{n.info} is inserted at the begining")
        
    # Insert at last ------------------->>
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

    # Insert at specific position -------------------
    def insert_specific_pos(self, item, pos):
        if self.start == None:
            print("Linked list is empty please insert some value first")
        else:
            n = Node(item)
            t = self.start
            p = 1

            while(t.link != None) and (p < pos-1):
                t = t.link
                p += 1
            if pos == 0:
                print("Position must be grater than 1")
                return
            if pos-1 == p+1:
                print("Sorry, Can't Insert At This Position")
                return

            n.link = t.link
            t.link = n

            if pos > p and pos != p-1:
                print(f"{pos} position not found so {item} inserted at the end")
            else:
                print(f"{n.info} inserted Successfully at the position {pos}")

    # Insert Afteritem -------------------
    def insert_afteritem(self, item, afteritem):
        n = Node(item)
        t = self.start
        if self.start == None:
            print("Linked list is empty please insert some value first")
            return

        while (afteritem != t.info) and (t.link != None):
            t = t.link
        
        n.link = t.link
        t.link = n
        if (t.info != afteritem):
            print(f"After item {afteritem} item not found so inserted at the end")
        else:
            print(f"{n.info} inserted Successfully after {afteritem}")
            
    
    # ------------ Insert End --------------

    # ------------ Delete Start --------------

    # Delete Start --------------
    def delete_Start(self):
        if self.start == None:
            print("Linked list is empty please insert some value first")
        else:
            n = self.start
            self.start = self.start.link
            print(f"{n.info} deleted Successfully at the begining")

    # Delete last --------------
    def delete_last(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty please insert some value first")
        elif t.link == None:
            self.start = None
            print(f"{t.info} item deleted Successfully at the Last")
        else:
            while(t.link != None):
                prev = t 
                t = t.link 
            print(f"{t.info} item deleted Successfully at the last")
            prev.link = None

    # Delete specified position --------------
    def delete_specified_pos(self, pos):
        if self.start == None:
            print("Linked list is empty please insert some value first")
            return
        if pos == 0:
            self.start = self.start.link
            print(f"Item deleted Successfully at the position {pos}")
            return 
        else:
            index = 0
            current = self.start
            prev = self.start
            temp = self.start
            f = 0
            while(current != None):
                if index == pos:
                    temp = current.link
                    f = 1
                    break
                prev = current
                current = current.link
                index += 1
            if f == 0:
                print("Sorry, Position Out of Range")
                return
            prev.link = temp
            print(f"Item deleted Successfully at the position {pos}")
            return prev

    # Delete particular item --------------
    def delete_particular_node(self, item):
        if self.start == None:
            print("Linked list is empty please insert some value first")
        else:
            t = self.start
            if (t != None):
                if (t.info == item):
                    self.start = t.link
                    t = None
                    print(f"{item} item deleted Successfully")
                    return
            while(t != None):
                if t.info == item:
                    break
                prev = t
                t = t.link
            if(t == None):
                print("Item not found")
                return
            prev.link = t.link
            t = None
            print(f"{item} item deleted Successfully")

    # --------------- Delete End ------------------

    # ------------- Display List -------------------
    def traverse(self):
        t = self.start
        if self.start == None:
            print("Linked list is empty")
        else:
            print("List is: ")
            while(t != None):
                print(t.info, end=' ')
                t = t.link

    # ------------ Reverse list --------------------
    def Reverse(self):
        node = self.start
        values = []
        if self.start == None:
            print("Linked list is empty")
            return
        while node:
            values.append(node.info)
            node = node.link

        print("Reverse list is: ")
        for value in reversed(values):
            print(value, end=" ")

    # ----------- Search element -------------------
    def Search(self, item):
        t = self.start
        if t == None:
            print("There is no Node")
            return
        elif t.info == item:
            print("Element is present in the list at the position : 0")
            return
        else:
            i = 0
            flag = 0
            while(t.link != None):
                i += 1
                t = t.link
                if t.info == item:
                    flag = 1
                    break
            if(flag == 1):  
                print("Element is present in the list at the position : " + str(i))
            else:  
                print("Element is not present in the list");  

    # --------------- Node Count -------------
    def nodeCount(self):
        t = self.start
        count = 0
        while(t):
            count += 1
            t = t.link
        print(count, "Node present in the list")

l = Linkedlist()
while(True):
    print("\n<<-------- Single Linked List operations -------->>\n")
    print("  <<--- Insertion --->>")
    print("  1. Insert at Begining")
    print("  2. Insert at Last")
    print("  3. Insert at Specific Position")
    print("  4. Insert After Specific Item\n")
    print("  <<--- Deletion --->>")
    print("  5. Delete at Begining")
    print("  6. Delete at Last")
    print("  7. Delete by Position")
    print("  8. Delete by Item\n")
    print("  <<--- Traversion --->>")
    print("   9. Traverse")
    print("  10. Reverse the list")
    print("  11. Search Any Item")
    print("  12. Node Count")
    print("  13. Exit\n")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        n = int(input("Enter your value: "))
        l.insert_at_begining(n)
    elif ch == 2:
        item = int(input("Enter your value: "))
        l.insert_at_last(item)
    elif ch == 3:
        item = int(input("Enter your value: "))
        pos = int(input("Enter the position you want to insert: "))
        l.insert_specific_pos(item, pos)
    elif ch == 4:
        item = int(input("Enter your value: "))
        afteritem = int(input("After which item you want to input: "))
        l.insert_afteritem(item, afteritem)
    elif ch == 5:
        l.delete_Start()
    elif ch == 6:
        l.delete_last()
    elif ch == 7:
        pos = int(input("Enter the position you want to delete: "))
        l.delete_specified_pos(pos)
    elif ch == 8:
        item = int(input("Enter your value you want to delete: "))
        l.delete_particular_node(item)
    elif ch == 9:
        l.traverse()
    elif ch == 10:
        l.Reverse()
    elif ch == 11:
        item = int(input("Enter the item you want to Search: "))
        l.Search(item)
    elif ch == 12:
        l.nodeCount()
    elif ch == 13:
        break
    else:
        print("Invalid Input")