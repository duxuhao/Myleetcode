class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >= 0:
            y = int(str(abs(x))[::-1])
        else:
            y = -int(str(abs(x))[::-1])
        if abs(y) > 2147483647:
            return 0
        else:
            return y
        
        
a = Solution()
print a.reverse(1534236469)
print a.reverse(-123)
print a.reverse(0)
print a.reverse(2147483648)