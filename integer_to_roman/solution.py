import pdb

class Solution:
    map = {
        1000: 'M',
        900:  'CM',
        500:  'D',
        400:  'CD',
        100:  'C',
        90:   'XC',
        50:   'L',
        40:   'XL',
        10:   'X',
        9:    'IX',
        5:    'V',
        4:    'IV',
        1:    'I',
    }

    def int_to_roman(self, num):
        output = ''

        for item in self.map.items():
            if num < item[0]:
                next

            count = num // item[0]
            output = output + item[1] * count
            num -= item[0] * count

        return output

obj = Solution()
print(obj.int_to_roman(20))
print(obj.int_to_roman(1994))
print(obj.int_to_roman(58))
print(obj.int_to_roman(3))
