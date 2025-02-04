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

def add_digits(int):
    while num >= 10:
        sum_digits = 0
        for digit in str(num):
            sum_digits += int(digit)
        num = sum_digits
    return num

