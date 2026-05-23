sweet = set(input().split())

n = int(input())

friends = set()

for i in range(n):
    friends |= set(input().split())   

only = sweet - friends

print(len(only))
