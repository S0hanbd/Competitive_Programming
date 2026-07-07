class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = []
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i-1]:
                return False
        return True

        