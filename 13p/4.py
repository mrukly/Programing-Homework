set1 = set(input().split())
set2 = set(input().split())

x = input().strip()   

if x in (set1 & set2):
    print("Yes")
else:
    print("No")
