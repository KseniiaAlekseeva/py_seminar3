nums = [1, 2, 1, 1, 4, 3, 1, 1, 5, 3]
print(len(set(nums)))  # uniq els

result = []
count = 0
for i in set(nums):
    if nums.count(i) == 1:
        result.append(i)
print(result, len(result))  # numbers which one time

result1 = [i for i in set(nums) if nums.count(i) == 1]
print(result1, len(result1))
