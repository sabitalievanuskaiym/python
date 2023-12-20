# 07.09.23
# Dicrete Math for CS

# var = {"Geeks","for","Geeks"}
# for i in range(1,100):
#   var.add(i)
# print(var)

# var = {"Geeks","for","Geeks"}
# var.add("WOOO")
# print(var)

# var = {"Geeks","for","Geeks"}
# var.remove("WOOO")
# print(var)

# var = {"Geeks","for","Geeks"}
# while True:
#  var.add("WOOO")
#  print(var)

# set1 = set()
# set2 = set()

# for i in range(5):
#     set1.add(i)

# for i in range(3,9):
#     set2.add(i)

# set3 = set1.intersection(set2)    
# print(set3)

# разница
# set1 = set()
# set2 = set()

# for i in range(5):
#     set1.add(i)

# for i in range(3,9):
#     set2.add(i)

# set3 = set1.difference(set2)    
# print(set3)

# разница
# set1 = set()
# set2 = set()

# for i in range(5):
#     set1.add(i)

# for i in range(3,9):
#     set2.add(i)

# set3 = set1 - set2    
# print(set3)

# удалить
# set1 = set()
# set2 = set()

# for i in range(5):
#     set1.add(i)

# for i in range(3,9):
#     set2.add(i)

# set1.clear()
# print(set1)

# -------------------------------------===================================
# 07.09.23
# intro to comp scince

# arr = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(arr)):
#     if i < len(arr)-1: 
#         arr[i] = arr[i]+ arr[i+1]
#     else:
#         arr[i] = arr[i]+arr[i-1]


# arr = [1,2,3,4,5,6,7,8,9,10]
# x = len(arr)
# for i in range(x-1):
#     arr[i]=arr[i]+arr[i+1]
# arr[9]=arr[9]+arr[0]
# print(arr)

# -----------------------------------------------=======================
# 12.09.23
# discrete math for CS


# num = 0
# for i in range(0,1001):
#  num= num+i
# print(num)

# num =0
# for i in range(10,21):
#     out = 5+2*i
#     num = num+out
# print(num)

# =========================================================================
# 14.09.23
# Math
# arr = []
# rows, cols = 5,5
# for i in range(rows):
#     col = []
#     for j in range(rows):
#         col.append(0)
#     arr.append(col)
# print(arr)

# a=[1,0,1,1]
# def convertBinTolt(a):
#     x=len(a)
#     decNumber=0
#     for i in range(x-1,-1,-1):
#           j=x-i-1
#           decNumber+=2**i*a[j]              
#     return decNumber
# print (convertBinTolt(a))

# a=[1,0,1,1]
# def convertBinTolt(a):
#  a = 6
# def convertIntoBin(a):
#  digit1 = a % 2
# num1 = a/2
# digit2 = num1 % 2
# num2 = num1/2
# digit3 = num2 % 2
# num3 = num2/2
# if(num3 == 0):
#  break

# =========================================================================
# Math / 19.09.23
# arr = []
# for i in range(3):
#     for j in range(2):
#       c[i][j]=a[i][j]*b[i][j]+a[i][j+1]*b[j+1]
# [i]+a[i][j+2]*b[j+2][i]

# a=[[1,0,2][2,3,-1],[3,-2,0]]
# b=[[4,1][0,-3][-1,1]]
# c = []
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         c[i][j]=0
#         for k in range(len(b)):
#             c[i][j]=c[i][j]+a[i][k]*b[k][j]
# print(c)

# =========================================================================
# 21.09.23/ Intro comp
# перевод на байнери
# n =23
# def convertDecToBin(n):
#     binArray = list() #[]
#     rem=n%2
#     binArray.append(rem)
#     quo = n//2
#     while (quo !=0):
#       rem = quo%2
#       quo = quo //2
#       binArray.append(rem)
#     return binArray[::-1]
# print (convertDecToBin(n))

# short version
# n = 23
# def convertDecToBin(n):
#     binArray = []
#     while (n!=0):
#         binArray.append(n%2)
#         n = n//2
#     return binArray[::-1]
# print (convertDecToBin(n))

# перевод на десимел
# a = [1,0,1,0]
# def convertBinToDec(a):
#   size = len(a)
#   sum = 0
#   for i in range(size):
#      sum = sum +2**(size-i-1)*a[i]
#   return sum
# print(convertBinToDec(a)) #10

# =====================================================================
# 28.09.23/MATH
# arr = [1,2,3,3,5]
# arr2 = []
# for i , val in enumerate(arr):
#     if i+1 != val:
#         arr2.append(val)
#         arr2.append(i+1)
# print(arr2)
# print(arr)

