class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        k = 1
        for i in xrange(len(nums)):
            if len(nums) > k:
                if nums[k] == i:
                    p = k
                    while (len(nums) > p+1) and (nums[p+1] == nums[p]):
                        p += 1
                    nums = nums[:k-1]+nums[p+1:]
                else:
                    k += 1
        return nums
a = Solution()
print a.removeDuplicates([1,1,2])
print a.removeDuplicates([1,1,2,2])
print a.removeDuplicates([1,1,2,3,4,5,5,6,6,5,4])
print a.removeDuplicates([])