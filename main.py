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

# def revTheArr(n,arr):
#   firstHalfProduct = 1
#   secondHalfProduct = 1

#   for i in range(0, n // 2):
#     firstHalfProduct *= arr[i]
#   for i in range(n // 2, n):
#     secondHalfProduct *= arr[i]
  
#   if firstHalfProduct < secondHalfProduct:
    
#     arr.reverse()
#     return arr
    
    
    
#     return arr.reverse()
#   else:
#     return arr


# print(revTheArr(5,[1,2,3,4,5]))


# sum of n numbers

# class Solution:
#     def seriesSum(self, n : int) -> int:
#         # code here
#         sum = 0
#         for i in range(1,n+1):
#             sum+=i
#         return sum


# largest element of array

# class Solution:
#     def largest(self, arr):
#         largest = -1
        
#         for i in range(len(arr)):
#             if arr[i]>largest:
#                 largest=arr[i]
                
#         return largest


# search x in arr

# class Solution:
#     #Complete the below function
#     def search(self,arr, x):
#         #Your code here
#         idx = 0
      
        
#         for i in range(len(arr)):
#             if arr[i]==x:
#                 return i
            
#         return -1





# cheking sub set
# def isSubset(a, b):
#         # Your code here
    
#     prevA = len(a)
        
#     for i in range(len(b)):
#         for j in range(len(a)):
#             if a[j]==b[i]:
#                 a.pop(j)
#                 break

#     newA = len(a)
                    
#     return prevA == newA+len(b)




# print(isSubset([1,2,3,4,5,6],[2,4]))




# class Solution:
#     #Function to check if a is a subset of b.
#     def isSubset(self, a, b):
#         # Your code here
#         totalN = 0
        
#         for i in range(len(b)):
#             for j in range(len(a)):
#                 if a[j]==b[i]:
#                     totalN+=1
#                     a.pop(j)
#                     break
#         return totalN==len(b)


# class Solution:
#     #Function to check if a is a subset of b.
#     def isSubset(self, a, b):
#         # Your code here
#         m = len(a)
#         n= len(b)
#         for i in range(n):
#             found = False
#             for j in range(m):
#                 if b[i]==a[j]:
#                     found = True
#                     break
                
#             if not found:
#                 return False
                    
#         return True


# class Solution:
#     #Function to check if a is a subset of b.
#     def isSubset(self, a, b):
#         # Your code here
#        hash_set = set(a)
#        for num in b:
#            if num not in hash_set:
#                return False
               
#        return True



# reverse a string

# def reverseString(self, s: str) -> str:
#         # code here
#         arr = list(str)
        
        
#         arr.reverse()
        
        
#         str2 = ''.join(arr)
        
#         return str2


#reverse array in groups

# Function to reverse an array in groups of size k
# def reverseInGroups(arr, k):
#     """
#     Reverses the elements of an array in groups of size k.

#     Args:
#         arr: The list to be reversed in groups.
#         k: The size of each group.

#     Returns:
#         The modified list with elements reversed in groups.
#     """
#     # Get the length of the array
#     n = len(arr)
#     # Iterate through the array with a step of k
#     for i in range(0, n, k):
#         # Check if the current group is within the array bounds
#         if i + k < n:
#             # Reverse the elements within the current group
#             # arr[i:i + k] extracts a slice of the list from index i to i+k (exclusive).
#             # reversed(arr[i:i + k]) returns a reversed iterator of this slice.
#             # arr[i:i + k] = ... assigns the reversed elements back to the slice.
#             arr[i:i + k] = reversed(arr[i:i + k])
#         # If the current group extends beyond the array bounds
#         else:
#             # Reverse the remaining elements from index i to the end of the array
#             # arr[i:n] extracts a slice from index i to the end.
#             # reversed(arr[i:n]) returns a reversed iterator of this slice.
#             # arr[i:n] = ... assigns the reversed elements back to the slice.
#             arr[i:n] = reversed(arr[i:n])
#     # Return the modified array
#     return arr

# print(reverseInGroups([1,2,3,4,5,6,7,8],3))



#  search k in arr
# class Solution:
#     ##Complete this function
#     def searchInSorted(self,arr, k):
#         #Your code here
#         for i in range(len(arr)):
#             if k==arr[i]:
#                 return True
#         return False

# s = Solution()
# print(s.searchInSorted([1,2,3,4,5,6,7,8],8))








import pandas as pd

# Load the data
input_file = 'allcall_report.xlsx'  # replace with your actual file name
data = pd.read_excel(input_file)

# Ensure 'Open Date(DD-MM-YYYY)' and 'Close Date' are datetime
data['Open Date(DD-MM-YYYY)'] = pd.to_datetime(data['Open Date(DD-MM-YYYY)'], format='%d-%m-%Y')
data['Close Date'] = pd.to_datetime(data['Close Date'], format='%d-%m-%Y')

# Calculate the time taken to complete each job
data['Time Taken'] = (data['Close Date'] - data['Open Date(DD-MM-YYYY)']).dt.days

# Group by ASF Name and calculate total calls and average time taken
asf_stats = data.groupby('ASF Name').agg(
    Total_calls=('S.No.', 'count'),
    Avg_time_taken=('Time Taken', 'mean')
).reset_index()

# Rank the ASF Names based on total calls and average time taken
asf_stats['Rank'] = asf_stats.rank(method='first', ascending=[False, True], numeric_only=True).astype(int)['Total_calls']

# Sort by rank
asf_stats = asf_stats.sort_values('Rank')

# Save the result to a new file
output_file = 'asf_ranking.csv'  # replace with your desired output file name
asf_stats.to_csv(output_file, index=False)

print(f"ASF ranking data has been saved to {output_file}")