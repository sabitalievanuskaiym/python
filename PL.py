# жаль в начале не сохраняла
# import random
# while True:
#   x = random.randint(1,5)
#   y = random.randint(1,5)
#   res = x+y
#   print(x,"+",y,"=")
#   val = input("Answer is :")
#   if (res ==int(val)):
#     print("МОЛОДЕЦ")
#   else:
#     print("НЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ")

# ----------------------------===========================================
# 06.09.23
# PL

# ARRAY

# arr = [13,14,17]
# arr.append(19)
# arr.append(12)
# print(arr)


# arr = [12,13,14,15]
# x = input("Age of a new student:")
# arr.append(int(x))
# print(sum(arr)/len(arr))


# n = 0
# s =0
# while True:
#     x = input("Age og a new student:")
#     s = s+  int(x)
#     n = n+1
#     print(s/n)


# n = 0
# s = 0
# while True:
#     op = input("add or subract(1,0):")
#     x = input("age:")
#     if op == "1":
#         n = n+1
#         s = s+int(x)
#     else:
#         n = n -1
#         s = s-int(x)
#         print(s/n)   


# arr = [12,13,14,14]
# n = sum(arr)/len(arr)
# print(n)


# arr = [1.2,1.3,1.4,1.9,1.7]
# n = sum(arr)/len(arr)
# print(n)
# for a in arr:
#     if a>n*1.2:
#         print("higher",a)
#     if a<n*0.8:
#       print("lower",a)   


# arr = [15,15,15,14,14,14,13,13,16,18,20,22]
# def maxi(arr):
#    x=arr[0]
#    for a in arr:
#       if a > x:
#          x = a
#    return x         

# def min(arr):
#    x = arr[0]
#    for a in arr:
#       if a<x:
#          x = a
#       return x
      

# arr = [15,15,15,14,14,14,13,13,16,18,20,22]
# n = sum(arr)/len(arr)
# print(n)

# arr = [15,15,15,14,14,14,13,13,16,18,20,22]
# n = sum(arr)
# print(n)

# -------------------------------------===================================
# 07.09.23
# PL

# HM
# a = [1,2,3,4,5]
# x = len(a)
# for i in range(x-1):
#     a[i]=a[i]+a[i+1]
# print (a)


# arr = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(arr)):
#     if i < len(arr)-1:
#         arr[i] = arr[i]+arr[i+1]
#     else:
#         arr[i]= arr[i]+arr[0]
# print (arr)        

# -------------------------------------===================================
# 11.09.23
# PL-продолжение 

# arr = [1,2,3,4]
# x = arr[0]
# arr[0]=arr[1]
# arr[1]=x 
# print(arr)

# arr = [1,3,5,8,9]
# def swap (arr, a,b):
#     x = arr[a]
#     arr[a ]=arr[b]
#     arr [b]=x
#     return arr
# print (swap (arr, 2,4))

# only in python
# arr[0],arr[1]=arr[1],arr[0]
# print (arr)

# arr1 = [ 2,4,6,8]
# arr2 = [3,7,3,9]
# print(arr1+arr2)

# arr = [1,3,5,6]
# i = 0
# while i <len(arr):
#       print(arr[i])
# i = i+1

# проходит с верху вниз и сравнивает
# arr1 = [1,3,5,6]
# arr2 = [2,4,7]
# j = 0
# i = 0
# while j<len(arr1)and i<len(arr2):
#  if arr1[j]<arr2[i]:
#   print(arr1[j])
#   j = j+1
#  else:
#   print(arr2[i])
#   i = i+1

# while i < len(arr2):
#  print(arr2[i])   
#  i= i+1

# while j < len(arr1):
#     print(arr1[j])
#     j =j+1
# print(sorted(arr1+arr2))

# распечатать до индекса (4)
# arr = [3,5,6,8,10,9]
# i = 0
# while i < 4:
#     print(arr[i])
#     i = i+1

# 2) второй вариант
# a = 0
# for a in arr:
#     print(a)
#     a = a+1
#     if a ==4:
#      break

# arr = [3,2,6,7,3,4,5,6]
# print(arr[:4])    

# arr = [5,3,6,8,10]
# i = 0
# while i < 3:
#     print(arr[i])
#     i = i+1

# arr = [5,3,6,8,10]
# print(arr[:3])

# arr1 = [5,3,6]
# arr2 = [1,2]

# arr3 = arr1+arr2
# print(arr3)
# -----------------------------------------------=======================
# HM
# arr = [7,23,45,5,67,87]

# def maxi(arr):
#  x = arr[0]
#  for i in arr:
#   if i>x:
#     x = i
#  return (x)   

# def min(arr):
#    x = arr[0]
#    for i in arr:
#       if i<x:
#          x = i

#    return (x)   


# def swap (arr,a,b):
#   x = arr[a]
#   arr[a] = arr[b]
#   arr[b]=x
#   return arr
# a=arr.index(maxi(arr))
# b=arr.index(min(arr))
# print (arr)
# print(swap(arr,a,b))

# -----------------------------------------------=======================
# 12.09.23
# PL

# arr = [3,5,8,6,2,1]
# def get_min_index(arr):
#     min = arr[0]
#     for i in arr:
#         if i < min:
#             min = i
#     index = 0
#     while arr[index]!=min:
#         index = index +1
#     return index
# print(get_min_index(arr))

# arr = [1,3,5,8,6,2,4]
# def find_index(arr,value):
#     index = 0
#     while index <len(arr) and arr[index]!=value:  
#         index = index+1
#     if index!=len(arr):
#         return "NOOO"    
#     else:
#         return index
# print(find_index(arr,3,))        
# print(find_index(arr,1,))  

# arr = [1,3,5,8,6,2,4]
# def has_index(arr,value):
#     for x in arr:
#         if x== value:
#             return True
#     return False
# print (has_index(arr,3))

# def median (arr):
#     arr = sorted(arr)
#     mid = len(arr)//2 #int(len(arr)/2)
#     if mid*2 == len(arr):
#         return sum(arr[mid-1:mid+1])/2
#     else:
#         return arr1 +arr2        

# def merge_sorted_arrays(arrr1,arr2):
#     arr3 = []
#     i =0
#     j = 0
#     while i < len(arr1) and j <len(arr2):
#         if arr1[i] <arr2[j]:
#             arr3.append(arr1[[i]])
#             i +=1 #i = i +1

#         else:
#             arr3.append(arr2[j]) 
#             j +=1

#     arr3 += arr1[i:]
#     arr3 +=arr2[j:]  
#     return arr3   
# ========================================================================
# rewrite / 12.09.23 / PL

arr = [1, 2, 4, 6, 3, 4, 1]
# get minimum value
# def min_value(arr):
#     min = arr[0]
#     for x in arr:
#         if x< min:
#             min = x
#     return min

#get min value index
# def min_value_index(arr):
#     min_index = 0
#     for i, val in enumerate(arr):
#         if arr[min_index]< val:
#             min_index = i
#     return min_index
# print (min_value_index(arr))      

# change values locations in the array
# def swap(arr, i ,j):
#   arr[i],arr[j]= arr[j],arr[i]
#   return arr

# get middle value in an array
# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr)//2
#     if mid*2== len(arr):
#         return sum(arr[mid-1:mid+1])/2
#     else:
#         return mid(arr)

# def add_two_arrays(arr1,arr2):
#     return arr1+arr2

# def add_two_arrays2(arr1,arr2):
#     for i in arr2:
#         arr1.append(i)
#     return arr1    

# def merge_sorted_arrays(arr1, arr2):
#     arr3 = []
#     i = 0
#     j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr3.append(arr1[i])
#             i += 1   # i = i + 1
#         else: 
#             arr3.append(arr2[j])
#             j += 1
    
#     arr3 += arr1[i:]
#     arr3 += arr2[j:]

#     return arr3

# arr1 = [1, 2, 3, 9]
# arr2 = [4, 5]
# print("merge sort")
# print(arr1)
# print(arr2)
# print(merge_sorted_arrays(arr1, arr2))

# def avrage1(arr):
#     x = 0
#     for i in arr:
#      x += i
#     return x/len(arr)

# def average2(arr):
#     s = 0
#     i = 0
#     while i < len(arr):
#         s += arr[i] # i = i + 1
#         i += 1
#     return s / i

# def has_value (arr,value):
#     for i in arr:
#         if i == value:
#             return True
#     return False    
# print(has_value(arr,8))

# def has_value2 (arr,value):
#     index = 0
#     while index < len(arr):
#         if arr[index]== value:
#             return True
#         index +=1
#     return False
# print(has_value2(arr,3))    

# arr = [1, 2, 3, 5, 6, 7]
# def get_value_index(arr, value):
#     index = -1
#     for i, val in enumerate(arr):
#         if value == val:
#             index = i
#     return index
# print(get_value_index(arr,7))

# byyyyeee, I go to slip ^-^
#                         ~
# ========================================================================
# 13.09.23
# Tuple
# 2d avrage
# arr =[[100,100],[1,3],[3,5],[3,4],[4,6],[5,4]]
# def avg(arr):
#     sx = 0
#     sy = 0
#     for i in arr:
#         sx += i[0]
#         sy+= i[1]
#     return sx/len(arr),sy/len(arr) 
# print(avg(arr))   

# def distance(p1,p2):
#  dx = (p2[0]-p1[0])
#  dy = (p2[1]+p1[1])
#  return(dx**2+dy**2)**0.5


# def avg2(arr):
#     sx,sy = 0,0
#     for x,y in arr:
#         sx,sy = sx+x,sy+y
#     return sx/len(arr),sy/len(arr)

# def distance (p1,p2):
#     dx = p1[0]-p2[0]

# arr = [[1,2],[2,3],[3,4],[5,6],[]]
# ========================================================================
# PL
# # ПОВТОРЕНИЕ
# arr = [[1,1],[3,5],[4,6],[7,5],[1,8],[7,2]]
# s = []

# def max_dist(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#            d = int(max_dist(arr[i], arr[j]))
#            s.append([i,j,d])
#     return s
# print(max_dist(arr))

# arr = [[2005,10,10],[2005,10,9],[2005,3,18],[2005,12,29],[2003,1,19]]
# def min_value3(arr):
#     min = arr[0]
#     for 
            
# ======================================================================
# ПОВТОРЕНИЕ ПОЛНОСТЬЮ

# arr = [1, 2, 4, 6, 3, 4, 1]

#                       get minimum value
# def min_value(arr):
#     mi = arr[0]
#     for i in arr:
#         if i < min:
#             min = i
#     return i
# print (min_value(arr))        

#                       get max value index
# def get_max_index(arr):
#   max_index = 0
#   for i, val in enumerate(arr):
#     if arr[max_index]< val:
#       max_index = i
#   return max_index
# print(get_max_index(arr))   
    

#                 change values locations in the array

# def swap(arr,i,j):
#     arr[i],arr[j]=arr[j],arr[i]
#     return arr
# print(swap(arr))

#                   get middle value in an array
# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr) // 2    # int(len(arr)/2)
#     if mid*2 == len(arr):
#         return sum(arr[mid-1 : mid+1])/2
#     else:
#         return arr[mid]
# print(median(arr))

# def add_two_arrays(arr1, arr2):
#     return arr1 + arr2

# def add_two_arrays(arr1, arr2):
#     for i in arr2:
#         arr1.append(i)
#     return arr1

# arr1 = [1, 2, 3]
# arr2 = [4, 5]
# print(add_two_arrays(arr1, arr2))

# arr1.append(arr2)
# print(arr1)
  
# def merge_sorted_arrays(arr1, arr2):
#     arr3 = []
#     i = 0
#     j = 0
#     while i <len(arr1) and j < len(arr2):
#         if arr1[i]<arr2[j]:
#             arr3.append(arr1[i])   
#             i+=1
#         else:
#             arr3.append(arr2[j])
#             j +=1
       
#     arr3 +=(arr1[i:])
#     arr3 +=(arr2[j:])
#     return arr3

# def average1(arr):
#     s = 0
#     for i in arr:
#         s+=i
#         i+=1
#     return s/len(arr)

# def average2(arr):
#     s = 0
#     i = 0
#     while i < len(arr):
#         s+=arr[i]
#         i+=1
#     return s/i

# def has_value(arr, value):
#     for i in arr:
#         if value ==i :
#             return True
#     return False

# def has_value2(arr, value):
#     index = 0 
#     while index < len(arr):
#         if arr[index] == value:
#             return True
#         index += 1
    
#     return False

# arr = [1, 2, 3, 5, 6, 7]
# def get_value_index(arr, value):
#     index = -1
#     for i, val in enumerate(arr):
#         if value ==val:
#             index = i
#     return index
    
