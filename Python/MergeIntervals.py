class Solution(object):

	def merge(self, intervals):
		'''
		:type intervals: List[List[int]]
		:rtype List[List[int]]
		'''
		if(len(intervals)<=1):
			return intervals
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

	def merge2(self, intervals):
		intervals.sort(key=lambda x: x.start)

		merged = []

		for interval in intervals:
			# if the list of merged intervals is empty or if the current
			# interval does not overlap with the previous, simply append it
			if not merged or merged[-1].end < interval.start:
				merged.append(interval)
			else:
				# otherwise, there is overlap, so we merge the current and previous
				# intervals
				merged[-1].end = max(merged[-1].end, interval.end)
		return merged




l = [[2,3],[4,5],[6,7],[8,9],[1,10]]
#sortl = sorted(l)
#print(l)
s =  Solution();
re = s.merge2(l)
print(re)