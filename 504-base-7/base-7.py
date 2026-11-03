class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        count = []
        neg = num < 0
        num = abs(num)
        while num != 0 :
            digit = str(num % 7)
            num = num//7
            count.append(digit)

        ans ="".join(count[::-1])
        if neg  :
            return "-"+ans
        else:
            return ans