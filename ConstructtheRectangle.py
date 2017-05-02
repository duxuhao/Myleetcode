import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        tempanswer = [[area - 1, [area,1]]]
        for i in range(2, int(math.sqrt(area))+1):
            if area % i == 0:
                tempanswer.append([area/i-i, [area/i,i]])
        return sorted(tempanswer)[0][1]
        
a = Solution()
print a.constructRectangle(4)
print a.constructRectangle(1000)
print a.constructRectangle(9999)
print a.constructRectangle(4343434)
print a.constructRectangle(5345483729)
print a.constructRectangle(34)
print a.constructRectangle(99)
print a.constructRectangle(0)