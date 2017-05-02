class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        a = sorted(nums)[::-1]
        answer = []
        for i in nums:
            answer.append(str(a.index(i)+1))
        answer[answer.index('1')] = 'Gold Medal'
        if len(answer) > 1:
            answer[answer.index('2')] = 'Silver Medal'
        if len(answer) > 2:
            answer[answer.index('3')] = 'Bronze Medal'
        return answer

a = Solution()
print a.findRelativeRanks([5,4,3,2,1])
print a.findRelativeRanks([23,345,567,245,6574,24,53,25,35,66,4])
print a.findRelativeRanks([1])
print a.findRelativeRanks([1,2])