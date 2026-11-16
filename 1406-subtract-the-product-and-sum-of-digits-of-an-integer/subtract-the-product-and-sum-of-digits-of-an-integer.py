class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        pro = 1
        while n > 0 :
            digit = n % 10
            pro = pro * digit
            sum = sum + digit 
            n = n//10
        c = pro - sum
        return c
        