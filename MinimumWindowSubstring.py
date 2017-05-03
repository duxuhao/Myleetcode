import time
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        scopy = list(s)
        a = []
        if (t == "") | (len(s)<len(t)):
            return ""
        try:
            num1 = Counter(t)
            for i in set(t):
                for j in range(num1[i]):
                    ind = scopy.index(i)
                    a.append([ind,i])
                    scopy[ind] = ' '
        except ValueError:
            return ""
        k = len(t)
        start = sorted(a)[0][0]
        end
        while k < len(s):
            for i in range(start, len(s) - k + 1):
                num2 = Counter(s[i:i+k])
                n = 0
                try:
                    for j in num1.keys():
                        if num1[j] <= num2[j]:
                            n += 1
                    if n == len(num1.keys()):
                        return s[i:i+k]
                except ValueError:
                    pass
            k += 1
        return ""
                        
    
start = time.time()    
a = Solution()
print a.minWindow("cabwefgewcwaefgcf","cae")

print a.minWindow("bdab","ab")
print a.minWindow("a","aa")
print a.minWindow("bba","ab")

print a.minWindow("SDFJHSGFKHEFBDBCMSH","SDSDFF")

print a.minWindow("SDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSH","SDFJSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDEKUHSKUGNDVXMVXVXJHFKRDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHHSGFKHEFBSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHDBCMSH")

print a.minWindow("RETRIUSEOFHJBVNMCNERGDAS","DAFG")
print a.minWindow("FHJDAHJBVNFHEDSJBHVJFSH","IRU")
print a.minWindow("EIURYUWORYFGFHCZSBVCN","HIOS")
print a.minWindow("ERTHRAFHSBVXNC","VC")
print a.minWindow("ADOBECODEBANC","AB")
print time.time()-start


import sys
class SolutionX(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        required, min_len = [0] * 128, sys.maxint
        # record numbers of each character in t
        for ch in t:
            required[ord(ch)] += 1
        left = right = min_start = 0
        # count: number of characters that are still required
        count = len(required) - required.count(0)
        while right < len(s):
            while count > 0 and right < len(s):
                # move right till s[left : right] has all characters in t
                required[ord(s[right])] -= 1
                if required[ord(s[right])] == 0:
                    count -= 1
                right += 1
            # s[left : right] has all characters in t, move left pointer
            while count == 0:
                required[ord(s[left])] += 1
                if required[ord(s[left])] == 1:
                    # now s[left : right] misses one character, update min_len if necessary
                    count = 1
                    if right - left < min_len:
                        min_len, min_start = right - left, left
                left += 1

        return s[min_start : min_start+min_len] if min_len != sys.maxint else ''
    
start = time.time()    
a = SolutionX()
print a.minWindow("cabwefgewcwaefgcf","cae")

print a.minWindow("bdab","ab")
print a.minWindow("a","aa")
print a.minWindow("bba","ab")

print a.minWindow("SDFJHSGFKHEFBDBCMSH","SDSDFF")

print a.minWindow("SDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSH","SDFJSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDEKUHSKUGNDVXMVXVXJHFKRDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHHSGFKHEFBSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHDBCMSH")

print a.minWindow("RETRIUSEOFHJBVNMCNERGDAS","DAFG")
print a.minWindow("FHJDAHJBVNFHEDSJBHVJFSH","IRU")
print a.minWindow("EIURYUWORYFGFHCZSBVCN","HIOS")
print a.minWindow("ERTHRAFHSBVXNC","VC")
print a.minWindow("ADOBECODEBANC","AB")
print time.time()-start

class SolutionY(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        scopy = list(s)
        a = []
        if (t == "") | (len(s)<len(t)):
            return ""
        try:
            num = Counter(t)
            for i in set(t):
                for j in range(num[i]):
                    ind = scopy.index(i)
                    a.append([ind,i])
                    scopy[ind] = ' '
        except ValueError:
            return ""
        a = sorted(a)
        Distance = [a[-1][0]-a[0][0],a[0][0],a[-1][0]]
        while 1:
            try:
                a[0][0] = scopy.index(a[0][1])
                scopy[a[0][0]] = ' '
                a = sorted(a)
                d = a[-1][0]-a[0][0]
                if d < Distance[0]:
                    Distance = [d,a[0][0],a[-1][0]]
            except ValueError:
                return s[Distance[1]:Distance[2]+1]
            
start = time.time()    
a = SolutionY()
print a.minWindow("cabwefgewcwaefgcf","cae")

print a.minWindow("bdab","ab")
print a.minWindow("a","aa")
print a.minWindow("bba","ab")

print a.minWindow("SDFJHSGFKHEFBDBCMSH","SDSDFF")

print a.minWindow("SDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSH","SDFJSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHFHAFGKAHFVCZfshbksgnbsFBDBCMSHSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDEKUHSKUGNDVXMVXVXJHFKRDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHHSGFKHEFBSDFJHSGFKHEvdjhfskhfsfjkhdvncxzsirjhfgdhiehfskgsndnskhfskigsjvnvxnvsfheighjvsbvxbvdrkhgdkdsjfehfnvxfjSKDHFJBJVCSEUIDJSNVJXFSEKUHSKUGNDVXMVXVXJHFKRDGSCBMCFUEHSKGBSBVZVMXCSGHKDGNIDbfskdfsfnvbshesfhdFBSKFVSGJOTUIORFCZCZKFHAFGKAHFVCZfshbksgnbsFBDBCMSHDBCMSH")

print a.minWindow("RETRIUSEOFHJBVNMCNERGDAS","DAFG")
print a.minWindow("FHJDAHJBVNFHEDSJBHVJFSH","IRU")
print a.minWindow("EIURYUWORYFGFHCZSBVCN","HIOS")
print a.minWindow("ERTHRAFHSBVXNC","VC")
print a.minWindow("ADOBECODEBANC","AB")
print time.time()-start