arr = [1,2,3,3,5]
arr2 = []
for i , val in enumerate(arr):
    if i != val+1:
        arr[i]=i+1
print(arr)

# arr = [1,2,3,3,5]
# s = set(arr)
# full = set()
# for i, val in enumerate(s):
#     if i != val +1:
#         full.add(val)
#         full.add(i+1)
# print(full)


# arr = {1,2,3,3,5}
# s = set(arr)
# saadat = set()
# for i, val in enumerate(arr):
#     if(i+2)!=val():
#         saadat.append(val)
# ------------------------------------
# 2,4,3,1
# num = [3,1,2,4]
# result = []

# for i in num:
#     if i %2 ==0:
#         result.append(i)
# for j in num:
#     result.appendI(j)
# print (result)

# num = [3,1,2,4]
# for i in num:
#     if num %2 ==0:
#         print(i)
# for j in num:
#     if num% 2 != 0:
#         print(j)
# print (i,j)


# num = [3,1,2,4]
# even_numbers = [x for x in num if x % 2 == 0]
# odd_numbers = [x for x in num if x % 2 != 0]
# sorted_numbers = even_numbers + odd_numbers
# print(sorted_numbers)

# num = [3,1,2,4]
# even_num = []
# odd_num = []
# for i in num:
#     if i %2 == 0:
#         even_num.append(i)
# for i in num:
#     if i % 2 !=0:
#         odd_num.append(i)
# print (even_num + odd_num)


# arr = [3,1,2,4]
# def even_num(arr):
#     a = []
#     p = 0
#     q = len(arr)-1
#     for i in arr:
#        if i%2 == 0:
#            a[p]=i
#            p +=1
#        else:
#            a[q] = i
#            q+=-1
#     return a
# print(even_num(arr))
# ????????????????????????????????????????\

# ===================================================================
# 05.10.23/ MATH TEST
# arr = [1,2,3,5,6,7]
# def find_dub(arr):
#     for i,val in enumerate(arr):
#         if i+1!=val:
#             return val-1
# print(find_dub(arr))
#  ----------------------------------------
# arr = [1,2,3,4,5,6,4,7]
#MATRICS CODE
# def find_dub(arr):
#     arr2 = []
#     for i in arr:
#         if i in arr2:
#            return i
#         arr2.append(i)
# print(find_dub(arr))

# def sum (num):
#   arr = 0
#   for i in range (1, num+1):
#     arr += 2* i +1
#   return arr
# print (sum(5))

# 3
# def prnt_2d_mtrx(mtrx):
#     for i in mtrx:
#         prnt = ""
#         for j in i:
#             prnt += str(j) + "\t"
#         print(prnt)
# mtrx1 = [[1, 0, 4], [2, 1, 1], [3, 1, 0], [0, 2, 2]]
# mtrx2 = [[2, 4], [1, 1], [3, 0]]

# def mtrx_2d_mult(mt1, mt2):
#     if len(mt1[0]) != len(mt2):
#         return [
#             [
#                 "error: the number of rows in the first martix must be equal to the number of columns in the second matrix"
#             ]
#         ]
#     out = []
#     for i in range(len(mt1)):
#         out.append([])
#         for j in range(len(mt2[0])):
#             out[i].append(0)
#             for q in range(len(mt1[i])):
#                 print(mt1[i][q], "*", mt2[q][j], "=", mt1[i][q] * mt2[q][j])
#                 out[i][j] += mt1[i][q] * mt2[q][j]
#                 prnt_2d_mtrx(out)
#                 print("//////////////////")
#     return out
# mtrx_2d_mult(mtrx1, mtrx2)

# second version
# a = [[1, 0, 4], [2, 1, 1], [3, 1, 0], [0, 2, 2]]
# b = [[2, 4], [1, 1], [3, 0]]
# def mat (a,b):
#     arr3 =[]
#     for i in range (len(a)):
#         arr3.append([])
#         for j in range (len(b[0])):
#             arr3[i].append(0)
#             for k in range (len(b)):
#                 arr3[i][j] += a[i][k] *b[k][j]
#     return arr3
# print(mat(a,b))

# ==================================================================
# 11.10.23/CS
# FACTORIAL
# n=5
# def factorial(n):
#     x = 1
#     for i in range(x,n+1):
#         x = i*x
#     return x
# print (factorial(n))
      
# n = 5
# x = 1
# for i in range(1,n+1):
#     x = x*i
# print(x)


