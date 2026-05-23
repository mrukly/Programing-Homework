lst = list(map(int, input().split()))
action = input()

direction = action[0]
n = int(action[1:])

if direction == 'R':        
    lst = lst[-n:] + lst[:-n]
elif direction == 'L':    
    lst = lst[n:] + lst[:n]

print(lst)
