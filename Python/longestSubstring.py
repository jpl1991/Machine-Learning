

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s, 1):
            if value in dicts:
                sums = dicts[value] 
                if sums > start:
                    start = sums

            num = i - start 
            #print(start, num)
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        print((dicts))
        return maxlength


s = ' '

solution = Solution();

print(solution.lengthOfLongestSubstring(s))