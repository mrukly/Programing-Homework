cities = input().split()

winner = None

for i in range(1, len(cities)):
    if cities[i][0].lower() != cities[i-1][-1].lower():
        if i % 2 == 1:  
            winner = "Петя"
        else:           
            winner = "Вася"
        break

if winner is None:
    if (len(cities) - 1) % 2 == 0:
        winner = "Петя"
    else:
        winner = "Вася"

print(winner)
