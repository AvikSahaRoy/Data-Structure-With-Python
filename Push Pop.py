# class Stack:
#     def __init__(self, m):
#         self.list = []
#         self.max = m
#         self.top = -1
#     def Push(self):
#         if self.top == self.max - 1:
#             print('Stack is full')
#             return
#         else:
#             item = int(input("Enter a value: "))
#             self.top += 1
#             self.list.append(item)
#             print("Value Inserted")
#     def Pop(self):
#         if self.top == -1:
#             print("Stack is empty")
#             return
#         else:
#             self.list.pop(self.top)
#             self.top -= 1
#             print("Item Deleted")
#     def Display(self):
#         if self.list == []:
#             print("Stack is empty")
#         else:
#             print("Stack is:",self.list)

# n = int(input("Enter the stack size: "))
# st = Stack(n)
# while(True):
#     print("\nEnter 1 for push")
#     print("Enter 2 for pop")
#     print("Enter 3 for display")
#     print("Enter 4 for exit")
#     ch = int(input("Enter your Choice: "))
#     if ch == 1:
#         st.Push()
#     if ch == 2:
#         st.Pop()
#     if ch == 3:
#         st.Display()
#     if ch == 4:
#         break





class Stack:
    def __init__(self, m):
        self.list = []
        self.max = m
        self.top = -1
    def Push(self):
        if self.top == self.max - 1:
            print('Stack is full')
            return
        else:
            item = int(input("Enter a value: "))
            self.top += 1
            self.list.append(item)
            print("Value Inserted")
    def Pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            self.list.pop(self.top)
            self.top -= 1
            print("Item Deleted")
    def Display(self):
        if self.list == []:
            print("Stack is empty")
        else:
            print("Stack is:",self.list)
    def Postfix(self):
        p = input("Enter the number: ")
        l = []
        d = p.split(",")
        for i in range(len(d)):
            if d[i] not in ['+', '-', '*', '/']:
                l.append(int(d[i]))
                # print(l)
            else:
                a = l.pop(l.index(l[-1]))
                b = l.pop(l.index(l[-1]))

                if d[i] == "+":
                    sum = b + a
                    l.append(sum)
                    # print(l)
                    
                elif d[i] == "-":
                    sum = b - a
                    l.append(sum)
                    # print(l)
                elif d[i] == "*":
                    sum = b * a
                    l.append(sum)
                    # print(l)
                elif d[i] == "/":
                    sum = b / a
                    l.append(sum)
                    # print(l)
        print("Postfix is: ",int(l[0]))

n = int(input("Enter the stack size: "))
st = Stack(n)
while(True):
    print("\nEnter 1 for push")
    print("Enter 2 for pop")
    print("Enter 3 for display")
    print("Enter 4 for postfix")
    print("Enter 5 for exit")
    ch = int(input("Enter your Choice: "))
    if ch == 1:
        st.Push()
    if ch == 2:
        st.Pop()
    if ch == 3:
        st.Display()
    if ch == 4:
        st.Postfix()
    if ch == 5:
        break