# print(get_value_index(arr,2))

# ??????????????????????????????????????????\
# def avg2(arr):
#     sx, sy = 0, 0
#     for x, y in arr:
#         sx, sy = sx + x, sy + y
#     return sx/len(arr), sy/len(arr)

# def distance(p1, p2):
#     dx = p1[0]-p2[0]
#     dy = p1[1]-p2[1]
#     return (dx**2+dy**2)**0.5

# def max (arr):
#     m = arr[0]
#     for i in arr:
#         if m < i:
#             m = i
#     return m


# =======================================================================
# Pl / 14.09.23
# s = 'emil'
# print(s[1]+s[0]+s[2:])
  
# arr = [1,2,3,4,5,6]
# arr = [arr[1]]+[arr[0]]+arr[2:]
# print (arr)

# s = 'emilbek'
# x = 'bek'
# def has_word(s,x):
#     i = 0
#     for i in range(len(s)):
#         if x == s[i:i+3]:
#             return True
        
#     return False
# print  (s.upper())#zaglavnye bukvy
# print(s.split(' ')) 


# def get_word_lengths(words):
#     arr = []
#     for i in words:
#         length = len(i)
#         arr.append(len(i))
#     return arr

# =======================================================================
# PL/ 18.09.23
# arr = [12,13,14,1345]
# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr)//2
#     if mid*2 ==len(arr):
#         return (arr[mid-1:mid+1])/2
#     else:
#         return arr[mid]
# def avg(arr):
#     s = 0
#     for i in arr:
#         s +=i
#         return s/len(arr)
# if median(arr)==avg(arr):
#     print("good")
# else:
#     print("not good")
# =======
# if avg(arr)>median(arr)*1.1:
#   print("not good")
# else:
#   print("good")

# arr = [1,3,5,1,6,2,3,1]
# print (set(arr))

# arr = [1,3,5,1,6,2,3,1]
# def find_value(arr,val): 
#   x = 0
#   for i in arr:
#     if i == val:
#         x +=1
#   return x
# for i in set(arr):
#    print(i,find_value(arr,i))

# arr1 = [1,2,3,5]
# arr2 = [1,2,3,8,9]
# print(set(arr1 + arr2)) 
# print(set(arr1) | set(arr2))#&
# print(set(arr1)-set(arr2)) #arr2-arr1 = {8,9}
# arr3=[]
# for i in arr1:
#     for j in arr2:
#         if i ==j:
#             arr3.append(i)
# print(arr3)
# [1,2,3]

# arr3=set()
# for i in arr1:
#     for j in arr2:
#         if i ==j:
#             arr3.add(i)
# print(arr3)
# {1,2,3}

# arr3=set(range(0,10))
# for i in arr1:
#     for j in arr2:
#         if i ==j:
#             arr3.add(i)
# print(arr3)

#?

# arr3=set()
# for i in arr1:
#     for j in arr2:
#         if i ==j:
#             pass
#     else:
#         arr3.add(i)
# print(arr3)       
# arr1 = [4,2,3,5,2,2]
# arr2= [10,2,3,8,9,2]
# #  -
# arr3=set()
# for i in arr1:
#     is_found = False
#     for j in arr2:
#         if i ==j:
#             is_found == True
#             break
#     if is_found == False:
#         arr3.add(i)
# print(arr3) 

# ===================================================
# PL/leetcode
# for i in range(3):
#      print(i)
# for j in range(4):
#         print(j)


# arr1 = [1,2,3,1,2]
# arr2=[2,3,4,4]
# a,b = set(arr1), set(arr2)
# c = set()
# for i in a:
#     if i in b:
#         c.add(i)
# print(c)
# print (a&b)

# c = {1,2,3}
# c.add(1)
# c.add(2)
# c.add(4)
# print(c)

# arr1 = [1,2,3,1,2]
# arr2=[2,3,4,4]
# a,b = set(arr1), set(arr2)
# c = set()
# for i in a:
#     if i not in b:
#         c.add(i)
# print(c)
# print (a-b)

# HM/ "OR"
# arr1 = [1,2,3,1,2]
# arr2=[2,3,4,4]
# a,b = set(arr1), set(arr2)
# c = set()
# for i in a:
#     c.add(i)
# for j in b:
#     c.add(j)
# print(c)
# # print(a|b)

# ==================================================
# PL/20.09.23
# arr = [1,3,4,7,4,9]
# def find(arr):
#     count = 0 
#     for i in arr:
#         count +=1
#     return count
# print(find(arr))

# arr = []
# from random import randint

# for i in range(10):
#     x = randint(0,10)
#     arr.append(x)
#     arr =[randint(0,10)]
# print(arr)

# arr = [3,5,6,5,6,7]
# x = [1 for i in arr]
# print(x)

# arr= [2,3,4,5,2,4,2]
# t = 2
# res = []
# for i, val in enumerate(arr):
#     if val == t:
#         res.append(i)
# print(res)

# x = [i for i , val in enumerate(arr) if val == t]
# print(x)

# arr1 = [2,3,5,6]
# arr2 = [5,4,2,1,6]
# arr3 = []
# for i, val1 in enumerate(arr1):
#     for j, val2 in enumerate(arr2):
#         if val1 == val2:
#          arr3.append([i,j])
# print(arr3)

# arr4 = [[i,j]for i, val1 in enumerate(arr1) for j,val2 in enumerate(arr2) if val1 ==val2]
# print (arr4)

# a = 10
# b = 6
# print(a if a>b else b)

# a = input("v1")
# b = input ("v2")
# c = input ("v3")

# if a>b and a>c:
#     print(a)
# if b>a and b>c:
#     print(b)
# else:
#     print(c)

# arr1 = [2,3,5,6,4]
# arr2 = [3,6,1,8,4]     
# arr3 = []
# for i in arr1:
#     if i in arr2:        &&&&&
#         arr1.append(i)



# arr1 = [2,3,5,6,4]
# arr2 = [3,6,1,8,4]
# a,b = set(arr1), set(arr2)
# c = set()
# for i in a:
#     if i not in b:
#         c.add(i)
# print (c)

# arr1 = [2,3,5,6,4]
# arr2 = [3,6,1,8,4]
# a,b = set(arr1), set(arr2)
# c = set()
# for i in b:
#     if i not in a:
#         c.add(i)
# print (c)
# ниже по стрингу

# arr = (1,2)
# print (arr[0])
# # arr[0] = 5 # dont do that
# print(arr)

# ==============================================================
# PL/21.09.23
# arr = [1,2,3,2]
# def f(arr):
#     x = 0
#     for i in arr:
#         if i < x:
#             x = i
#     return x
# print(f(arr))

# def f3 (arr):
#     max = 0
#     for index in arr:
#         if len(index)<max:
#              max = len(index)
#     return max
# arr = ['abc','bc','d','ab']
# print(f3(arr))
    

# arr1 = [1,2,3,3,4]
# arr2 = [2,3,5,5,5]
# print ((set(arr1)&arr2(2)) | (set(arr2)-set(arr1)))

# def f():
#     return 1
# for i in range(10):
#     print (f())

# x = input ('')
# y = input ('')
# print (max(x,y))

# x = [1,2,3,4,5,6]
# y = [0,0,0,0,0]

# x [0],y[1] = x[2],y[0]
# print(x)

# arr = [1,2,4,1,5,2,6,3,2]
# target = 2
# def has_target(arr, target ):
#   counter = 0
#   for i in arr:
#    if target == i:
#     counter +=1
#   return counter
# print(has_target(arr, target))

# arr = [1,2,4,1,5,2,6,3,2]
# target = 2
# def target_index(arr, target ):
#   index = []
#   for i, val in enumerate(arr):
#    if target == val:
#     index.append(i)
#   return index
# print(target_index(arr, target))

# s = 'hi, hello, uraa, pre'
# words = s.split(' ')
# def get_word_lengths(words):
#     arr = []
#     for i in words:
#         out = len(i)
#         out = i
#     return out
# print (get_word_lengths(words))



# s = 'hi, uraa,goood, no,yeaaaah, '
# words = s.split(',')
# def get_len_longest_word(words):
#     max = 0
#     for i, val in enumerate(words):
#        x = len(val)
#        if x> max:
#            max = x
#     return max
# print(words)
# print (get_len_longest_word(words))

# s = 'hi, hello, uraa, gooood'
# words = s.split(' ')
# def get_word_count(words):
#     count = 0
#     for i in words:
#         count+=1
#     return count
# print(get_word_count(words))

# str = 'super'
# s = list(str)
# i = 1
# j = 3
# s[i],s[j]=s[j],s[i]
# str = "".join(s)
# print (str)

# arr1 = [1,2,3,4,5]
# arr2 = [2,4,6,7,8]
# def uniq_val(arr1, arr2):
#     x = []
#     y = []

#     for i in arr1:
#         if i not in x and i not  in arr2:
#             x.append(i)

#     for j in arr2:
#         if j not in y and j not in arr1:
#             y.append(j)

#     return x,y
# print (uniq_val(arr1,arr2))

# text = 'hell hi pree god megaaa '
# words= text.split()
# def longest_word(words):
#   x = words[0]
#   for i in words:
#      if len(i)> len(x):
#       x = i
#   return x
# print(longest_word(words))

# text = 'hell hi pree god megaaa '
# words= text.split()
# def longest_word(words):
#  x = 0
#  for i in words:
#   if len(i)>x:
#    x = len(i)
#  return x
# print(longest_word(words))

# a  ="forest"
# s = list(a)
# s[2:],s[4:6]=s[4:6],s[:2]
# a = "".join(s)
# print (a)

# s = "maybe, hello, gooood, god"
# words = s.split()
# def longest_word(words):
#     x =words[0]
#     return x


# =====================================================
# PL/25.09.23

# fb = open("C:/Users/user/Desktop/textFile.md","r")
# line= fb.read()
# words = line.split()
# def longest_word(words):
#     x = words[0]
#     for i in words:
#         if len(i)> len(x):
#             x = i
#     return x

# print (longest_word(words))
# fb.close()

# fb = open("C:/Users/user/Desktop/textFile.md","r")
# for i in fb:
#     print(i)
# fb.close()

# ===================================================
# 26.09.23/PL

# fb = open(f"C:/Users/user/Desktop/text.txt","r")
# line = fb.read()
# arr = line.split(",")
# def avg(arr):
#     s = 0
#     for i in arr:
#         s+=int(i)
#     return s/len(arr)
# print(avg(arr))
# print(arr)
# fb.close()

# =================================
# def mymax(s):
#     sarr=s.split(",")
#     x = []
#     for i in sarr:
#         x.append(int(i))
#     return max(x)

#------------------------
# fb = open(f"C:/Users/user/Desktop/input.txt","r")
# line = fb.read()
# arr = line.split("\n")
# for i in arr:
#     print(i, mymax(i))
# ---------------------------

# fo = open("C:/Users/user/Desktop/output.txt","w")
# fi = open(f"C:/Users/user/Desktop/input.txt","r")
# line = fi.read()
# arr = line.split("\n")
# x = ""
# out = []
# for i in arr:
#     x = i+ ',' +str(mymax(i))
#     out.append(x)
# fo.write("\n".join(out))
# print(x)
# print(out)
# print("\n".join(out))


# ===============================================================
# HM /csv
# import csv

# out = []
# for i in csv.reader(open("names.txt")):
#     out.append([i[1], 0, 0])


# for i in csv.reader(open("payment.txt")):
#     out[int(i[0]) ][1] += int(i[2])
#     out[int(i[0]) ][2] += 1

# arr = []
# for i in out:
#     arr.append(f"{i[0]},{i[1]},{i[2]}")
# b = "\n".join(arr)

# print(b)
# open("output.txt", "w").write(b) 
# -----------------------------------------------
# ==================================================
# -----------------------------------------------
# повторение
# from random import randint
# fb = open ("plus.txt","w")
# for i in range(100):
#  val1 = randint(0,10)
#  val2 = randint(0,10)
#  s2 = f"{val1}+{val2} = \n"
#  fb.write(s2)
# fb.close()

# fb = open ("plus.txt","w")
# for i in range(1,6):
#     x,y = random.randint (0,10),random.randint (0,10)
#     fb.write (f"{x},{y}\n")
# fb.close()

# n = 4
# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x = i*x
#     return x
# print(factorial(n))

# ==================================================================
# 03.10.23/PL

# import csv 
# reader_name = csv.reader(open("names.txt"))
# reader_transactions = csv.reader(open("transactions.txt"))

# names = [name for id, name, num ,adress in reader_name]
# print(names)

# super_arr = [[]for i in range(len(names))]
# print(super_arr)

