import time
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) * len(nums2):
            answerindex = [[0,0]]
            answer = []
            n = 1
            overload = 1
            row = {0: 0}
            while (n < k) & overload:
                temp = []
                for i in row.keys():
                    if row[i]+1 < len(nums2):
                        temp.append([nums1[i] + nums2[row[i]+1],[i,row[i]+1]])
                if i+1 < len(nums1):
                    temp.append([nums1[i+1] + nums2[0],[i+1,0]])
                if temp == []:
                    overload = 0
                else:
                    x = sorted(temp)[0][1]
                    answerindex.append(x)
                    try:
                        row[x[0]] += 1
                    except:
                        row[x[0]] = 0
                    n += 1
            for ai in answerindex:
                answer.append([nums1[ai[0]], nums2[ai[1]]])
        else:
            answer = []
        return answer

class SolutionX(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        temp = []
        answer = []
        for i in nums1:
            for j in nums2:
                temp.append([i+j,[i,j]])
        temp = sorted(temp)
        for i in range(min([k,len(temp)])):
            answer.append(temp[i][1])
        return answer
start = time.time()
a = Solution()
print a.kSmallestPairs([1,7,11],[2,4,6], 3)
print a.kSmallestPairs([1,1,2],[1,2,3], 2)
print a.kSmallestPairs([1,2],[3], 3)
print a.kSmallestPairs([],[1], 5)
print a.kSmallestPairs(range(10000),range(10000), 100)
print time.time() - start
