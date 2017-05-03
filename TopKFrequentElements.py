from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        b = Counter(nums)
        T=[]
        answer = []
        for i in b.keys():
            T.append([-b[i],i])
        T = sorted(T)
        for i in T[:k]:
            answer.append(i[1])
        return answer

a = Solution()
print a.topKFrequent([1,1,1,2,2,3],2)
print a.topKFrequent([1,1,1,2,2,2,3,3,3],2)
print a.topKFrequent([0,0,0,2],2)

class SolutionX(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numdict = {}
        T = []
        answer = []
        for i in nums:
            try:
                numdict[i] += 1
            except:
                numdict[i] = 0
        for i in numdict.keys():
            T.append([-numdict[i],i])
        T = sorted(T)
        for i in T[:k]:
            answer.append(i[1])
        return answer