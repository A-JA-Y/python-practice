# y=2016
# population = 80000
# for i in range(y,2021):

#     if y%2==0:
#         population+= population*(10/100)
#         y+=1
#     else:
#         population-= population*(10/100)
#         y+=1
# print(population)



# class Solution:
#     def isPrime(self, n):
#         # code here
#         if n<=3:
#             return True
#         else:
#             for i in range(1,n):
#                 if n%i==0 and (i!=1 and i!=n):
#                     return False
#             return True
#         return True



# class Solution:
#     def get_min_max(self, arr):
#         minN = arr[0]
#         maxN = 1
#         minMax=[]
        
#         for i in range(len(arr)):
#             if maxN <= arr[i]:
#                 maxN=arr[i]
#         for i in range(len(arr)):
#             if minN >= arr[i]:
#                 minN=arr[i]
        
#         minMax.append(minN)
#         minMax.append(maxN)
        
#         return minMax



# def avg(*args):
#     n = len(args)
#     sum=0
    
#     for i in range(n):
#         sum+= args[i]
        
        
#     return round(sum/n,3)


# print(avg(2, 5))


# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3==0 and i%5!=0:
#             print("Fizz")
#         elif i%5==0 and i%3!=0:
#             print("Buzz")
#         else:
#             print(i)


# two sum


# def two_sum(arr,t):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i]+arr[j]==t:
#                 return [i,j]
#     return []

# print(two_sum([2,7,11,15],9))




# palindrome

def palindromeCheck(n):
    strN= str(n)
    revStrN = ""+reversed(strN)

    if strN==revStrN:
        return True
    else:
        return False

print(palindromeCheck(121))

