class Solution(object):
    def sumAndMultiply(self, n):
        sum = 0
        n = int(n)
        new = 0
        i =1
        while n > 0:
            if n%10 != 0:

                sum += n%10
                new += (n%10) * i
                i = i *10
            n = n//10

        return sum * new