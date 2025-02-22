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