nums = input()
nums = nums.split()

a = int(nums[0])
b = int(nums[1])

steps = 0

while True:
    if a == b:
        break
    if a < b:
        a += 1
        steps += 1
    elif a % 2 == 0:
        a /= 2
        steps += 1
    else:
        a += 1
        steps +=1

print(steps)
