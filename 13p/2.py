n = int(input())                     
courses = set(input().split())        

for i in range(n - 1):               
    courses &= set(input().split())  

print(len(courses))                   
