# def quicksort(arr):
#     if len(arr) <=1:
#         return arr
#     mid = arr[len(arr)//2]
#     mids = []
#     right = []
#     left = []
#     for i in arr:
#         if i > mid:
#             right.append(i)
#         elif i == mid:
#             mids.append(i)
#         else:
#             left.append(i)
#     print(left, mids, right)
#     return quicksort(left) + mids + quicksort(right)
# print(quicksort([1,2,4,5,6,7,4,3,6,0]))

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 5, 6, 7, 1, 3]

# def merge_sorted_two_arrays(arr1, arr2, output=[]):
#     if not arr1:
#         return output + arr2
#     if not arr2:
#         return output + arr1
#     if arr1[0] < arr2[0]:
#         return merge_sorted_two_arrays(arr1[1:], arr2, output + arr1[0:1])
#     else:
#         return merge_sorted_two_arrays(arr1, arr2[1:], output + arr2[0:1])

# result = merge_sorted_two_arrays(arr1, arr2)
# print(result)

# def power(a,b):
#     if b == 0:
#         return 1,0
#     elif b ==1:
#         return a,0
#     elif b%2 == 1:
#         x,cnt = power(a,b//2)
#         return x*x*a, 2+cnt
#     elif b%2 == 0:
#         x,cnt = power(a,b//2)
#         return x*x, 1+cnt
# print(power(2,3))

# def fact(n):
#     d = {}
#     i = 2
#     while n != 1:
#         if n%i == 0:
#             if i not in d:
#                 d[i] = 0
#             d[i] += 1
#             n = n/i

#         else:
#             i += 1
#     return d
# print(fact(6))

# def target(arr,t):
#     mid = len(arr)//2
#     if t == arr[mid]:
#         return True
#     if t> arr[mid]:
#         return target(arr[mid:], t)
#     if t< mid:
#         return target(arr[:mid], t)
# print(target([3,4,5,6,3,7,8,9,4,5],5))


# def fibonacci(n, d = {}):
#     if n<=1:
#         return n
#     if n not in d:
#         d[n] = fibonacci(n-1)+ fibonacci(n-2)
#     return d[n]
# print(fibonacci(10))

from collections import defaultdict

class Session:
    def __init__(self, start, end, mid, max_count = 50):
        self.start, self.end, self.mid, self.max = start, end, mid, max_count
        self.audience = []

    def add_person(self, pid):
        if len(self.audience) < self.max:
            self.audience.asppend(pid)
            return True
        else:
            return False
        

    def count(self):
        return len(self.audience)
    
class Person:
    def __init__(self, name, telno):
        self.name , self.telno = name, telno

class Movie:
    def __init__(self, name, duration):
        self.name, self.suration = name, duration

class Kassa:
    def __init__(self):
        self.session = defaultdict(int)
        self.members = {}
        self.movies = {}


    def add_new_session(self, start, end, mid):
        self.session[len(self.session)] = Session(start, end, mid)

    def delete_session(self, sid):
        del self.session[sid]

    def sell_ticket(self,pid, sid, type):
        if self.session[sid].add_person(pid):
            print('Successfully sold the ticket')
        else:
            print('This session is full')   

    def add_movie(self, movie_name, duration):
        self.movies[len(self.movies)] = Movie(movie_name, duration)

    def add_new_member(self, name, tel_number):
        self.members[len(self.members)]= Person(name, tel_number)
    
    def total_sold_ticket(self):
        return sum([session.count() for sid, session in self.session.items()])
    
    def total_sold_ticket_for_session(self, sid):
        return self.session[sid].count()

