class Solution(object):

	def merge(self, intervals):
		'''
		:type intervals: List[List[int]]
		:rtype List[List[int]]
		'''
		sortl = sorted(intervals)
		maxn = sortl[0][1]
		minn = sortl[0][0]
		result = []

		for item in sortl[1:]:
			if(item[0]>=minn and item[0]<=maxn):

				maxn = max(maxn, item[1])

			elif(item[0]<minn ):
				minn = item[0]
				maxn = max(maxn, item[1])
			else:
				newlist = [minn, maxn]
				minn = item[0]
				maxn = item[1]
				result.append(newlist)
			
		result.append([minn, maxn])
		return result


l = [[2,3],[4,5],[6,7],[8,9],[1,10]]
#sortl = sorted(l)
#print(l)
s =  Solution();
re = s.merge(l)
print(re)