# for id,date,amount in reader_transactions:
#     super_arr [int(id)].append(int(amount))
# print(id, date, amount,super_arr)

# def avg(arr):
#     s = 0
#     c = 0
#     for i in arr:
#         s+=i
#         c+=1
#     return s/c
# for name, num in zip(names, super_arr):
#     print(name, num,sum(num),"-", max(num), len(num),sum(num)/len(num), avg(num))


# arr = [1,2,3,4,6,7,7,9,10]
# arr2 = []
# for i , val in enumerate(arr):
#     if i != val+1:
#         arr2.append(i+1)
# print(arr2)

# arr = [1,2,3,4,6,7,7,8,9,10]
# arr2 = []
# for i , val in enumerate(arr):
#     if i != val+1:
#         # arr[i]=i+1
#         arr2.append(i+1)
# print(arr2)

# ===========================================================
# Emir version
# import csv 
# reader_student = csv.reader(open("students.txt"))
# reader_classes = csv.reader(open("classes.txt"))
# reader_static = csv.reader(open("taken_classes_by_students.txt"))

# names = [( name )for id, name in reader_student]
# names_case = [[]for i in range(len(names))]

# lessons = [name for id, name in reader_classes]
# names_lessons = [[]for i in range(len(lessons))]

# print("    Count of кто сколько взял")

# for id,id_classes, date in reader_static:
#     names_case[int(id)].append(id_classes) #count less
#     names_lessons[int(id_classes)].append(1) #count for less

# for name, arr in zip(names,names_case):
#     print(name, len(arr))

# print("    Count of taken classes")


# for lessons, arr in zip(lessons,names_lessons):
#     print(lessons, sum(arr))
# print ("    Count of NOT taken classes")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import csv
# reader_students = csv.reader(open("students.txt"))
# reader_classes = csv.reader(open("classes.txt"))
# reader_classes_taken= csv.reader(open("classes_taken.txt"))

# students = [(id, name) for id, name in reader_students]
# classes = [(id, class_name) for id, class_name in reader_classes]
# taken = [[student_id, class_id] for student_id, class_id, year in reader_classes_taken]

# ### HOW MANY CLASSES EACH STUDENT TOOK?
# arr = []
# for sid, name in students:
#     taken_classes = set()
#     all_classes = set([id for id, name in classes])
#     for student_id, class_id in taken:
#         if sid == student_id:
#             taken_classes.add(class_id) 
#     print(name, len(taken_classes))
#     print(name, taken_classes)
#     non_taken_classes = all_classes - taken_classes
#     print(name, non_taken_classes)
#     # out = []
#     # for id in non_taken_classes:
#     #     index = int(id)
#     #     out.append(classes[index][1])
#     # print(name, out)
#     print(name, [classes[int(id)][1] for id in non_taken_classes]) #?


# print()
# ### FOR EACH CLASS HOW MANY STUDENTS TAKEN? 
# arr = []
# for id, class_name in classes:
#     count = 0
#     for student_id, class_id in taken:
#         if class_id == id:
#             count += 1
#     print(class_name, count)
#     #arr.append((clas_name, count))
# ## open("classes_taken.txt").write("\n".join(arr))
# print()
# ### FOR EACH STUDENT WHICH CLASSES DIDNT TAKE?

# for sid, name in students:
#     all_classes = set([id for id, name in classes])
#     #taken_classes = set()
#     for student_id, class_id in taken:
#         if sid == student_id:
#             all_classes.discard(class_id)
#         #taken_classes.add(class_id)
#     print(name, [classes[int(i)][1] for i in all_classes]) #?
#     #print(name, all_classes - taken_classes)


# =======================================================
# # 04.10.23/ PL
# import csv
# trans = list(csv.reader(open("trans.txt")))
# valuta = "usd,kzt,euro,rub".split(',')
# x = 0
# for arr in valuta:
#     count = 0
#     balance = 0
#     for val,amount, cost in trans:
#         if arr == val:
#             count+=1
#             balance += int(amount)
#     print(f"{arr}, count={count}, balance={balance}")

# som = 10000
# for val, amount, cost in trans:
#     if x < abs(int(cost)):
#         x = abs(int(cost))
#         result = [val, amount, cost]
#     som += int(cost)

# print('som', som)
# print('max trans', result)

# som = 10000
# for i, (val, amount, cost )in enumerate (trans):
#     if x < abs(int(cost)):
#         x = abs(int(cost))
#         id = i
#     som += int(cost)

# print('som', som)
# print('max trans', trans[id])
# ================================================================
# =====================================================================
# PL LAB/10.10.23


# 1) Find the full name of the customer who purchased the most expensive car.
# 2) Find the median car cost.
# 3) Find the most popular car color.
# 4) Find the car model that was sold the least.
# 5) Find the average car model year.
# 6) Find the median customer age.
# 7) Find if any cars were sold to customers in Denver, Colorado. If there were sales,

# # import csv
# x=list (csv.reader(open("car_dealership.txt")))
# dealership=[[pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost] for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x] 
# def who_bought_mostexcar(arr):
#     full_name=0
#     a=float("-inf")
#     for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
#        car_cost=int(car_cost.replace("$",""))
#        if car_cost>a:
#            a=car_cost
#            full_name=f"{f_n} {l_n}"
#     return full_name
# print(f"{who_bought_mostexcar(dealership)} bought the most expensive car")
# print()
# def median(arr):
#     s=[]
#     for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
#         s.append(int(car_cost.replace("$","")))
#         s=sorted(s)
#         mid=len(s)//2
#         if mid*2==len(s):
#             mid=sum(s[mid-1:mid+1])/2
#         else:
#             mid=s[mid]
#     return mid
# print(f"${median(dealership)} is median car cost")
# print()
# colors=list(set([car_color for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x]))
# def popular_car_color(arr):
#     counter = [0 for color in colors]
#     for color in colors:
#      for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
#        if color==car_color:
#           counter[colors.index(color)]+=1
#     return colors[counter.index(max(counter))]
# print(f"{popular_car_color(dealership)} is the most popular color")
# print()
# cars=list(set([car_model for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in x]))
# def least_sold_car(dealership):
#  counter = [0 for car in cars]
#  least_sold_cars=[]
#  for car in cars:
#      for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in dealership:
#        if car==car_model:
#           counter[cars.index(car)]+=1
#  least_sold_cars.append([val for i,val in enumerate(cars) for j,val2 in enumerate(counter) if val2==min(counter) and i==j])
#  return least_sold_cars
# print(f"{least_sold_car(dealership)} ware sold the least")
# print()
# def avg_car_year(arr):
#    sum=0  
#    for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
#      sum+=int(model_year)
#    return sum//len(arr)
# print(f"{avg_car_year(dealership)} the average car model year" )
# print()
# def median_customer(arr):
#     ages=[]
#     s=[]
#     for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in arr:
#         ages.append(date_birth.split("."))
#     for i in ages:
#         s.append(2023-int(i[2]))
#         s=sorted(s)
#         mid=len(s)//2
#         if mid*2==len(s):
#             mid=sum(s[mid-1:mid+1])/2
#         else:
#             mid=s[mid]
#     return mid
# print(f"{median_customer(dealership)} is the median customer age" )
# print()
# def was_sold(dealership):
#    x='Colorado Denver'
#    count=0
#    m=0
#    for pid,f_n,l_n,gender,date_birth,state,city,car_model,model_year,car_color,car_cost in dealership:
#      place=f"{state} {city}"
#      if place==x:
#         count+=1
#         return True,count
# print(f"{was_sold(dealership)}  cars were sold to customers in Denver, Colorado")

# =================================================================
# 17.10.23
# import csv
# id,name,movie,date,time

# x = csv.reader(open("movie_list.txt"))
# data = [[id,name,movie,date,time] for id,name,movie, date,time in x]
# id = [id[0] for id in data]
# name_act = [name[1] for name in data]
# movie_name =[movie[2] for movie in data]
# date_movie = [date[-2] for date in data]
# time_movie =[time[-1] for time in data]


# def avg_time(arr):
#     if len(arr):
#         s = 0 
#         for hour, minute in arr:
#             s+=int(hour)*60 + int(minute)
#         avg = s/ len(arr)
#         hours = int(avg/60)
#         mins = int(avg%60)
#         return f"{hours}:{mins}"

# def long_movie(movie_name, data):
#     duration = [0 for movie in movie_name]
#     for id,name,movie,date,time in data:
#         hour, minute = [int(i) for i in time.split(":")]
#         time = int(hour)*60 + int(minute)
#         if time: 
#            duration[movie_name.index(movie)]+=time     
#     mx = max(zip(duration,movie_name))
#     print(f"{mx[1]} -> the longest movie, duration is - {mx[0]//60}:{mx[0]%60}")


# def short_movie(movie_name, data):
#     duration = [0 for movie in movie_name]
#     for id,name,movie,date,time in data:
#         hour, minute = [int(i) for i in time.split(":")]
#         time = int(hour)*60 + int(minute)
#         if time: 
#            duration[movie_name.index(movie)]+=time 
#     mn = min(duration)
#     out = []
#     for id,name,movie,date,time in data:
#         hour, minute = [int(i) for i in time.split(":")]
#         time = int(hour)*60 + int(minute)
#         if time == mn:
#             out.append(name)

#     print(f"The shortest movie duration is - {mn//60}:{mn%60}: {out}")
    
# def total_duration(movie_name,data):
#     total_dur = 0
#     for id,name,movie,date,time in data:
#         hour, minute = [int(i) for i in time.split(":")]
#         time = int(hour)*60 + int(minute)
#         if time:
#             total_dur += time
#     print(f"Total duration - {total_dur//60}:{total_dur % 60}")

# def late_movie(data, qdate):
#     qdate = [int(i) for i in qdate.split(".")]
#     qdate = qdate[2] * 365 + qdate[1] * 30 + qdate[0]
#     lates = []
#     for id,name,movie,date,time in data:
#         date = [int(i) for i in date.split(".")]
#         date = date[2] * 365 + date[1] * 30 + date[0]
#         if date > qdate:
#             lates.append(name)
#     print(f"Late movies - {lates}")

# def mini_movie(data,qtime):
#     qtime = qtime = [int(i) for i in qtime.split(":")]
#     short = []
#     for id,name,movie,date,time in data:
#         time = time = [int(i) for i in time.split(":")]
#         if time< qtime:
#             short.append(name)
#     print(f"Less duration movies - {short}")

# def specific_data_movie(data,qdate):
#     specific_year = []
#     for id,name,movie,date,time in data:
#         date = [int(i) for i in date.split(".")]
#         if date[2] == qdate:
#             specific_year.append(name)
#     print(f"Released in a specific year - {specific_year}")


# def general_stats(movie_name, id):
#         print("GENERAL STATS")
#         print("average time of movies - ",avg_time([time.split(":") for id, name, movie,date, time in data]),)
#         print("")
#         long_movie(movie_name, data)
#         print("")
#         short_movie(movie_name, data)
#         print("")
#         total_duration(movie_name, data)
#         print("")
#         late_movie(data,"10.09.2023")
#         print("")
#         mini_movie(data,"1:01")
#         print("")
#         specific_data_movie(data,2024)
        

# general_stats(movie_name, id)

# ============================================================
# 18.10.23/ PL 

# import csv
# items = list(csv.reader(open("sales.txt")))

# purchased_items = []
# for date,name,quantity,price in items:
#     if int(quantity)>0:
#         purchased_items.append((name,price))

# def get_price(purchased_items, name):
#     for items_name, item_price in purchased_items:
#         if name == items_name:
#             return int(item_price)
# input_date = input("Insert the date - ")

# viruchka = 0
# for date, name, quantity, sale_price in items:
#     if int(quantity)<0  and date == input_date:
#         purchase_price = get_price(purchased_items,name)
#         # print(quantity, purchase_price, int(sale_price))
#         viruchka +=(purchase_price - int(sale_price))* int(quantity)
# print("Viruchka : ", viruchka)

# -------------------------
# AGAYS VERSION

# import csv
# items = list(csv.reader(open("sales.txt")))
# d = {name:int(price)for d,name,q,price,in items if int(q)>0}
# input_date = input("Insert the date - ")
# res = [(d[n] - int(p)) * int(q) for dt,n,q,p,in items if int(q)<0 and dt == input_date]
# print("Viruchka - ", sum(res))

# CASH MAP VERSION
# import csv
# valuts = list(csv.reader(open("valuta.txt")))
# purchased_items = {}
# for date,name,quantity,price in items:
#     if int(quantity)>0:
#         purchased_items[name]= int(price)

