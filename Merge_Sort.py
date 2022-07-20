 # A = [22, 38, 45, 50, 59, 75]
# B = [10, 15, 20, 28,  30, 35, 40, 48]
# C = []
# i = 0
# j = 0
# while (i<len(A) and j<len(B)):
#     if A[i] <= B[j]:
#         C.append(A[i])
#         i += 1
#     else:
#         C.append(B[j])
#         j += 1
# while(i<len(A)):
#     C.append(A[i])
#     i += 1
# while(j<len(B)):
#     C.append(B[j])
#     j += 1
# print("First list is:  ",A)
# print("Second list is: ",B)
# print("Merge list is:  ",C)

# ------------------------------------------

# A = [22, 38, 45, 50, 59, 75, 10, 15, 20, 28, 30, 35]
# C = []
# mid = (0+len(A))//2
# # print(mid)
# i = 0
# j = mid
# while (i<=mid and j<len(A)):
#     if A[i] <= A[j]:
#         C.append(A[i])
#         i += 1
#     else:
#         C.append(A[j])
#         j += 1
# while(i<mid):
#     C.append(A[i])
#     i += 1
# while(j<len(A)):
#     C.append(A[j])
#     j += 1
# print("First list is:  ",A)
# print("Merge list is:  ",C)

# ------------------------------------------

def Merge(A, f, m, l):
    C = []      # new list
    i = f       # first index
    j = m + 1   # mid point
    while (i<=m and j<=l):
        if A[i] <= A[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
    while(i<=m):
        C.append(A[i])
        i += 1
    while(j<=l):
        C.append(A[j])
        j += 1

    i = f 
    k = 0 
    while i<=l:
        A[i]=C[k]
        i+=1
        k+=1 

def Merge_Sort(List, f, l):
    if f < l:
        mid = (f+l)//2
        Merge_Sort(List, f, mid)
        Merge_Sort(List, mid+1, l)
        Merge(List, f, mid, l)
        
List = [10, 8, 30, 60, 50, 4]
print("Original Array: ", List)
# List = [22, 38, 45, 50, 59, 75, 10, 15, 20, 28, 30, 35]
f = 0
l = len(List) - 1
Merge_Sort(List, f, l)
print("Sorted array:   ",List)

