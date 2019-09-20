
def twosum(nums, target):

	for i in range(0, len(nums)):

		for j in range(0, len(nums)):

			if(nums[i]+nums[j]==target):
			
				return [i,j]






nums = [2,7,11,15]
target = 9

result = twosum(nums, target)
e = enumerate(nums)

print(list(e))