# input_date = input ("Insert the Date - ")
# viruchka = 0
# for date, name, quantity, sale_price in items:
#      if int(quantity)<0  and date == input_date:
#          purchased_price = purchased_items[name]
#          viruchka+=(purchased_price - int(sale_price))*int(quantity)
# print("Viruchka - ", viruchka)


# ==================================================================
# 19.20.23/PL
# OBMENKA

# import csv
# d = {}
# lines = csv.reader(open("valuta.txt", "r"))

# for curr , quan, price in lines:
#     if curr not in d:
#         d[curr] = []
#     d[curr].append((int(quan),float(price)))

# for curr, arr in d.items():
#     arr = d[curr]
#     quantity_buy = sum([a for a,b, in arr if a > 0])
#     quantity_sell = sum([a for a,b in arr if a < 0 ])
#     buy_cost = sum([a*b for a, b in arr if a > 0])
#     sell_cost = sum([a*b for a,b in arr if a < 0 ])
#     avg_b = buy_cost/quantity_buy
#     avg_s = sell_cost/quantity_sell
#     print("Valuta:",(curr), "= ","AVRAGE BUY-",(avg_b) ,"","AVRAGE SELL ",(avg_s),"/", "Profit-",(quantity_sell*(avg_b- avg_s)),"/","QUANTITY-", (quantity_buy), (quantity_sell))

# ======================================================================
# 23.10.23/ МИДТЕРН ЗАДАНИЕ
# arr1 = [1,2,3,3,3,4,4,1,5,5]
# arr2 = [3,3,3,4,4,4,4,4,4,4]
# d1= {}
# d2= {}
# for i in arr1:
#     if i in d1:
#         d1[i]+=1
#     else:
#         d1[i]=1
# for i in arr2:
#     if i in d2:
#         d2[i]+=1
#     else:
#         d2[i]=1

# for key in d1.keys()&d2.keys():
#     print(key,min(d1[key],d2[key]))


# # ЗАДАНИЕ
# arr1 = [1,1,5, 2, 3, 3, 3, 4, 4]
# arr2=[3, 3, 3, 4, 4, 4, 4, 4,7,8]
# d1 = {}
# d2 = {}

# for i in arr1:
#     if i in d1:
#         d1[i] +=1 
#     else:
#         d1[i] = 1

# for i in arr2:
#     if i in d2:
#         d2[i] += 1  
#     else:
#         d2[i] = 1
# print("COUNT NUMBER FROM FIRST ARR ")
# for key in d1.keys():
#     # if key not in d2:
#         print(key,"->",d1[key])
# print("COUNT NUMBER FROM SECOND ARR")  

# for key2 in d2.keys():
#     # if key2 not in d1: 
#         print(key2,"->",d2[key2])
# print("COUNT OF SIMILAR FIGURES ")

# for key in d1.keys()&d2.keys():

#     print(key,"->",min(d1[key],d2[key])+max(d1[key],d2[key]))

# ===========================================================================
# 24.10.23/PL
# arr = [11,1,5,6,3,8,9,7]
# arr = sorted(arr)
# print(arr)
# d = {}
# for i in arr:
#     if 10-i in d:
#         print([i,10-i])
#     d[i] = True



# =================================================================================
# TEST/LAB/30.10.23
# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr)//2
#     if mid*2 ==len(arr):
#         return sum(arr[mid-1:mid+1])/2
#     else:
#         return arr[mid]
# from collections import defaultdict
# import csv
# d = defaultdict(list)
# student = {}
# lines = csv.reader(open("student_list.txt","r"))
# class_reader = list(csv.reader(open("class_list.txt","r")))
# class_name = {cl_id:cl_name for cl_id, cl_name ,credits in class_reader}
# class_credits = {cl_id:int(credits) for cl_id, cl_name, credits in class_reader}
# for st_id, st_name, year, semester, cl_id in lines:
#     d[st_id].append((year,cl_id))
#     student[st_id] = st_name

# medians = []
# ## avg per student
# for st_id, arr in d.items():
#     credits = [class_credits[cl_id]for year,cl_id in arr]
#     print(student[st_id],'average', sum(credits)/len(credits))
#     print(student[st_id],'missing credits', 240-sum(credits))

#     taken_classes = defaultdict(int)
#     for year, cl_id in arr:
#         taken_classes[year]+= class_credits[cl_id]
        
#     # year_classes = [val for key, val in taken_classes.items()]
#     print(student[st_id],'min', min(taken_classes.values()))
#     print(student[st_id],'max',max(taken_classes.values()))
#     medians.append(median(credits))

# given_students_id = input('Insert student_id: ')
# taken_classes = [class_name[cl_id] for year , cl_id in d [given_students_id]]
# print(student[given_students_id],'take classes', taken_classes)

# print('Median of median credits', median(medians))

# ==========================================================
# 31.10.23/PL

# class my_set():
#     def __init__(self,arr):
#         self.data = []
#         for i in arr:
#             self.data.append(i)

#     def my_add(self,i):
#         if i not in self.data:
#             self.data.append(i)

#     def show(self):
#         print(self.data)

#     def compare(self,obj, n=-1):
#         return self.data[:n]==obj.dasta[:n]
    
#     def my_sort(self):
#         self.data = sorted(self.data)

#     def show_cubes(self):
#         for i in self.data :
#             print(i**3, end= ',')

#     def __len__(self):
#         return len(self.data)
    

# s = my_set([1,2,3,3,3,3,3])
# s.show()
# s.my_add(3)
# s.show()
# s.my_add(2)
# s.show()
# s.compare()
# s.show()
# s.my_sort()
# s.show_cubes
# s.show()



# HomeWork
# class person:
#     def __init__(self,name,phone,picture = "default",discription="I'm using Whatsapp now"):
#         self.name = name
#         # self.surname = surname
#         self.phone = phone
#         self.picture = picture
#         self.discription = discription
#     # def __init__(self,admin):
#     #     self.admin = admin
#     #     self.adm = []
#     # def add_admin(self,admin):
#     #     self.admin.append(admin)

# class group:
#     def __init__(self,name,date,admin,picture="default",discription="I'm using Whatsapp now"):
#         self.name = name
#         self.picture = picture
#         self.discription = discription
#         self.date = date
#         self.admin = admin
#         self.members = []
#     def add_members(self,member):
#         self.members.append(member)

#     # def add_date(self, date):
#     #     self.date.asppend(date)

#     def remove_members(self,member):
#         self.members.remove(member)

#     def show_members(self):
#         for i in self.members:
#             print(i.name)
#             # print(i.phone)
        

#     # def __init__(self,admin):
#     #     self.admin = admin
#     #     self.adm = []
#     # def add_admin(self,admin):
#     #     self.admin.append(admin)    

# class group_second:

#     def __init__(self,name,date,admin,picture="default",discription="I'm using Whatsapp now"):
#         self.name = name 
#         self.picture = picture
#         self.date = date
#         self.admin = admin

#         self.discription = discription
#         self.members = []

#     def add_members(self,member):
#         self.members.append(member)

#     # def add_date(self, date):
#     #     self.date.asppend(date)
    
#     def remove_members(self,member):
#         self.members.remove(member)

#     def show_members(self):
#         for i in self.members:
#             print(i.name)
            
#             # print(i.date)
            


# p1 = person("Oma",328402834)
# p2 = person("Aza",273970238)
# p3 = person("Wara",948248025)
# p4 = person("Roma",8374920)


# print("-------------------------------|")
# g = group("AIT students","12.3.22, 10:45","Aruuke")
# print("Group name: ",g.name)   
# print("Date created: ",g.date)
# print("Admin - ",g.admin)
# print(" ")
# print("Members:")
# g.add_members(p2)
# g.add_members(p4)
# g.add_members(p1)
# g.show_members()

# print("-------------------------------|")

# s = group_second("Colledge","11.5.23, 12:23","Maksat") 
# print("Group name: ",s.name)
# print("Date created: ",s.date)     
# print("Admin - ",s.admin)  
# print(" ")   
# print("Members: ")

# s.add_members(p2)
# s.add_members(p4)
# s.add_members(p1)
# s.show_members()
# print("-------------------------------|")

# #HM/AKBAR--------------------------------------- 
# from datetime import date


# class Group:
#     def __init__(self):
#         self.data = {
#             "name": "",
#             "date": "",
#             "members": [],
#             "admin": [],
#             "ex_members": [],  }

#     def name_group(self, group_name):
#         self.data["name"] = group_name

#     def date_group(self, date):
#         self.data["date"] = date

#     def add_members(self, member):
#         if member not in self.data["members"]:
#             self.data["members"].append(member)

#     def add_admin(self, admin):
#         self.data["admin"].append(admin)

#     def remove_member(self, ex_member):
#         for i in self.data["members"]:
#             if i == ex_member:
#                 self.data["members"].remove(i)
#                 self.data["ex_members"].append(i)

#     def remove_admin(self, admin_name):
#         for i in self.data["admin"]:
#             if i == admin_name:
#                 self.data["admin"].remove(i)

#     def show(self):
#         print(f"Group name: {self.data['name']}")
#         print(f"Created date: {self.data['date']}")
#         print(f"Group members: {self.data['members']}")
#         print(f"Group admins: {self.data['admin']}")
#         print(f"Group ex-members: {self.data['ex_members']}")

# class Group:
#     def __init__(self):
#         self.data = {
#             "name": "",
#             "date": "",
#             "members": [],
#             "admin": [],
#             "ex_members": [],  }

#     def name_group(self, group_name):
#         self.data["name"] = group_name

#     def date_group(self, date):
#         self.data["date"] = date

#     def add_members(self, member):
#         if member not in self.data["members"]:
#             self.data["members"].append(member)

#     def add_admin(self, admin):
#         self.data["admin"].append(admin)

#     def remove_member(self, ex_member):
#         for i in self.data["members"]:
#             if i == ex_member:
#                 self.data["members"].remove(i)
#                 self.data["ex_members"].append(i)

#     def remove_admin(self, admin_name):
#         for i in self.data["admin"]:
#             if i == admin_name:
#                 self.data["admin"].remove(i)

#     def show(self):
#         print(f"Group name: {self.data['name']}")
#         print(f"Created date: {self.data['date']}")
#         print(f"Group members: {self.data['members']}")
#         print(f"Group admins: {self.data['admin']}")
#         print(f"Group ex-members: {self.data['ex_members']}")

# print("----------------------------------|")
# ait_23 = Group()
# ait_23.name_group("AIT students")
# ait_23.date_group(date.today())
# ait_23.add_members("Akbar")
# ait_23.add_members("Atay")
# ait_23.add_members("Temirlan")
# ait_23.add_members("Aziz")
# ait_23.add_members("Akylbek")
# ait_23.add_members("Sadyr")
# ait_23.add_members("Kamchy")
# ait_23.add_members("Dastan")
# ait_23.add_members("Conor")
# ait_23.add_members("Habib")
# ait_23.add_admin("Ulan Agay")
# ait_23.add_admin("Emil Agay")
# ait_23.add_admin("Munara eje")
# ait_23.show()
# print(" ")
# print("----------------------------------|")

# print("After remove")
# print(" ")

# ait_23.remove_member("Sadyr")
# ait_23.remove_member("Kamchy")
# ait_23.remove_member("Akbar")
# ait_23.show()
# print("----------------------------------|")

# print()
# AIT = Group()
# ait_23 = Group()
# ait_23.name_group("COLLEDGE students")
# ait_23.date_group(date.today())
# ait_23.add_members("aza")
# ait_23.add_members("tima")
# ait_23.add_members("emirlan")
# ait_23.add_members("Aziz")
# ait_23.add_members("Akylbek")
# ait_23.add_members("samat")
# ait_23.add_members("Kamchy")
# ait_23.add_members("Dastan")
# ait_23.add_members("lil")
# ait_23.add_members("billie")
# ait_23.add_admin("Ulan Agay")
# ait_23.add_admin("Emil Agay")
# ait_23.add_admin("Munara eje")
# ait_23.show()
# print(" ")
# print("----------------------------------|")

# print("After remove")
# print(" ")

# ait_23.remove_member("billie")
# ait_23.remove_member("aza")
# ait_23.remove_member("samat")
# ait_23.show()

# -===================================================================
# 1.11.23/ WhatApp


# from datetime import datetime

# class Message:
#     def __init__(self, user, text, to):
#         self.user = user
#         self.text = text
#         self.show_sender = True
#         self.show_receiver = True
#         self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         print(f"Message \"{text}\" from {user.name} {user.surname} sended to {to}")
        
#     def __str__(self):
#         return f"{self.time} {self.user.name} {self.user.surname}: {self.text}"

# class Chat:
#     def __init__(self, user1, user2):
#         self.user1 = user1
#         self.user2 = user2
#         self.messages = []
#         print(f"Chat {user1.name} {user1.surname} and {user2.name} {user2.surname} has been created")
    
