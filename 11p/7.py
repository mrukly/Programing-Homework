nums = list(map(int, input().split()))

even = 0
odd = 0

for i in nums:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(even, odd)
