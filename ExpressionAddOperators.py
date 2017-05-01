class Solution(object):
    def myasser(self, target,index,rl, prl, num, pronum):
        if prl[0] == '+':
            newtarget = target - pronum
        elif prl[0] == '-':
            if rl == '':
                return 0
            else:
                newtarget = target + pronum
        rl += prl
        if (newtarget == 0) & (len(num) == index):
            self.solution.append(rl[1:])
        else:
            self.addOperators(num[index:], newtarget, rl = rl)
    def Times(self, num, temp, rl, target, tempstr):
        if len(num):su
            for k in range(1, (len(num) - 1) * (num[:1] != '0') + 2):
                tempx = temp * int(num[:k])
                tempstrx = tempstr + '*' + num[:k]
                self.myasser(target, k, rl, '+'+tempstrx, num, pronum = tempx)
                self.myasser(target, k, rl, '-'+tempstrx, num, pronum = tempx)
                self.Times(num[k:], tempx, rl, target, tempstrx)
    def addOperators(self, num, target, rl = '', x = 1):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if rl == '':
            self.solution = []
        for sl in range(1, (len(num) - 1) * (num[:1] != '0') + 2):
            tempstr = str(num[:sl])
            self.myasser(target, sl, rl, '+'+tempstr,num,pronum = int(num[:sl]))
            self.myasser(target, sl, rl, '-'+tempstr,num,pronum = int(num[:sl]))
            self.Times(num[sl:], int(num[:sl]), rl, target, tempstr)
        return self.solution

a = Solution()
x = a.addOperators("3456237490", 9191)
print x
x = a.addOperators("123", 6)
print x
x = a.addOperators("105", 5)
print x
x = a.addOperators("00", 0)
print x
x = a.addOperators("232", 8)
print x
x = a.addOperators("13222", 25)
print x
x = a.addOperators("123456789", 45)
print x