#     def send_message(self, user, text):
#         user0 = self.user1 if user == self.user2 else self.user2
#         self.messages.append(Message(user, text, f"{user0.name} {user0.surname}"))
        
#     def delete_for_me(self, user, index):
#         msg = self.messages[index]
#         if msg.user == user:
#             msg.show_sender = False
#             print(f"Message \"{msg.text}\" \"deleted for me\" by {user.name} {user.surname}")
#         else:
#             print(f"Error: Message was sended by other user")
            
#     def delete_for_receiver(self, user, index):
#         msg = self.messages[index]
#         if msg.user == user:
#             msg.show_receiver = False
#             print(f"Message \"{msg.text}\" \"deleted for receiver\" by {user.name} {user.surname}")
#         else:
#             print(f"Error: Message was sended by other user")
        
#     def print_messages(self, user):
#         me = self.user1 if user == self.user1 else self.user2
#         notme = self.user1 if user == self.user2 else self.user2
#         print(f"{me.name} {me.surname} and {notme.name} {notme.surname} chat:")
#         for i in self.messages:
#             if i.user == me and i.show_sender:
#                 print(i)
#             elif i.user != me and i.show_receiver:
#                 print(i)
        

# class User:
#     def __init__(
#         self,
#         name,
#         surname,
#         phone,
#         picture="default",
#         description="Hey there! I'm using WhatsApp.",
#     ):
#         self.name = name
#         self.surname = surname
#         self.phone = phone
#         self.picture = picture
#         self.description = description
#         self.chats = {}
#         self.registration_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         print(f"User {self.name} {self.surname} has been created")
        
#     def add_contact(self, user):
#         if f"{user.name} {user.surname}" not in self.chats:
#             chat = Chat(self, user)
#             self.chats[f"{user.name} {user.surname}"] = chat
#             if f"{self.name} {self.surname}" not in user.chats:
#                 user.chats[f"{self.name} {self.surname}"] = chat
#             print(f"{self.name} {self.surname} and {user.name} {user.surname} have been added to each other's contacts")

#     def print_info(self):
#         print(f"{self.name} {self.surname} info:")
#         print(f"Phone number: {self.phone}")
#         print(f"Picture link/default picture: {self.picture}")
#         print(f"{len(self.chats)} chats: \n - {'/n - '.join(self.get_chat_list())}")
#         print(f"Registration time: {self.registration_time}")
        
#     def send_message(self, user, text):
#         key = f"{user.name} {user.surname}"
#         if key in self.chats:
#             self.chats[key].send_message(user, text)
#         else:
#             self.add_contact(user)
#             self.chats[key].send_message(user, text)
    
#     def remove_for_me(self, user, index):
#         key = f"{user.name} {user.surname}"
#         if key in self.chats:
#             self.chats[key].delete_for_me(user, index)
                
#     def remove_for_receiver(self, user, index):
#         key = f"{user.name} {user.surname}"
#         if key in self.chats:
#             self.chats[key].delete_for_receiver(user, index)
    
#     sm = send_message
        
#     def print_messages(self, user):
#         key = f"{user.name} {user.surname}"
#         if key in self.chats:
#             self.chats[key].print_messages(self)
    
#     def get_chat_list(self):
#         return [name for name in self.chats]

# class Group:
#     def __init__(
#         self, name, creator, picture="default", description="I'm a WhatsApp group."
#     ):
#         time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         self.name = name
#         self.creator = creator
#         self.admins = {creator}
#         self.picture = picture
#         self.creation_date = time
#         self.description = description
#         self.members = {creator}
#         self.messages = []
#         self.removed_members = set()
#         self.removed_admins = set()
#         print(f"Group {self.name} has been created by {self.creator.name} {self.creator.surname}")

#     def print_info(self):
#         print(f"{self.name} group info:")
#         member_info = [f"{member.name} {member.surname}" +
#                (", Creator" if member == self.creator else ", Admin" if member in self.admins else "")
#                for member in self.members]
#         members_count = len(self.members)

#         members_str = '\n - '.join(member_info)

#         print(f"{members_count} members: \n - {members_str}")

#         admins_info = [f'{a.name} {a.surname}' + (', Creator' if a == self.creator else '') for a in self.admins]
#         admins_count = len(self.admins)
#         admins_str = '\n - '.join(admins_info)

#         print(f"{admins_count} admins: \n - {admins_str}")


#         print(f"Picture link/default picture: {self.picture}")
#         print(f"Description: {self.description}")
#         print(f"Creation time: {self.creation_date}")
    
#     def add_member(self, member):
#         if member in self.removed_members:
#             self.removed_members.remove(member)
#         self.members.add(member)
#         member.chats[self.name] = self
#         print(f"{member.name} {member.surname} has been added in the {self.name} group")

#     def send_message(self, user, text):
#         if user in self.members:
#             self.messages.append(Message(user, text, f"{self.name} group"))
        
#     sm = send_message
    
#     def remove_for_me(self, user, index):
#         if user in self.members:
#             msg = self.messages[index]
#             if msg.user == user:
#                 msg.show_sender = False
                
#     def remove_for_receiver(self, user, index):
#         if user in self.members:
#             msg = self.messages[index]
#             if msg.user == user:
#                 msg.show_receiver = False
    
#     def remove_member(self, member):
#         if member in self.members:
#             self.members.remove(member)
#             self.removed_members.add(member)
#             print(f"{member.name} {member.surname} has been removed from the {self.name} group")
#         else:
#             print(f"User {member.name} {member.surname} is not in the {self.name} group")

#     def add_admin(self, member):
#         if member in self.members:
#             self.admins.add(member)
#             print(f"{member.name} {member.surname} now an admin in the {self.name} group")
#             if member in self.removed_admins:
#                 self.removed_admins.remove(member)
#         else:
#             print(f"User {member.name} {member.surname} is not in the {self.name} group")
    
#     def remove_admin(self, member):
#         if member in self.admins:
#             self.admins.remove(member)
#             self.removed_admins.add(member)
#             print(f"{member.name} {member.surname} is no longer an admin in the {self.name} group")
#         else:
#             print(f"User {member.name} {member.surname} is not an admin in the {self.name} group")

#     def print_members(self):
#         print(f"{self.name} group members:")
#         for member in self.members:
#             print(
#                 f" - {member.name} {member.surname}"
#                 + (", Creator" if member == self.creator else ", Admin" if member in self.admins else "")
#                 + f", phone number: {member.phone}"
#             )
#     def print_removed_members(self):
#         print(f"Removed {self.name} group members:")
#         for member in self.removed_members:
#             print(f" - {member.name} {member.surname}, phone number: {member.phone}")
    
#     def print_admins(self):
#         print(f"{self.name} group admins:")
#         for member in self.admins:
#             print(f" - {member.name} {member.surname}" + (", Creator" if member == self.creator else "") + f", phone number: {member.phone}")
    
#     def print_removed_admins(self):
#         print(f"Removed {self.name} group admins:")
#         for member in self.removed_admins:
#             print(f" - {member.name} {member.surname}, phone number: {member.phone}")
            
#     def print_messages(self):
#         print(f"Messages in {self.name} group")
#         for i in self.messages:
#             if i.user == self and i.show_sender:
#                 print(i)
#             elif i.user != self and i.show_receiver:
#                 print(i)


# chel1 = User("Michael", "Jordan", 111111111111)
# chel2 = User("Elon", "Musk", 122222222222)
# chel3 = User("Aleksandr", "Nyrko", 996666666666)
# business_group = Group("Business Group", chel3)
# business_group.add_member(chel2)
# business_group.add_member(chel1)
# business_group.print_members()
# business_group.remove_member(chel1)
# business_group.print_members()
# business_group.add_admin(chel2)
# business_group.print_members()
# business_group.print_admins()
# business_group.remove_admin(chel2)
# business_group.print_members()
# business_group.print_admins()
# print()
# chel2.add_contact(chel3)
# chel2.print_info()
# print()
# business_group.print_info()
# print()
# business_group.print_removed_members()
# business_group.print_removed_admins()
# print()
# chel4 = User("Steve", "Jobs", 133333333333)
# chel5 = User("Business", "Man", 144444444444)
# new_group = Group("Very Serious Business", chel5, description="The group for the real Businessmen")
# new_group.add_member(chel2)
# new_group.add_member(chel4)
# print("## trying to add Alekdandr Nyrko in Very Serious Business admins list")
# new_group.add_admin(chel3)
# print("## trying to remove Michael Jordan from the Very Serious Business")
# new_group.remove_member(chel1)
# print("## trying to remove Elon Musk from the Very Serious Business admins list")
# new_group.remove_admin(chel2)
# new_group.add_admin(chel4)
# new_group.print_members()
# new_group.print_info()
# new_group.send_message(chel4, "Hi")
# new_group.send_message(chel2, "Hello")
# new_group.send_message(chel4, "How are you?")
# new_group.send_message(chel2, "I'm fine and you?")
# new_group.send_message(chel4, "I'm fine to")
# new_group.print_messages()
# chel2.send_message(chel4, "I think you're not fine")
# chel4.send_message(chel2, "Why?")
# chel2.print_messages(chel4)
# chel4.remove_for_me(chel2, 1)
# chel2.print_messages(chel4)
# chel4.print_messages(chel2)
# chel4.remove_for_receiver(chel2, 0)
# chel2.print_messages(chel4)
# chel4.print_messages(chel2)
# while True:
#     try:
#         inp = input()
#         exec(inp)
#     except KeyboardInterrupt:
#         exit()
#     except:
#         pass

# =============================================================
# 31.10.23
# class Unit():
#     def __init___(self, input):
#         self.value = input
#         self.left = None
#         self.right = None

# arr = [7,11,2,3,8,18,13,21,4,32,31,45]
# # root = Unit(7)
# # root.right = Unit(11)
# # root.left = Unit(2)
# # root.left.right = Unit(3)
# # root.right.left= Unit(8)
# # root.right.right= Unit(18)
# # root.right.left.right= Unit(13)
# # root.right.right.right = Unit(21)
# # root.left.right.right = Unit(4)
# # root.right.right.right.right = Unit(32)
# # root.right.right.right.right.left = Unit(31)
# # root.right.right.right.right.right = Unit(45)
# def bek(root):
#     if not  root:
#         return
#     bek(root.left)
#     print(root.value , end = ',')
#     bek(root.right)


# def nus(curr_unit,input):
#     if not curr_unit:
#         return Unit(input)
    
#     if curr_unit.value > input:
#         curr_unit.left = nus(curr_unit.left, input)
#     else:
#         curr_unit.right = nus(curr_unit.right, input)\
        
#     return curr_unit

# root = None
# for i in arr:
#     root = nus(root, i)
    
# bek(root)

# =====================================================
# 1.11.23

# from time import time

# class Group():
#     def __init__(self, name, description = ""):
#         self.members = []
#         self.admins = []
#         # self.created_time = time()
#         self.name = name
#         self.description = description

#     def get_name(self):
#         return self.name
    
#     def set_name(self,name):
#         self.name = name    

#     def get_description(self):
#         return self.description
    
#     def set_description(self, description):
#         self.description= description

#     def remove(self, user):
#         self.members.remove(user)

#     def add(self, user):
#         self.members.append(user)

#     def add_admin(self, user):
#         if user in self.members and user not in self.admins:
#             self.admins.append(user)

#     def remove_admin(self, user):
#         if user in self.admins:
#             self.admins.remove(user)

#     def show_info(self):
#         print("*****",self.name.upper(),"*****")
#         print("membors", self.members)
#         print("admins", self.admins)
#         print()

# arr = ["Inter","Real Madrid","Barselona","Arsenal","Dordoi","Semetey"]

# groups = {}

# for name in arr:
#     groups[name] = Group(name)

# groups['Real Madrid'].add("Ronaldo")
# groups['Barselona'].add("Messi")
# groups['Dordoi'].add("Baymatov")
# groups['Arsenal'].add("archavin")

# for name in groups:
#     groups[name].show_info ()

# ====================================================
# 15.10.23/PL
# SASHA

# from datetime import datetime


# class Message:
#     def __init__(self, text, user="You", to="You", forwarded=False):
#         self.user = user
#         self.text = text
#         self.show = True
#         self.forwarded = forwarded
#         self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         print(f'Message "{text}" sended from {user} to {to}')

#     def remove_for_me(self):
#         self.show = False

#     def is_deleted(self):
#         return self.show
    
#     def get_text(self):
#         return self.text

#     def __str__(self):
#         return f"{self.time} {self.user} {'*forwarded*' if self.forwarded else ''}: {self.text}"


