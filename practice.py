
y=2016
population = 80000
for i in range(y,2021):

    if y%2==0:
        population+= population*(10/100)
        y+=1
    else:
        population-= population*(10/100)
        y+=1
print(population)



class Solution:
    def isPrime(self, n):
        # code here
        if n<=3:
            return True
        else:
            for i in range(1,n):
                if n%i==0 and (i!=1 and i!=n):
                    return False
            return True
        return True



class Solution:
    def get_min_max(self, arr):
        minN = arr[0]
        maxN = 1
        minMax=[]
        
        for i in range(len(arr)):
            if maxN <= arr[i]:
                maxN=arr[i]
        for i in range(len(arr)):
            if minN >= arr[i]:
                minN=arr[i]
        
        minMax.append(minN)
        minMax.append(maxN)
        
        return minMax



def avg(*args):
    n = len(args)
    sum=0
    
    for i in range(n):
        sum+= args[i]
        
        
    return round(sum/n,3)


print(avg(2, 5))


def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i%5==0 and i%3!=0:
            print("Buzz")
        else:
            print(i)


two sum


def two_sum(arr,t):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==t:
                return [i,j]
    return []

print(two_sum([2,7,11,15],9))




palindrome

def palindromeCheck(n):
    strN= str(n)
    revStrN = ""+reversed(strN)

    if strN==revStrN:
        return True
    else:
        return False

print(palindromeCheck(121))


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            curr_value = roman_map[s[i]]

            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value

            prev_value = curr_value

        return result



class Solution:
    def romanToInt(self, s: str) -> int:
        lsStr=str.split("")
        num = 0
        for ch in range(len(lsStr)):
            if lsSTr[ch]=='I':
                num+=1
            if lsStr[ch]=="V":
                num+=5
            if lsStr[ch]=="X":
                num+=10
            if lsStr[ch]=="L":
                num+=50
            if lsStr[ch]=="C":
                num+=100
            if lsStr(ch)=="D":
                num+=500
            if lsStr[ch]=="M":
                num+=1000
        return num
            

s = Solution()
print(s.romanToInt("MCMXCIV"))


def performOperations(arr, operations):
    # Write your code here
    newArr = arr[:]
    for i in range(0,len(arr)):
        for operation in operations:   
            start=operation[i]
            end=operation[i+1]
            
        
        if start < 0 or end > len(newArr) or start >= end:
          continue

        
        sub_array = newArr[start:end]
        sub_array.reverse()

        newArr[start:end] = sub_array


    return newArr



print(performOperations([1,2,3,4,5],[[1,3],[2,4]]))
