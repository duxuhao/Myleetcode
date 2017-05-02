class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(bin(n)[2:]).count('1')
        
a = Solution()
print a.hammingWeight(4)
print a.hammingWeight(40)
print a.hammingWeight(11)
print a.hammingWeight(2 ** 64)