# class Connection:
#     def __init__(self, name):
#         self.name = name
#         self.msgs = []

#     def set_tel(self, tel):
#         self.tel = tel

#     def send_msg(self, msg, forwarded=False):
#         self.msgs.append(Message(msg, to=self.name, forwarded=forwarded))

#     def remove_message(self, msg_id):
#         msg_id = int(msg_id)
#         self.msgs[msg_id].remove_for_me()
#         print(f'Message "{self.msgs[msg_id]}" removed')

#     def show_msgs(self):
#         for i, msg in enumerate(self.msgs):
#             if msg.is_deleted():
#                 print(i, msg)

#     def get_msgs(self):
#         return self.msgs

#     def get_msg(self, msg_id):
#         msg_id = int(msg_id)
#         return self.msgs[msg_id]


# c = {}

# # for i in range(100):
# while True:
#     name = input("name : ")
#     print("send(0),show(1),remove(2),count(3),forward(4)")
#     a = input("action : ")
#     match a:
#         case "0":
#             msg = input("msg : ")
#             if name not in c:
#                 c[name] = Connection(name)
#             c[name].send_msg(msg)
#         case "1":
#             if name in c:
#                 c[name].show_msgs()
#             else:
#                 print(f"there is no messages with {name}")
#         case "2":
#             if name in c:
#                 c[name].show_msgs()
#             else:
#                 print(f"there is no messages with {name}")
#                 break
#             msg_id = input("message id : ")
#             c[name].remove_message(msg_id)
#         case "3":
#             if name in c:
#                 print(len(c[name].msgs))
#             else:
#                 print(f"there is no messages with {name}")
#         case "4":
#             from_name = input("from (name) : ")
#             if name in c:
#                 c[name].show_msgs()
#             else:
#                 print(f"there is no messages with {name}")
#                 break
#             msg_id = input("message id : ")
#             if name not in c:
#                 c[name] = Connection(name)
#             c[name].send_msg(c[from_name].get_msg(msg_id).get_text(), forwarded=True)


# ============================================================
# 16.11.23/PL
# KREDIT/KODE
# from time import time,strftime
# class Client:
#     def __init__(self,name,telnumber,amount):
#         self.balance = amount
#         self.name = name
#         self.telnumber =telnumber
#         self.data = []

#     def debuct(self,date,amount):
#         self.balance -= amount
#         self.data.append([date,amount])

#     def show_balance(self):
#         print(f"Client={self.name}'s balance")
#         print(self.balance)

#     def show_payment(self):
#         print("*"*35)
#         print(f"Client={self.name} payment hiistory")
#         for i in self.data:
#             print(i)
#         print("*"*35)

#     def show_payment_between(self,start,end):
#         print(f"Client = {self.name}'s payment for the period of{start} and{end}")
#         for date,amount in self.data:
#             if start <= date <= end:
#                 print(date, amount)

# bank = {}
# bank["bek"] = Client("Bekbolsun","25135",10000)
# bank["Saadat"] = Client("Saadat","353252",3000)
# bank["bek"].debuct("2023-09-01",2000)
# bank["bek"].debuct("2023-09-05",1000)
# bank["Saadat"].debuct("2023-10-01",100)

# bank["bek"].show_balance()
# bank["bek"].show_payment()
# bank["bek"].show_payment_between("2023-09-03","2023-09-15")


#============================================================

# from time import time

# items = {}
# def get_item(barcode):
#     if barcode in items:
#         return items[barcode]

# class Item:
#     def __init__(self, barcode, name, expiration_date, sell_cost):
#         self.barcode = barcode
#         self.name = name
#         self.expiration_date = expiration_date
#         self.sell_cost = sell_cost

#     def get_barcode(self):
#         return self.barcode

#     def get_name(self):
#         return self.name


# class Basket:
#     def __init__(self):
#         self.items = {}
#         self.time = time()
#         self.cost = 0
#         self.quantity = 0
#         self.item_quantity = {}

#     def add(self, barcode, quantity=1):
#         self.item_quantity[barcode] += quantity
#         self.quantity += quantity
#         self.cost += get_item(barcode).cost * quantity

#     def remove(self, barcode, quantity=1):
#         if barcode in self.item_quantity:
#             if self.item_quantity[barcode] == quantity:
#                 del self.item_quantity[barcode]
#                 self.cost -= get_item(barcode).cost * quantity

#             elif self.item_quantity[barcode] > quantity:
#                 self.item_quantity[barcode] -= quantity
#                 self.cost -= get_item(barcode).cost * quantity

#     def print_check(self):
#         print("*"*10, "CHECK", "*"*10)
#         for barcode, quantity in self.item_quantity.item():
#             print(barcode, get_item(barcode).get_name(), quantity)
#         print("Total quantity:", self.quantity)
#         print("Total cost:", self.cost)
# 




# --------------------------------------------------------------------------------------------------
# 16.11.23. SHOP
# from time import time


# class Item:
#     def __init__(self, barcode, name, price, expire, date=None):
#         self.name = name
#         self.barcode = barcode
#         self.time = time()
#         self.expire = expire
#         self.price = price

#     def get_barcode(self):
#         return self.barcode


# class Basket:
#     def __init__(self, get_item, add_money):
#         self.items = {}
#         self.time = time()
#         self.cost = 0
#         self.quantity = 0
#         self.get_item = get_item
#         self.add_money = add_money
#         self.finished = False

#     def add(self, barcode, quantity=1):
#         if barcode not in self.items:
#             self.items[barcode] = 0
#         self.items[barcode] += quantity
#         self.quantity += quantity
#         self.cost += self.get_item(barcode)[-1].price * quantity

#     def remove(self, barcode, quantity=1):
#         if barcode in self.items:
#             if self.items[barcode] == quantity:
#                 del self.items[barcode]
#                 self.cost -= self.get_item(barcode)[-1].price * quantity
#             elif self.items[barcode] > quantity:
#                 self.items[barcode] -= quantity
#                 self.cost -= self.get_item(barcode)[-1].price * quantity

#     def print_check(self):
#         print("*" * 10, " CHECK ", "*" * 10)
#         for barcode, quantity in self.items.items():
#             item = self.get_item(barcode)[-1]
#             print(f"{barcode} {item.name} : {quantity} {item.price * quantity}")
#         print(f"Total quantity: {self.quantity}")
#         print(f"Total cost: {self.cost}")

#     def finish(self):
#         self.finished = True
#         self.add_money(self.cost)
#         for barcode in self.items:
#             for i in range(self.items[barcode]):
#                 self.get_item(barcode).pop()


# class Shop:
#     def __init__(self, name, balance=1000000):
#         self.name = name
#         self.baskets = []
#         self.items = {}
#         self.buy_history = []
#         self.balance = balance

#     def buy_items(self, barcode, name, buy_price, sell_price, expire, amount=1, date=None):
#         if barcode not in self.items:
#             self.items[barcode] = []
#         for i in range(amount):
#             self.items[barcode].append(Item(barcode, name, sell_price, expire, date))
#         self.balance -= buy_price * amount
#         self.buy_history.append([barcode, name, buy_price, amount, time()])

#     def get_item(self, barcode):
#         return self.items[barcode]

#     def add_money(self, amount):
#         self.balance += amount

#     def create_basket(self) -> Basket:
#         self.baskets.append(Basket(self.get_item, self.add_money))
#         return self.baskets[-1]

#     def show_items(self):
#         print("***Items in shop***")
#         print(
#             "\n".join([f"{i}, {v[-1].name}, {len(v)}" for i, v in self.items.items()])
#         )
#         print("*******************")

#     def show_sell_history(self):
#         print(
#             "\n".join(
#                 [
#                     f"***check №{i}:***\nitems:\ntime:{v.time}\n{
#                         "\n".join([f"{
#                             self.get_item(b)[-1].name}:  quantity: {v.items[b]}, cost: {self.get_item(b)[-1].price * v.items[b]
#                         }" for b in v.items])
#                     }\nTotal cost: {v.cost}\n***check end***"
#                     for i, v in enumerate(self.baskets)
#                     if v.finished
#                 ]
#             )
#         )
    
#     def show_buy_history(self):
#         print("***Buy history***")
#         print("\n".join([f"{time} : {name}: amount: {amount} buy price: {price}" for barcode, name, price, amount, time in self.buy_history]))
#         print("*****************")


# magaz = Shop("Magaz")
# magaz.buy_items(7534578345, "Cola", 50, 100, 20241010, 1000)
# magaz.buy_items(7534578344, "Sprite", 50, 100, 20241010, 1000)
# magaz.buy_items(7534578343, "Fanta", 50, 100, 20241010, 1000)
# current_basket = magaz.create_basket()
# current_basket.add(7534578345, 2)
# current_basket.finish()
# current_basket = magaz.create_basket()
# current_basket.add(7534578345, 1)
# current_basket.add(7534578344, 1)
# current_basket.finish()
# current_basket = magaz.create_basket()
# current_basket.add(7534578345, 3)
# current_basket.add(7534578343, 2)
# current_basket.finish()
# current_basket = magaz.create_basket()
# current_basket.add(7534578345, 3)
# current_basket.add(7534578344, 2)
# current_basket.add(7534578343, 1)
# current_basket.finish()
# print("Balance:", magaz.balance)
# magaz.show_items()
# current_basket = magaz.create_basket()
# current_basket.add(7534578345, 3)
# magaz.show_sell_history()
# magaz.show_buy_history()


# ======================================================================
# 17.11.23/VALUTA/OBMENKA


# from time import time, sleep, strftime
# from datetime import datetime


# from random import randint
# def my_sleep():
#     seconds = randint(0,2)
#     print('Sleeping for ', seconds, 'seconds')
#     sleep(seconds)


# class Valuta:
#     def __init__(self, name, amount=0, avg_buy=0, avg_sell=0):
#         self.name = name
#         self.avg_buy = avg_buy
#         self.avg_sell = avg_sell
#         self.amount = amount
#         self.sell_amount = 0
#         self.history = []

    
#     def buy(self, amount, rate):
#         print('Buying: ', self.name, amount, rate)
#         self.avg_buy = (self.amount*self.avg_buy + amount * rate) / (self.amount + amount)
#         self.amount += amount
#         self.history.append([datetime.now(), amount, rate])
    
#     def sell(self, amount, rate):
#         print('Selling: ', self.name, amount, rate)
#         self.avg_sell = (self.sell_amount*self.avg_sell + amount * rate) / (self.sell_amount + amount)
#         self.amount -= amount
#         self.sell_amount += amount
#         self.history.append([datetime.now(), -amount, rate])
                                         
#     def show_profit(self):
#         profit = (self.avg_sell - self.avg_buy) * self.sell_amount
#         print('Profit for ',self.name, profit)
#         return profit
    
#     def show_history(self):
#         print('Showing history for', self.name)
#         for ts, amount, rate in self.history:
#             print(ts.strftime('%H:%M:%S'), amount, rate)


# class Obmenka:
#     def __init__(self, name):
#         self.data = {}
#         self.name = name
    
#     def buy(self, valuta, amount, rate):
#         if valuta in self.data:
#             self.data[valuta].buy(amount, rate)

    
#     def sell(self, valuta, amount, rate):
#         if valuta in self.data:
#             self.data[valuta].sell(amount, rate)
    
#     def add_valuta(self, name):
#         self.data[name] = Valuta(name)

#     def show_profit(self):
#         print()
#         total = 0
#         for name, valuta_obj in self.data.items():
#             total += valuta_obj.show_profit()
#         print('Total profit: ' , total)

#     def show_history(self):
#         print()
#         for name, obj in self.data.items():
#             obj.show_history()


# obmenka = Obmenka('BEKObmen')
# obmenka.add_valuta('dollar')
# obmenka.buy('dollar', 100, 89.5)
# my_sleep()
# obmenka.buy('dollar',500, 89.6)
# my_sleep()
# obmenka.sell('dollar',100, 89.8)
# my_sleep()
# obmenka.buy('dollar',1000, 89.65)
# my_sleep()
# obmenka.sell('dollar',1500, 89.75)
# print()
# obmenka.add_valuta('euro')
# obmenka.buy('euro', 100, 100)
# my_sleep()
# obmenka.sell('euro', 50, 101)
# my_sleep()
# print()
# obmenka.add_valuta('rubl')
# obmenka.buy('rubl', 1000, .89)
# obmenka.sell('rubl', 500, .91)
# print()

# obmenka.add_valuta('kzt')
# obmenka.buy('kzt', 1000, 0.03)
# my_sleep()
# obmenka.buy('kzt', 5000, 0.04)
# my_sleep()
# obmenka.sell('kzt', 2000, 0.05)

