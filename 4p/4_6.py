score = input()

fteam, steam = map(int, score.split(':'))

if fteam > steam:
    print(1)  
elif steam > fteam:
    print(2) 
else:
    print(0)
