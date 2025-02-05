# Suggested code may be subject to a license. Learn more: ~LicenseLog:2624359296.
  # 1. perfect square 
# def isPerfectSquare(num):
#     if num < 0:
#         return False
#     if num == 0:
#       return True
#     x = int(num**0.5)
#     return x * x == num
            
# print(isPerfectSquare(1))

# 2. print the fractions

# def add_digits(int):
#     while num >= 10:
#         sum_digits = 0
#         for digit in str(num):
#             sum_digits += int(digit)
#         num = sum_digits
#     return num


# fibonacci of n number

# def fib(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(5))


# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)


#perfect number

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if(num<=1):
            return False
        divisor_sum = 1
        for i in range(2, int(num**0.5) + 1):
          if num % i == 0:
            divisor_sum += i
            if i * i != num:
              divisor_sum += num // i
        
        return divisor_sum == num

            
        



        

sol = Solution()
print(sol.checkPerfectNumber(28))
print(sol.checkPerfectNumber(6))
print(sol.checkPerfectNumber(496))
print(sol.checkPerfectNumber(8128))


        





