lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
a, b = int(input()), int(input())

lst2 += lst1[a-1:b][::-1]
del lst1[a-1:b]

print(lst1)
print(lst2)
