import time

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        leng = len(nums)
        if leng < 3:
            pass
        else:
            nums = sorted(nums)
            for i in xrange(leng-2):
                for j in xrange(i+1, leng-1):
                    x = -nums[i] - nums[j]
                    if (x in nums[j+1:]):
                        y = [nums[i],nums[j], x]
                        if y not in answer:
                            answer.append(y)
        return answer
    
start = time.time()
a = Solution()
print a.threeSum([5,4,3,2,1,-3])
print a.threeSum([-1, 0, 1, 2, -1, -4])
print a.threeSum([-1, 2, 1, 2, -1, -4])
print a.threeSum([1,2,0,3,-6,-4,5,-7,3,3,4,4,2,43,3,43,4,5,5,3,2,4,5456,45,765,867,7,54,42,45,436,57,7,67,74,4543,567,68,677,643,3456,57,5,464,23,5,])
print time.time() - start