# # COMBINATION
# def combination(n,k):
#    return int(factorial(n)/(factorial(k)*factorial(n-k)))
# print(combination(10,5))

# # PERMUTATIAN
# def permutatiom(n,k):
#     return int(factorial(n)/factorial(n-k))
# print(permutatiom(10,5))

# n = len(a)
# arr = "google"
# def rep_perm(arr):
#     set = set(arr)
#     n = len(a)
#     a = []
#     for i in arr:
#         if i not in a:
#             a.append(i)

#     for i in range(n):
#         for j in range(i,n):
#             for k in range(k,n):
#                 print(a[i],a[j],a[a])
# arr = [0,1,1,2,3,5,8,13,21,34]


# def  fibonacci(n):
#     num1 = 0
#     num2 = 1
#     for i in range(0, n-1):
#         num3 = num1 + num2
#         num1 = num2
#         num2 = num3
#     return num2

# print(fibonacci(9))


# def arr(n):
#     fib = [0,1]
#     for i in range (2,n+1):
#         swap = fib [i-1] + fib[i-2]
#         fib.append(swap)
#     return fib
# print(arr(11))

# def recorsion(n):
#     if n<=0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return recorsion(n-1) + recorsion(n-2)
# print(recorsion(9))

# =====================================================================
# intro/ 16.10.23

# while True:
#     try:
#         a = int(input("first - "))
#         b = int(input("second - "))
#         c = int(input(f"{a}+{b}="))
#         if a+b == c:
#             print("correct")
#         else:
#             print("nooo")
#     except ZeroDivisionError:
#         print("there you have 0")
#     except ValueError:
#         print("do normanlly")


# from random import randint
# count_correct = 0
# count_nooo = 0
# while True:
#     try:   
#         ops = "+-/*"
#         index = randint(0,3)
#         a = randint(0,10)
#         b = randint(1,10)
#         result = 0
#         if ops == "/":
#             result, a = a, a * b
#         c = int(input(f"{a}{ops[index]}{b} = "))

#         if result == c:
#             count_correct +=1
#             print(f'Number of correct answers: {count_correct} Number of wrong answers: {count_nooo}')
#             print("Correct!")
#             continue
        
#         elif a-b==c and ops[index] =="-":
#             count_correct +=1
#             print(f'Number of correct answers: {count_correct} Number of wrong answers: {count_nooo}')
#             print("correct")
#         elif a+b == c and ops[index] == "+":
#             count_correct +=1
#             print(f'Number of correct answers: {count_correct} Number of wrong answers: {count_nooo}')
#             print("correct")        
#         elif a*b ==c and ops[index] == "*":
#             count_correct +=1
#             print(f'Number of correct answers: {count_correct} Number of wrong answers: {count_nooo}')
#             print("correct")
#         else:          
#             count_nooo +=1
#             print(f'Number of correct answers: {count_correct} Number of wrong answers: {count_nooo}')
#             print("NOOOOO")
      
#     except ZeroDivisionError:
#         if a/"0":
#          print("WE CANT DIVITE FOR 0")
#     except ValueError:
#         print("WRITE INTEGER NUUMBER!!!")

# ==============================================================
# 19.10.23/Math.CS

# arr= "001101"
# new_arr= ""
# for i in arr:
#     if i=="0":
#         new_arr+="1"
#     else:
#         i=="1"
#         new_arr+="0"
# print(new_arr)

# s = "ab#c"
# t = "ad#c"
# def remove_and_compare(s, t):
#     def remove_hash(s):
#         result = []
#         for char in s:
#             if char != "#":
#                 result.append(char)
#             elif result:
#                 result.pop()
#         return "".join(result)
    
#     return remove_hash(s)==remove_hash(t)

# if  remove_and_compare(s, t):
    # print("Cовпадают после удаление:)")

# else:
    # print("Не сопадают:(")

# s = "america"
# t = s[:3]
# print(t)


# import time

# st = time.process_time()
# sum_x = 0
# for i in range(1000000):
#     sum_x+=i

# time.sleep(20)
# print("Sum of first 1 million is: " , sum_x)

# et = time.time()

# elapsed_time = et - st
# print("Execution time: " , elapsed_time, "second")

# ====================================================================================
# =================================================================
# =================================================================
# =================================================================
# ==================================================================================
# =================================================================
# =================================================================
# =================================================================
# ===================================================================================
# 24.10.23/MATH
#PALIMDROME 
# def pali(x):
#     a = x
#     y = 0
#     while a>0:
#         k = a%10
#         y = y*10+k
#         a = a//10
#     if x==y:
#         return True
#     return False
# print(pali(12321))


