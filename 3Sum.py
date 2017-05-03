import time
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        leng = len(nums)
        if leng < 3:
            return []
        else:
            answer = []
            nums = sorted(nums)
            for i in xrange(leng-2):
                if ((i == 0) | (nums[i] != nums[i-1])) & (nums[i] <= 0):
                    j = i+1
                    k = leng-1
                    th = 0
                    while j < k:
                        x = nums[j] + nums[k] + nums[i]
                        if  x == 0:
                            answer.append([nums[i],nums[j], nums[k]]) 
                            j += 1
                            while (j < k) & (nums[j] == nums[j-1]):
                                j += 1
                            k -= 1
                            while (j < k) & (nums[k] == nums[k+1]):
                                k -= 1
                        elif x < 0:
                            j += 1
                        else:
                            k -= 1
            return answer
    
start = time.time()
a = Solution()
print a.threeSum([5,4,3,2,1,-3])
print a.threeSum([0,0,0,0])
print a.threeSum([-1, 0, 1, 2, -1, -4])
print a.threeSum([-1, 2, 1, 2, -1, -4])
a.threeSum(range(2000,-1000,-1) + range(-1000,1000))
print a.threeSum([1,2,0,3,-6,-4,5,-7,3,3,4,4,2,43,3,43,4,5,5,3,2,4,5456,45,765,867,7,54,42,45,436,57,7,67,74,4543,567,68,677,643,3456,57,5,464,23,5,])
print time.time()-start