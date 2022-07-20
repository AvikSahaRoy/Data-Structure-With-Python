class Array1:
    def __init__(self):
        self.list = []

    def CreatArray(self):
        self.max = int(input("Enter the size of the list: "))
        for i in range(self.max):
            self.list.append(int(input("Enter the {} value: ".format(i))))
        print("List is created")

    def ShowArray(self):
        if self.list == []:
            print("No list is created")
        else:
            print("List is: ", self.list)

    def LinearSearch(self):
        if self.list == []:
            print("No list is created")
        else:
            item = int(input("Enter the value you want to searh: "))
            if item in self.list:
                print('Search value index is: ',self.list.index(item))

    def Sorting(self):
        if self.list == []:
            print("No list is created")
        else:
            for i in range(self.max):
                for j in range(i+1, self.max):
                    if self.list[i] > self.list[j]:
                        self.list[i], self.list[j] = self.list[j], self.list[i]
            print("Sorted list is: ",self.list)

    def BinarySearch(self):
        if self.list == []:
            print("No list is created")
        else:
            item1 = int(input("Enter the value you want to searh for sorted list: "))
            l = 0
            h = self.max
            m = 0
            while(l<=h):
                m = (h+l) // 2
                if self.list[m] < item1:
                    l = m+1
                elif self.list[m] > item1:
                    h = m-1
                else:
                    print('Search Sorted value index is:',m)
                    break

obj = Array1()
if __name__ == "__main__":
    while(True):
        print("\n----- Data Structure operations on array -----")
        print("1. Create Array")
        print("2. Show Array")
        print("3. Linear Search")
        print("4. Sort Array")
        print("5. Binary Search")
        print("6. Exit\n")
        ch = int(input("Enter your Choice: "))
        if ch == 1:
            obj.CreatArray()
        if ch == 2:
            obj.ShowArray()
        if ch == 3:
            obj.LinearSearch() 
        if ch == 4:
            obj.Sorting()   
        if ch == 5:
            obj.BinarySearch()
        if ch == 6:
            break