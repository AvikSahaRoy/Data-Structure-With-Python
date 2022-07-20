# number = [1,5,6,9,0]
# for i in range(len(number)):
#   for j in range(i+1, len(number)):
#     if number[i] > number[j]:
#       number[i], number[j] = number[j], number[i]
# print(number)


T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']
c = 0
for i in range(T):
    N = int(input())
    S = input()
    for j in range(N):
        if S[j] in vowel:
            c += 1 
    if N-c >= 4:
        print("NO")
    else:
        print("YES")