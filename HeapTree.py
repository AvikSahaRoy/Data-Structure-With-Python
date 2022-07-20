# # Input  -->> L = [10, 20, 30, 40, 15, 21, 25]
# # Output -->> L = [40, 20, 30, 10, 15, 21, 25]
# <<<--------------- Max Heap ------------------->>>

# def Heapify(L, i):
#     l = left(i)
#     r = right(i)
#     largest = i

#     if l < len(L) and L[l] > L[largest]:
#         largest = l

#     if r < len(L) and L[r] > L[largest]:
#         largest = r

#     if largest != i:
#         L[largest], L[i] = L[i], L[largest]
#         Heapify(L, largest)

# def left(i):
#     return 2 * i + 1
# def right(i):
#     return 2 * i + 2

# def Max_Heap(L):
#     n = len(L) // 2
#     for i in range(n, -1, -1):
#         Heapify(L, i)

# L = [10, 20, 30, 40, 15, 21, 25]
# Max_Heap(L)
# print("List is: ", L)


# -------------------------------------------------

# Input  -->> L = [10, 20, 30, 40, 15, 21, 25]
# Output -->> L = [40, 20, 30, 10, 15, 21, 25]

def Heapify(L, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and L[l] > L[largest]:
        largest = l

    if r < n and L[r] > L[largest]:
        largest = r

    if largest != i:
        L[largest], L[i] = L[i], L[largest]
        Heapify(L, n, largest)

def Heap_Sort(L):
    n = len(L)
    for i in range(n // 2 -1, -1, -1):
        Heapify(L, n, i)

    for i in range(n-1, 0, -1):
        L[i], L[0] = L[0], L[i]  
        Heapify(L, i, 0)

L = [ 11, 12, 5, 13, 6, 7, 1]
print("Original Array:  ", L)
Heap_Sort(L)
print("Sorted Array is: ", L)
