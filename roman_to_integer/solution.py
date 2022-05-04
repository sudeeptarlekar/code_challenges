class Solution:
    map = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    def romanToInt(self, s):
        length = len(s) - 1
        sum = 0

        while length > -1:
            if length != 0 and self.map[s[length]] > self.map[s[length - 1]]:
                sum += self.map[s[length - 1] + s[length]]
                length -= 2
            else:
                sum += self.map[s[length]]
                length -= 1

        return sum

obj = Solution()
print(obj.romanToInt('III'))
print(obj.romanToInt('LIV'))
print(obj.romanToInt('MCMXCIV'))
