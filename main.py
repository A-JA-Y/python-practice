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

# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         if(num<=1):
#             return False
#         divisor_sum = 1
#         for i in range(2, int(num**0.5) + 1):
#           if num % i == 0:
#             divisor_sum += i
#             if i * i != num:
#               divisor_sum += num // i
        
#         return divisor_sum == num
            
#permution problem : return all possible permutuation of a given list


# def permute(nums):
#     result = []

#     if len(nums) == 1:
#         return [nums[:]]

#     for i in range(len(nums)):
#         n = nums.pop(0)
#         perms = permute(nums)

#         for perm in perms:
#             perm.append(n)
#         result.extend(perms)
#         nums.append(n)

#     return result


# print(permute([1,2,3]))



# happy number

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = self.sum_of_squares(n)
#         return n == 1

#     def sum_of_squares(self, n: int) -> int:
#         sum_squares = 0
#         while n:
#             digit = n % 10
#             sum_squares += digit ** 2
#             n //= 10
#         return sum_squares



# Suggested code may be subject to a license. Learn more: ~LicenseLog:1413961163.
# class Solution:
#     def maximumProduct(self, nums: list[int]) -> int:
#         nums.sort()
#         return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


# def isHappy(n):
#     seen = set()
    
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum_of_squares(n)
#         print(seen)
#     return n == 1
    

# def sum_of_squares(n):
#     sum_squares = 0
#     while n:
#         digit = n % 10
#         sum_squares += digit ** 2
#         n //= 10
#     return sum_squares 

# print(isHappy(19))

#two sum problem
# def twoSum(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

# nums = [2,7,11,15]
# target = 9
# print(twoSum(nums))


# def twoSum(nums, target):
#     num_dict = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in num_dict:
#             return[num_dict[complement], i]

#         num_dict[num] = i

#     return[]

# nums = [2,7,11,15]

# print(twoSum(nums, 18))
        

# sorted and rotated or not
# def check(nums):
#     count = 0
#     for i in range(len(nums)):
#         # Check if the current element is greater than the next element (circularly)
#         if nums[i] > nums[(i + 1) % len(nums)]:    
#             count += 1
#             print(count)
#     return count <= 1

# print(check([3,4,5,1,2]))
# print(check([2,1,3,4]))
# print(check([1,2,3]))

# Given an integer numRows, return the first numRows of Pascal's triangle.

# def generate(numRows):
#     triangle = []
#     for i in range(numRows):
#         row = [None] * (i + 1)
#         row[0], row[-1] = 1, 1
#         for j in range(1, len(row) - 1):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#     return triangle
# print(generate(5))


# frequency
# def max_frequency_elements(nums):
#     counts = {}
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1
#     max_freq = 0
#     for num in counts:
#         max_freq = max(max_freq, counts[num])
#     total_freq = 0
#     for num in counts:
#         if counts[num] == max_freq:
#             total_freq += counts[num]
#     return total_freq

# print(max_frequency_elements([1,2,2,3,1,4]))
# print(max_frequency_elements([1,2,3,4,5]))


# from collections import Counter

# class Solution:
#     def maxFrequencyElements(self, nums: list[int]) -> int:
#         freq = Counter(nums)
#         max_freq = max(freq.values())  # Find the maximum frequency
     
#         return sum(count for count in freq.values() if count == max_freq)


# sol = Solution()
# print(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]))





# def runningSum(nums):
#     running_sum = []
#     current_sum = 0
#     for num in nums:
#         current_sum += num
#         print(current_sum)
#         running_sum.append(current_sum)
#         print(running_sum)
#         print(current_sum)
#     return running_sum

# print(runningSum([1,2,3,4]))



# move zeroes

# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zero_count = nums.count(0)
#         nums[:] = [num for num in nums if num != 0]
#         nums.extend([0] * zero_count)


#User function Template for python3

# def missingNumber(arr):
#     arr.sort()
#     n = len(arr)
    
#     # Check if 1 is missing
#     if arr[0] != 1:
#         return 1

#     # Check if the missing number is in between the array
#     for i in range(n - 1):
#         if arr[i+1] - arr[i] > 1:
#             return arr[i] + 1

#     # If no number is missing in between, check if n+1 is missing
#     return arr[-1] + 1




# print(missingNumber([1,2,4,5]))

# def getSecondLargest(arr):
#     arr.sort()
#     n = len(arr)

#     for i in range(n-2,-1,-1):
#         if(arr[i] != arr[n-1]):
#             return arr[i]
        
#     return -1

# getSecondLargest([2,1,2])


# if(getSecondLargest([2,1,2]) == 1):
#     print("Correct")


# leader number 

# def leaders(arr):
#         # code here
#     ans= [] 
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]<arr[j]:
#                 break
#         else:
#             ans.append(arr[i])
#     return ans

# print(leaders([16,17,4,3,5,2]))


#peak element

# class Solution:   
#     def peakElement(self,arr):
#         # Code here
        
#         for i in range(len(arr)):
#             left = True
#             right = True
            
#             if i > 0 and arr[i]<= arr[i-1]:
#                 left = False
#             if i<(len(arr)-1) and arr[i]<=arr[i+1]:
#                 right = False
                
#             if left and right:
#                 return i

def revTheArr(n,arr):
  firstHalfProduct = 1
  secondHalfProduct = 1

  for i in range(0, n // 2):
    firstHalfProduct *= arr[i]
  for i in range(n // 2, n):
    secondHalfProduct *= arr[i]
  
  if firstHalfProduct < secondHalfProduct:
    # Changed: arr.reverse() modifies the list in-place and returns None.
    # We need to return the reversed list itself.
    arr.reverse()
    return arr
    
    
    
    return arr.reverse()
  else:
    return arr


print(revTheArr(5,[1,2,3,4,5]))






    

   


        





        
            




       