# obmenka.show_profit()
# obmenka.show_history()    

# ===================================================
# 20.11.23/MIDTERN/STUDNETS

# class Students:
#     def __init__(self):
#         self.info = {}
#         self.classes = {}
#         self.last = None
#         self.first = None4

#     def set(self, param, value):
#         self.info[param] = value

#     def add_classes(self, class_id, class_name, class_year):
#         self.classes[class_id] = [(class_name, class_year)]
#         self.last = class_id
#         if  self.first is None:
#             self.first = class_id

#     def get_first_last(self):
#         return self.first, self.last
    
#     def remove_classes(self, class_id):
#         self.classes.pop(class_id)

#     def print(self):
#         print(self.info)
# ---------------------------------------------------------------------
# 20.11.23/MIDTERN/STUDNETS

# class Class:
#     def __init__(self, id, name, limit=2, credits=3):
#         self.id = id
#         self.name = name
#         self.limit = limit
#         self.credits = credits

# class Students:
#     def __init__(self):
#         self.info = {}
#         self.classes = {}
#         self.last = None
#         self.first = None
#         self.limit = 3

#     def set(self, param, value):
#         self.info[param] = value

#     def add_class(self, year, enrolled_class):
#         if enrolled_class.limit > 0 and self.limit > 0:
#             self.classes[enrolled_class.id] = enrolled_class
#             self.last = enrolled_class
#             if self.first is None:
#                 self.first = enrolled_class
#             enrolled_class.limit -= 1
#             self.limit -= 1
#             print(f"{self.info['name']} was successfully enrolled to {enrolled_class.name}, {enrolled_class.limit} places left")
#         elif enrolled_class.limit == 0:
#             print(f"{enrolled_class.name} has reached its limit.")
#         elif self.limit == 0:
#             print(f"{self.info['name']} has reached the limit of classes.")

#     def get_first_limit_class(self):
#         return self.first, self.last

#     def remove_class(self, class_id):
#         self.classes.pop(class_id)

#     def print(self):
#         print(self.info)
#         print(self.classes.keys())

# class101 = Class(101, 'PL')
# class201 = Class(201, 'Static')
# class202 = Class(202, 'Operating System')
# class102 = Class(102, 'DM')

# x = Students()
# x.set('name', 'Bekbolsun')

# y = Students()  # Added parentheses to call the constructor
# y.set('name', 'Saadat')

# z = Students()  # Added parentheses to call the constructor
# z.set('name', 'Aziz')

# x.add_class(2023, class101)
# x.add_class(2023, class201)
# x.add_class(2023, class202)
# x.add_class(2023, class101)

# y.add_class(2023, class101)
# z.add_class(2023, class101)

# y.add_class(2023, class101)
# z.add_class(2023, class101)

# ============================================================================
# 22.11.23/PL
# TICKETING SYSTEM

# class User:
#     def __init__(self):
#         self.name = None
#         self.lastname = None
#         self.email = None
#         self.dateofbirth = None
#         self.phone = None

#     def show_info(self):
#         print(f'Name: {self.name}, Lastname: {self.lastname}, DOB: {self.dateofbirth}, email: {self.email}')

# class Seat:
#     def __init__(self):
#         self.material = None
#         self.color = None
#         self.type = None

#     def show_info(self):
#         print(f'Type: {self.type}, material: {self.material}')

# class TicketingSystem:
#     def __init__(self):
#         self.name = None
#         self.prices = None
#         self.users = {}
#         self.seats = {}
#         self.data = {}
#         self.sold = 0
#         self.max_capacity = 0

#     def add_seat(self, info, quantity=1):
#         for i in range(quantity):
#             self.seats[len(self.seats)] = info
#             self.max_capacity += 1

#     def add_user(self, user_info):
#         self.users[len(self.users)] = user_info

#     def user_info(self):
#         for user_id, user_info in self.users.items():
#             print(user_id)
#             user_info.show_info()
#             print()

#     def show_seats(self):
#         for seat_id, info in self.seats.items():
#             if seat_id not in self.data:
#                 print(seat_id)
#                 info.show_info()
#                 print()

#     def buy_ticket(self, seat_id, user_id):
#         if seat_id not in self.data:
#             self.data[seat_id] = user_id
#             self.sold += 1
#         else:
#             print(f'Seat: {seat_id} is already sold to user {self.data[seat_id]}')
#             print()

#     def show_seat_info(self, seat_id):
#         if seat_id in self.data:
#             user_id = self.data[seat_id]
#             print(f'Seat: {seat_id} was sold to user {user_id}')
#             self.users[user_id].show_info()
#             print()


# stadion = TicketingSystem()

# user1 = User()
# user1.name = 'Bek'
# user1.email = 'bek@gmail.com'

# user2 = User()
# user2.name = 'Aziz'
# user2.phone = "050519054"

# user3 = User()
# user3.name = 'Asan'
# user3.email = 'asan@gmail.com'

# stadion.add_user(user1)
# stadion.add_user(user2)
# stadion.add_user(user3)

# seat1 = Seat()
# seat1.type = 'Economy'

# seat2 = Seat()
# seat2.type = 'Vip'

# stadion.add_seat(seat1)
# stadion.add_seat(seat2)

# for i in range(5):
#     seat_id = int(input('Seat id: '))
#     stadion.user_info()
#     user_id = int(input('User id: '))
#     stadion.show_seats()
#     stadion.buy_ticket(seat_id, user_id)
#     stadion.show_seat_info(seat_id)



# =========================================================
# 23.11.23/ AIRPORT
# class Person:
#     def __init__(self, name, lastname, phone, birthdate=None):
#         self.name = name
#         self.lastname = lastname
#         self.phone = phone
#         self.birthdate = birthdate
#         self.email = None


# class Flight:
#     def __init__(self, frm, to, price, departure, arrival, seats):
#         self.frm = frm
#         self.to = to
#         self.price = price
#         self.departure = departure
#         self.arrival = arrival
#         self.seats = seats


# class Airport:
#     def __init__(self, name):
#         self.name = name
#         self.airlines = {}
#         self.clients = {}

#     def add_airline(self, name):
#         print(f"Airline {name} is added in {self.name} airport")
#         self.airlines[name] = {}

#     def add_flight(self, airline, id, frm, to, price, departure, arrival, seats=150):
#         print(
#             f"Flight {airline} {id} from {frm} to {to} d: {departure} a: {arrival} is added in {self.name} airport"
#         )
#         self.airlines[airline][id] = [
#             Flight(frm, to, price, departure, arrival, seats),
#             [-1 for i in range(seats)],
#             [i + 1 for i in range(seats)],
#         ]

#     def add_client(self, person):
#         print(
#             f"Client {person.name} {person.lastname} is registered in {self.name} airport"
#         )
#         self.clients[len(self.clients)] = person

#     def has_client(self, client_id):
#         if client_id in self.clients:
#             return True
#         else:
#             print(f"There is no client {client_id}")
#             return False

#     def buy_ticket(self, airline, flight_id, client_id):
#         if self.has_client(client_id):
#             if len(self.airlines[airline][flight_id][2]) > 0:
#                 seat = self.airlines[airline][flight_id][2][0]
#                 self.airlines[airline][flight_id][1][seat - 1] = client_id
#                 self.airlines[airline][flight_id][2].remove(seat)
#                 client = self.clients[client_id]
#                 print(
#                     f"{client.name} {client.lastname} bought a flight ticket {seat} {airline} {flight_id}"
#                 )
#             else:
#                 print(f"Seats on {airline} {flight_id} have run out")

#     def buy_ticket_seat(self, airline, flight_id, client_id, seat):
#         if self.has_client(client_id):
#             if self.airlines[airline][flight_id][1][seat - 1] == -1:
#                 self.airlines[airline][flight_id][1][seat - 1] = client_id
#                 self.airlines[airline][flight_id][2].remove(seat)
#                 client = self.clients[client_id]
#                 print(
#                     f"{client.name} {client.lastname} bought a flight ticket {seat} {airline} {flight_id}"
#                 )
#             else:
#                 print(f"Seat {seat} on {airline} {flight_id} is already sold")

#     def return_ticket(self, airline, flight_id, seat):
#         if self.airlines[airline][flight_id][1][seat - 1] != -1:
#             client_id = self.airlines[airline][flight_id][1][seat - 1]
#             self.airlines[airline][flight_id][1][seat - 1] = -1
#             self.airlines[airline][flight_id][2].append(seat)
#             client = self.clients[client_id]
#             print(
#                 f"{client.name} {client.lastname} returned the flight ticket {seat} {airline} {flight_id}"
#             )
#         else:
#             print(f"Seat {seat} on {airline} {flight_id} is not sold")

#     def print(self):
#         print(f"============ {self.name} airport ============")
#         for name, airline in self.airlines.items():
#             print(f"======= {name} flights =======")
#             for id, flight in airline.items():
#                 print(f"=== {name} {id} ===")
#                 print(
#                     f"from {flight[0].frm} to {flight[0].to}, price: {flight[0].price}"
#                 )
#                 print(f"departure: {flight[0].departure}, arrival: {flight[0].arrival}")
#                 print(
#                     f"{flight[0].seats - len(flight[2])}/{flight[0].seats} passengers:"
#                 )
#                 for id, client_id in enumerate(flight[1]):
#                     if client_id != -1:
#                         print(
#                             f"{id + 1}: {self.clients[client_id].name} {self.clients[client_id].lastname}"
#                         )
#         print("============================================")


# manas = Airport("Manas")

# manas.add_airline("Manas Airlines")

# manas.add_flight("Manas Airlines", 1000, "Bishkek", "Karakol", 1000, 20231111, 20231111)

# akbar = Person("Akbar", "Kalmatov", 996707717171, 20000427)

# bektur = Person("Bektur", "Kenzhebaev", 996558755783, 20050204)

# akbar.email = "akbar@akbar.akbar"

# manas.add_client(akbar)

# manas.add_client(bektur)

# manas.buy_ticket("Manas Airlines", 1000, 0)

# manas.buy_ticket("Manas Airlines", 1000, 1)

# manas.buy_ticket_seat("Manas Airlines", 1000, 0, 10)

# manas.buy_ticket_seat("Manas Airlines", 1000, 1, 10)

# manas.print()

# ==============================================================================================
# 27.11.23/PL/LIBRARY/ex

# class User:
#     def __init__(self,id,name,phone):
#         self.id = id
#         self.name = name
#         self.phone = phone

#     def show_info(self):
#         print(f'ID:{self.id},Name:{self.name},Phone:{self.phone}')

# class Book:
#     def __init__(self, name, book_id, author,year):
#         self.name = name
#         self.book_id = book_id
#         self.author = author
#         self.year = year

#     def show_info(self):
#         print(f'ID:{self.book_id},Name:{self.name},Author: {self.author},Year:{self.year}')

# class Library:
#     def __init__(self,name):
#         self.name = name
#         self.books = {}
#         self.users = {}
#         self.user_last_id = 0
#         self.data = {}
#         self.booklog = []
    
#     def add_books(self,author, name, year):
#         self.books[len(self.books)] = Book(name,len(self.books),author,year)


#     def add_user(self, name, phone):
#         self.user_last_id +=1
#         self.users[self.user_last_id] = User(self.user_last_id, name, phone)

#     def taken_books(self, book_id, user_id):
#         if user_id not in self.data:
#             self.data[user_id] = []
#         self.data[user_id].append(book_id)
#         self.booklog.append(book_id)

#     def user_info(self, user_id):
#         if user_id in self.users:
#             self.users[user_id].show_info()
#             if user_id in self.data:
#                 for books in self.data[user_id]:
#                     self.books[books].show_info
#         else:
#             print('User id not in the DataBase')

#     def ShowAvaliavility(self,BID):
#             if BID  in self.booklog:
#                 print(f'Book{BID}: is already taken')
#             else:
#                 print(f'Book {BID}: is free to rent')


# =============================================================================
# 28.11.23/POLIMORTISM/ INHERITANCE
# class Car_v1(Items):
#     def set_cartype(self, type):
#         self.car_type = type

#     def set_color(self, color):
#         self.color = color

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.car_type, self.color )


# class Items:
#     def __init__(self,brand,price,weight, location):
#         self.brand = brand
#         self.price = price
#         self.weight = weight
#         self.location = location

#     def get_location(self):
#         return self.location
    
#     def set_location(self, location):
#         self.location = location

#     def show_info(self):
#         pass


# class Car_v2(Items):
#     def __init__(self, brand, price, weight, location, type, color):
#         super().__init__(brand, price, weight, location)
#         self.color = color
#         self.car_type = type

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.car_type, self.color)

