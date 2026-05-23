numbers = list(map(int, input().split()))
x = int(input())

nums = set()
repeating = set()

for n in numbers:
    if n in nums:
        repeating.add(n)
    else:
        nums.add(n)

print("Yes" if x in repeating else "No")