# a ="12321"
# def pali(a):
#     for i in a:
#         x = a[::-1]
#         if a == x:
#             return True
#     return False
# print(pali(a))


# ================================================================================
# HM
# ## 1 TASK
# n=4421
# def difference(n):
#     a=n
#     y=1
#     x=0
#     while a>0:
#         k=a%10
#         y=y*k
#         x+=k
#         a=a//10
#     return y-x
# print(difference(n))


# ### 2 TASK
# def convertDecToBin(n):
#     binArray = []
#     while n != 0:
#         rem = n % 2
#         n = n // 2
#         binArray.append(rem)
#     while len(binArray) < 4:
#         binArray.append(0)
#     return binArray[::-1]

# print(convertDecToBin(1))

# def xor_operation(n1, n2):
#     a = convertDecToBin(n1)
#     b = convertDecToBin(n2)
#     xor_results = []
#     for i in range(len(a)):
#         xor_results.append(a[i] ^ b[i])
#     return xor_results

# print(xor_operation(11, 5))

# ### 3 TASK
# arr1=[1,4,6,6,7,8,10,11]
# arr2=[2,4,5,9]
# def merge_sorted(arr1,arr2):
#     arr3=[]
#     i=0
#     j=0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<arr2[j]:
#             arr3.append(arr1[i])
#             i+=1
#         else:
#             arr3.append(arr2[j])
#             j+=1
#     arr3+=arr1[i:]
#     arr3+=arr2[j:]
#     return arr3
# print(merge_sorted(arr1,arr2))

# ## 4 TASK
# def white_black(coordinates):
#     numbers="12345678"
#     letters="abcdefgh"
#     a=0
#     b=0
#     for i in range(len(letters)):
#       if coordinates[0]==letters[i]:
#         if i%2==0:
#          a=False
#         else:
#           a=True
#       if coordinates[1]==numbers[i]:
#         if i%2==0:
#           b=False
#         else:
#           b=True
#     return a^b
# print(white_black("h3"))


# ===================================================================
# # 31.10.23.MATH


# def is_prime(number):
#     if number <= 1:
#         return False
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#     return True

# number = 18
# if is_prime(number):
#     print(f"({number}) --> is a prime number.")
# else:
#     print(f"({number}) --> is NOT a prime number.")



# def count_primes_in_factorial(n):
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i

#     primes_count = 0
#     divisor = 2
#     while factorial > 1:
#         if factorial % divisor == 0:
#             primes_count += 1
#             while factorial % divisor == 0:
#                 factorial //= divisor
#         divisor += 1

#     return primes_count

# n = 12 
# count = count_primes_in_factorial(n)
# print(f"Количество простых чисел в {n}! равно {count}")




# ====================================================================
# class Substitute_Cipher:
# # CRYPTOLOGY
#     def __init__(self):
#         self.ciph  = ""
#         self.a1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         self.a2 = "NOPQRSTUVWXYZABSDEGHIJKLM"


# ]=====================================================================
# 23.11.23
# EUCLID ALGOTITHM

# def gcd(a,b):
#     while b:
#         remainder = a % b
#         a = b
#         b = remainder
#     return a
# ab = int(input("A - "))
# ba = int(input("B - "))
# result = gcd(ab,ba)
# print(f"GCD -> {ab} and {ba} = {result}" )


# def gcd_euclid(a,b):
#     if a%b == 0 :
#         return b
#     else:
#        return gcd_euclid(b,a%b)

# # print(gcd_euclid(91,287))

# def lcm_euclid(a,b):
#     return a*b/gcd_euclid(a,b)
# print(lcm_euclid(91,287))


# def gcd(a, b):
#     while b:
#         remainder = a % b
#         a = b
#         b = remainder
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# def lcm_of_multiple_numbers(numbers):
#     result = 1
#     for num in numbers:
#         result = lcm(result, num)
#     return result

# numbers = [36,24]
# result = lcm_of_multiple_numbers(numbers)
# print(f"LCM o--> {numbers} is {result}")



# def factorize(n):
#     factors = []
#     i = 2
#     while i * i <= n:
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#         i += 1
#     if n > 1:
#         factors.append(n)
#     return factors
# print(factorize(24))
    

# def unique_factors(numbers):
#     all_factors = []
#     for num in numbers:
#         factors = factorize(num)
#         for factor in factors:
#             if factor not in all_factors:
#                 all_factors.append(factor)
#     return all_factors


