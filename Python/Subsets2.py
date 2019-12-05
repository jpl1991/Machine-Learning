class Solution(object):
	def subsetWithDup(self, nums):
		'''
		:type nums: List[int]
		:rtype List[List[int]]
		'''
		result = [[]]

		for i in range(len(nums)):

			for j in range(1, len(nums)+1):
				if(nums[:j] not in result):
					result.append(nums[:j])


			nums = nums[i:]
		if(nums not in result):
			result.append(nums)

		return result

sol = Solution()

result = sol.subsetWithDup([1,2,3])

s = [1,2,3,4]

print(result)
