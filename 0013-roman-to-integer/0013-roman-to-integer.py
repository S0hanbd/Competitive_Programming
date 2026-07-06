class Solution(object):
    def romanToInt(self,s):
        s = s.upper()

        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        finalValue = 0

        for i in range(len(s)):
            if i < len(s) - 1 and value[s[i]] < value[s[i + 1]]:
                finalValue -= value[s[i]]
            else:
                finalValue += value[s[i]]

        return finalValue
        