# def lcm_of_multiple_numbers(numbers):
#     all_factors = unique_factors(numbers)
#     lcm = 1
#     for factor in all_factors:
#         max_power = max([factorize(num).count(factor) for num in numbers])
#         lcm *= factor ** max_power
#     return lcm

# # Example usage:
# numbers = [36, 24]
# result = lcm_of_multiple_numbers(numbers)
# print(f"LCM of {numbers} is {result}")

# ======================================================================
# 29.11.23/ REPEAT FOR EXAM OF MATH

# def coaser(s):
#     new_str = ""
#     letters = {"A":1.....}
#     for i in s:
#         for key,val in letters.items():
#             if letters [i]+3 == val:
#                 new_str += key

#             if letters[i]+ 3 > max(letters.values()):
#                 if letters[i]+3 - 26== val:
#                     new_str += key


# s = "HelLo"
# res = ""
# for i in s:
#     maxz = ord("z")
#     x = ord(i)+3
#     if x > maxz:
#         res+= chr(x -26)
#     else:
#         res+= chr(x)
# print(res)


# primes = [2, 3, 5, 7, 11, 13, 17, 23, 27, 29]
# def is_prime(n):
#     for i in primes:
#         if  n % i == 0:
#             return False
#     return True

# print(is_prime(101))    


# =============================================================================
# 02.12.23/ MERGE SORTED

# arr1 = [1,4,5,7,8,9]
# arr2 = [2,3,6,10]
# def merge_sorted(arr, arr2):
#     arr3 = []
#     i = 0
#     j = 0
#     while i< len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr3.append(arr1[i])
#             i +=1
#         else:
#             arr3.append(arr2[j])
#             j +=1

#     arr3 += arr1[i:]
#     arr3 += arr2[j:]

#     return arr3
# print(merge_sorted(arr1, arr2))

# -----------------------------------------
# outarr = []
# def merge_rec(arr1, arr2, outarr):
#     if (len(arr1) == 0):
#         outarr += arr2
#         return
#     if (len(arr2) == 0):
#         outarr += arr1
#         return
#     if (arr1[0] < arr2[0]):
#         outarr.append(arr1[0])
#         merge_rec(arr1[1:], arr2, outarr)
#     else:
#         outarr.append(arr2[0])
#         merge_rec(arr1,arr2[1:], outarr)

# print(merge_rec(arr1,arr2,outarr))


# def power_two(n):
#     if n == 2:
#         return True
#     elif n<2:
#         return False
#     else:
#         return power_two(n/2)
# print(power_two(8))

# def is_power_of_two(n):
#     while n < 1:
#         if n %2 != 0:
#             return False
#         n /= 2
#     return False

# x = 1
# n = 16
# def recursive(x,n):
#     if x == n:
#         return True
#     elif x > n:
#         return False
#     else:
#         return recursive(x*2,n)
    
# print(recursive(x,n))

# =============================================
# class Subtitute_Cipher:
#     def __init__(self):
#         self.ciph = ""
#         self.alph1 = "ABCDEFDHIJKLMNOPQRSTUVWXYZ"
#         self.alph2 = "NOPQRSTUVWXYZABCDEFGHIJKLM"
#     def cipher(self, input):
#         for value in input:
#             self.ciph += self.alph2[self.alph1.index(value)]
#     def get_cipher(self):
#         return self.ciph

# s = Subtitute_Cipher()
# s.cipher("HELLO")
# x = s.get_cipher()
# print(x)




# world1=['sabit']
# world2=['nuska']
# x=''
# for i in world1:
#     x+=i+world2[0]
# print(x)


# ======================================================================
# 07.12.23

# from random import randint
# from time import time

# def create_1000_x_1000_matrix():
#     return [[0 for i in range(1000)] for i in range(1000)]

# def generate_1000_x_1000_matrix():
#     return [[randint(0, 10) for i in range(1000)] for i in range(1000)]

# a = generate_1000_x_1000_matrix()
# b = generate_1000_x_1000_matrix()

# c = create_1000_x_1000_matrix()

# tic = time()
# for i in range(1000):
#     for j in range(1000):
#         c[i][j] = a[i][j] * b[i][j]
# toc = time()
# print("Row-wise multiplication time:", toc - tic)


# c = create_1000_x_1000_matrix()  
# tic = time()
# for i in range(1000):
#     for j in range(1000):
#         c[j][i] = a[j][i] * b[j][i]
# toc = time()
# print("Column-wise multiplication time:", toc - tic)



