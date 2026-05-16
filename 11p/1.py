nums = []
for i in range(10):
    nums.append(int(input()))

new = []
for i in range(9):
    new.append(nums[i] + nums[i + 1])

print(new)