# class Shampoo(Items):
#     def __init__(self, brand, price, weight, location, compound, gender):
#         super().__init__(brand, price, weight, location)
#         self.gender = gender
#         self.compound = compound

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.gender, self.compound)

# class TShirt(Items):
#     def __init__(self, brand, price, weight, location,material):
#         super().__init__(brand, price, weight, location)
#         self.material = material

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.material)

    
# def add_item(cart, item):
#     cart.append(item)

# def move(cart, location):
#     for item in cart:
#         item.set_location(location)

# car = Car_v2('BMW', 5000, 1500, 'Bishkek','sedan','black')
# tshirt = TShirt('nike', 15,0.1, 'Bishkek','cotton') 
# shampoo = Shampoo('Clear',5,1,'Bishkek','water','male')
# cart = []

# add_item(cart,car)
# add_item(cart,tshirt)
# add_item(cart,shampoo)

# move(cart,'NY')

# car.show_info()
# shampoo.show_info()
# tshirt.show_info()


# =======================================================================
#INTERFACE/ CALCULATOR
# import sys
# import keyboard
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QFont

# from random import randint

# class AIT(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.label1 = QLabel("Label1")
#         self.label2 = QLabel("Label2")
#         self.operator = QLabel("OPS")
#         self.equal = QLabel("=")
#         self.result = QLineEdit("")

#         self.operation_layout = QHBoxLayout()
#         self.operation_layout.addWidget(self.label1)
#         self.operation_layout.addWidget(self.operator)
#         self.operation_layout.addWidget(self.label2)
#         self.operation_layout.addWidget(self.equal)
#         self.operation_layout.addWidget(self.result)

#         font = QFont()
#         font.setPointSize(50)
#         self.button_ok = QPushButton("✔️")
#         self.button_retry = QPushButton("❌")
#         self.button_next = QPushButton("-->>>")

#         self.button_next.clicked.connect(self.generate_random_number)
#         self.button_retry.clicked.connect(self.clear_result)
#         self.button_ok.clicked.connect(self.check_result)

#         self.operation_layout.addWidget(self.button_ok)
#         self.operation_layout.addWidget(self.button_retry)
#         self.operation_layout.addWidget(self.button_next)

#         self.generate_random_number()

#         self.setLayout(self.operation_layout)
#         self.setWindowTitle("Вычислите")
#         self.setFixedSize(QSize(500, 500))
#         self.show()

        

#     def check_result(self):
#         v1 = int(self.label1.text())
#         v2 = int(self.label2.text())
#         op = self.operator.text()
#         if op == '+':
#             result = v1 + v2
#         else:
#             result = v1 - v2

#         if result == int(self.result.text()):
#             self.result.setStyleSheet("background-color :green")
#         else:
#             self.result.setStyleSheet("background-color :red")

#     def clear_result(self):
#/         self.result.setText("")
#         self.result.setStyleSheet("background-color:white")

#     def generate_random_number(self):
#         self.result.setText("")
#         self.result.setStyleSheet("background-color:white")
#         val1 = randint(0, 5)
#         val2 = randint(0, 5)

#         op = ['+', '-'][randint(0, 1)]
#         if op == '-':
#             if val1 < val2:
#                 val1, val2 = val2, val1

#         self.label1.setText(str(val1))
#         self.label2.setText(str(val2))
#         self.operator.setText(op)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     counter = AIT()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QFont

#/ from random import randint

7# class AIT(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.label1 = self.create_label("label 1")
#         self.label2 = self.create_label("label 2")
#         self.equal = self.create_label('=')
#         self.operator = self.create_label("")

        
#         self.result = self.create_label('', QLineEdit) #QLineEdit("")
#         self.result.returnPressed.connect(self.check_result)
        
#         self.operation = QHBoxLayout()
#         self.operation.addWidget(self.label1)
#         self.operation.addWidget(self.operator)
#         self.operation.addWidget(self.label2)
#         self.operation.addWidget(self.equal)
#         self.operation.addWidget(self.result)


#         self.button_ok = self.create_button("✅", self.check_result)
#         self.button_retry = self.create_button("❌", self.clear_result)
#         self.button_next = self.create_button("-->>>", self.generate_random_number)

        
#         self.buttons = QHBoxLayout()
#         self.buttons.addWidget(self.button_ok)
#         self.buttons.addWidget(self.button_retry)
#         self.buttons.addWidget(self.button_next)


#         self.layout = QVBoxLayout()
#         self.layout.addLayout(self.operation)
#         self.layout.addLayout(self.buttons)

#         self.generate_random_number()

#         self.setLayout(self.layout)
#         self.setWindowTitle("Вычеслител")
#         self.setFixedSize(QSize(750, 500))
#         self.show()

#     def create_button(self, text, func):
#         button = QPushButton(text)
#         font = QFont()
#         font.setPointSize(50)
#         button.setFont(font)
#         button.setStyleSheet('background-color: grey; border-radius: 50%')
#         button.clicked.connect(func)
#         return button

#     def create_label(self,name,type = QLabel):

#         font = QFont()
#         font.setPointSize(50)
#         label = type(name)
#         label.setFont(font)
#         return label

#     def check_result(self):
#         v1 = int(self.label1.text())
#         v2 = int(self.label2.text())
#         op = self.operator.text()
#         if op == '+':
#             result = v1 + v2
#         else:
#             result = v1 - v2
    
        

#         if result == int(self.result.text()):
#             self.result.setStyleSheet("background-color: green;")
#         else:
#             self.result.setStyleSheet("background-color: red;") 
 
        


#     def clear_result(self):
#         self.result.setText("")
#         self.result.setStyleSheet("background-color: white")

#     def generate_random_number(self):
#         self.result.setText("")
#         self.result.setStyleSheet("background-color : white")
#         val1 = randint(0, 9)
#         val2 = randint(0, 9)

#         op = ['+', '-'][randint(0,1)]
#         if op == '-':
#             if val1 < val2:
#                 val1, val2 = val2, val1
        
#         self.label1.setText(str(val1))
#         self.label2.setText(str(val2))
#         self.operator.setText(op)
        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     counter = AIT()
#     sys.exit(app.exec_())

# ===========================================================================
# 04.12.23/ CAFE/EXAM

# class Food:
#     def __init__(self,price, name, weight):
#         self.price = price
#         self.name = name
#         self.weight = weight

#     def show_info(self):
#         print(f"Name: {self.name},{self.weight}/{self.price}")


# class Main(Food):
#     def __init__(self, price, name, weight):
#         super().__init__(price, name, weight)
#         self.type = "Main Courses"

# class Dessert(Food):
#     def __init__(self, price, name, weight):
#         super().__init__(price, name, weight)
#         self.type = "Dessert"

# class Lagman(Main):
#     def __init__(self, price, name, weight):
#         super().__init__(price, name, weight)
#         self.description = "Lagman"

# class IceCream(Dessert):
#     def __init__(self, price, name, weight):
#         super().__init__(price, name, weight)
#         self.description = "IceCream"


# plov = Main(120,400,15)
# tort = Dessert(150,300, "a lot")
# foods = []
# def add_food(foods,name): 
#     return foods.append(name)
# def cost(foods):
#     sum = 0
#     for food in foods:
#         sum += food.get_price()
#     return sum
# add_food(foods,plov)
# add_food(foods, tort)
# print(cost(foods))
# print(foods)

# ---------------------------------------------------------
# class Meat:
#     def _init_(self) -> None:
#         print('Meat class was initialized')
        
#     def set_animal(self, animal):
#         self.animal = animal

# class Dough:
#     def _init_(self) -> None:
#         print('Dough class was initialized')
    
#     def set_expiration(self, expiration):
#         self.expiration = expiration
        
# class Cow(Meat):
#     def _init_(self) -> None:
#         super()._init_()
#         print('Cow class was initialized')

# class Sheep(Meat):
#     def _init_(self) -> None:
#         super()._init_()
#         print('Sheep class was initialized')
        
# class Lagman(Dough, Sheep):
#     def _init_(self) -> None:
#         super()._init_()
#         Sheep._init_(self)
#         print('Lagman class was initialized')

        
# lagman = Lagman()

# =========================================================
# 06.12.23/ RECURSIVE
# arr = [11,7,8,3,6,4,2,1,0,9]
# def my_sorted(arr):
#     if len(arr)== 0 or len(arr) ==1:
#         return arr
#     left = []
#     last = arr[-1]
#     centeral_arr = []
#     right = []
#     for i in arr:
#         if i > last:
#             right.append(i)
#         if i < last:
#             left.append(i)
#         if i== last:
#             centeral_arr.append(i)
#     return my_sorted(left)+centeral_arr+my_sorted(right)
# print(my_sorted(arr))




# class AirTicket:
#     def __init__(self, name, flight_from, flight_to, seat, price):
#         self.name = name
#         self.flight_from = flight_from
#         self.flight_to = flight_to
#         self.seat = seat
#         self.price = price        

# class Economy(AirTicket):
#     def __init__(self, name, flight_from, flight_to, seat, price, small_luggage):
#         super().__init__(name, flight_from, flight_to, seat, price)
#         self.small_luggage = small_luggage

# class Business(AirTicket):
#     def __init__(self, name, flight_from, flight_to, seat, price, large_luggage):
#         super().__init__(name, flight_from, flight_to, seat, price)
#         self.large_luggage = large_luggage
#         self.legroom = "Availabel"

# class AviaKassa:
#     def __init__(self, name):
#         self.name = name
#         self.seat_econom = []
#         self.seat_business = []

#     def buy_econom(self, passanger):
#         if passanger not in self.seat_econom:
#             self.seat_econom.append(passanger)
#             print(f"Name: {passanger.name}\nSeat: {passanger.seat}\nClass: Econom\nFlight from: {passanger.flight_from}\nFlight to: {passanger.flight_to}\nLuggage: {passanger.small_luggage}\n")
#         else:
#             print("This seat is taken")

#     def buy_business(self, passanger):
#         if passanger not in self.seat_business:
#             self.seat_business.append(passanger)
#             print(f"Name: {passanger.name}\nSeat: {passanger.seat}\nClass: Business\nFlight from: {passanger.flight_from}\nFlight to: {passanger.flight_to}\nLuggage: {passanger.large_luggage}\nLegroom: {passanger.legroom}\n")
#         else:
#             print("This seat is taken")
    
#     def refundable(self, inp_seat):
#         if inp_seat in self.seat_business:
#             self.seat_business.remove(inp_seat)
#         else:
#             print("You can't remove seat")
    
#     def change_seat(self, inp_seat, new_seat):
#         if inp_seat in self.seat_business and new_seat not in self.seat_business:
#             self.seat_business.remove(inp_seat)
#             self.seat_business.append(new_seat)
#             print(f"{inp_seat} changed to {new_seat}")

# kassa = AviaKassa("TEZ JET")

# p1 = Economy("Bayel", "Bishkek", "Dubai", 1, 5000, "small luggage")
# p2 = Business("Adilet", "Bishkek", "Dubai", 2, 15000, "large luggage")

# kassa.buy_econom(p1)
# kassa.buy_business(p2)

# =======================================================================================
# 11.12.23
# RECURSIVE GCD(FACTORIZATION)
def factorizxation(n):
    d = {}
    i = 2
    while n!= 1:
        if n%i == 0:
            if i not in d:
                d[i] = 0
            d[i] +=1
            n = n/i
        else:
            i+= 1
    return d
print(factorizxation(150))

def GCD(n1, n2):
    d1 = factorizxation(n1)
    d2 = factorizxation(n2)
    n = 1
    keys = d1.keys()&d2.keys()
    for key in keys:
        for i in range(min(d1[key],d2[key])):
            n = n*key
    return n
print(GCD(300,80))
    
def GCD2(n1,n2):
    if n1%n2 == 0:
        return n2
    return GCD2(n2, n1%n2)



# -------------------------------------
# # POWER
# def power(a,b):
#     if b == 0:
#         return 1
#     if b ==1:
#         return a
#     x = power(a,b/2)
#     if b %2 == 0:
#         return x*x
#     else:
        # return x*x*a
# print(power(8,12))


# def power2(a,b):
#     n = 1
#     for i in range(b):
#         n = n*a
#     return a

# print(power2(8,12))

# list =[1,3,5,8,12,13,14,18,20,25,30,32]
# def find_target(arr,t):
#     mid = len(arr)//2
#     print(arr)
#     if len(arr) <= 1:
#         ### arr[0]==2
#         return False
#     if t == arr[mid]:
#         return f"Yeah we have {t}"
#     if t > arr[mid]:
#         return find_target(arr[mid:],t)
#     if t< arr[mid]:
#         return find_target(arr[:mid],t)
    
# print(find_target(list,4))