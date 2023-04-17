nums = [1, 2, 3, 4, 5, 6, 7]

sdvig = int(input("Enter k: ")) % len(nums)

# for _ in range(sdvig):
#     nums.insert(0, nums.pop(len(nums)-1))
# print(nums)

nums = nums[-sdvig:]+nums[:-sdvig]
print(nums)
