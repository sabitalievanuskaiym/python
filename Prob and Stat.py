# ------------------------------------------------=======================
# 11.09.23
# Probability and Stat
# Avrage

# arr = [2000,350,360,700,10000,20000,100000,300,400]
# def median (arr):
#     arr = sorted(arr)
#     x = int (len(arr))
#     if x *2 == len(arr):
#       a = arr[x]+arr[x-1]
#       return( a/2)
#     else:
#        return (arr[x])

# def median (arr):
#     arr = sorted(arr)
#     mid = int(len(arr)/2)
#     if mid *2 == len(arr):
#         return(arr[mid]+arr[mid-1])/2
#     else:
#         return arr[mid]
# print (median(arr))

# =======================================================================
# 18.09.23
# prob and stat
# формула кредита

# m = [0]
# n = 120
# p = 100
# k = 0.01
# for i in range(n):
#     x = p +m[-1]*(1+k)
#     m.append(int(x))
# print(m)

# n = 45*12
# m = [0]*n
# p = 100
# k = 0.01
# for i in range(n):
#    m[i]= p +m[i-1]*(1+k)
# print(m)

# =======================================================================
# 20.09.23/PROBABILITY
# игровая кость
# from random import randint
# arr = [0]*19
# n= 10000
# for i in range (n):
#     d1 = randint(1,6)
#     d2 = randint(1,6)
#     d3 = randint(1,6)
#     d = d1+d2+d3
#     arr[d]+=1
# for i in arr[3:]:
#  print(i/n)

# from random import randint
# arr = [0]*13
# varr = [0,0,1,2,3,4,5,6,5,4,3,2,1]
# n= 100
# for i in range (n):
#     d1 = randint(1,6)
#     d2 = randint(1,6)
#     d = d1+d2
#     arr[d]+=1
# for i,j in zip(arr,varr):
#  print(i/n,j/36)

# from random import randint
# arr = [0]*13
# varr = [0,0,1,2,3,4,5,6,5,4,3,2,1]
# n= 1000
# for i in range (n):
#     d1 = randint(1,6)
#     d2 = randint(1,6)
#     d = d1+d2
#     arr[d]+=1
# for i,j in zip(arr,varr):
#  print((i/n-j/36)*100)

# =======================================================================
# 27.09.23/ probability ans stat
# n = 5
# def factorial(n):
#     x = 1
#     for i in range(x,n+1):
#         # print(f"{x}*{i}")
#         x = i*x
#     return x
# print (factorial(n))


# permitation- перестановка
# s = "a,b,c"
# def permitation(s,i):
#      if i == len(s):
#         print("".join(s))
#      for a in range(i,len(s)):
#          s[a], s[i] = s[i],s[a]
#          permitation(s,i+1)
#          s[a],s[i]==s[i],s[a]


# s = "ABC"
# print(list(s))
# permitation(list(s),0)


# from itertools import permutations
# s = "123"
# for i in permutations(list(s)):
#     print(i)

# s = "quiz"
# def bek (s,i):
#   if i ==len(s):
#     x = "".join (s)
#     if "ui" not in x and "iu" not in x:
#      print(x)

#   for a in range (i,len(s)):
#        s[a], s[i] = s[i],s[a]
#        bek(s, i+1)
#     #    s[a],s[i]==s[i],s[a]

# # s = 'quiz'
# bek(list(s),0)

# =====================================================================
# 02.10.23/ PROBABILITY
# COMBINATION
# arr = [0,1,2,3,4]
# n=0
# combination / 10
# for i in range(0,5):
#     for j in range(i+1,5):
#         for k in range(j+1,5):
#             n+=1
#             print(i,j,k)
# print(n)
# all combinations /125
# for i in range(0,5):
#     for j in range(0,5):
#         for k in range(0,5):
#             n+=1
#             print(i,j,k)
# print(n)
# permitation/60
# for i in range(0,5):
#     for j in range(0,5):
#         for k in range(0,5):
#             if not(i==j or i==k or j==k):
#               n+=1
#               print(i,j,k)
# print(n)

# ==================================================================
#Sshas code/REPETITION FOR TEST
#Находит вероятность количество слов по длине
# words = []
# for line in open("text.txt"):
#     for word in line.split():
#        words.append(word.strip(";,. "))
# lengths = [0] * 20

# for word in words:
#     lengths[len(word)] += 1
   
# count = sum(lengths)

# n = int(input("Длина = "))

# probability = round(lengths[n] * 100 / count, 2)
# print(f"вероятность слова длинной {n} = {probability}%, всего таких слов {lengths[n]}")

# ------------------------------------------------------
#KREDIT/ INTEREST
#10000 сом под 12% годовых на 20 лет
# k = 12  # процент
# n = 20  # год
# p = 10000  # сколько денег вложено
# for i in range(1, n + 1):
#     print(f"Баланс = {p} + {k}%")
#     # p = int(p + p * (k / 100))
#     p = int(p * (1 + k / 100))
#     print(f"Баланс = {p}")
# print(p)


# def compound_interest(p, n, k):
#     return p * (1 + k) ** n


# def save_compound_month_interest(p, n, k):
#     m = 0
#     for i in range(n):
#         m = int(p + m * (1 + k))
    # return m

# print(save_compound_month_interest(100, 12*10, 0.01))
# print(compound_interest(10000, 20, 0.12))
# ---------------------------------------------------

# #PERMUTATION- перестановка
# def permutations(s, i=0):
#     if i == len(s):
#         print(s)
#     for x in range(i, len(s)):
#         s[x], s[i] = s[i], s[x]
#         permutations(s, i + 1)
#         # s[x], s[i] = s[i], s[x]
# permutations([1, 3, 2, 4, 5, 6])


#permitation- перестановка
# def permutation(s,i=0):
#      if i == len(s):
#         print("".join(s))
#      for a in range(i,len(s)):
#          s[a], s[i] = s[i],s[a]
#          permutation(s,i+1)
#         #  s[a],s[i]==s[i],s[a]
# s = "ABC"
# permutation(list(s))


# ИГРОВАЯ КОСТЬ
# out = [0] * 13
# for i in range(1, 7):
#     for j in range(1, 7):
#         print(f"{i}+{j}={i+j}")
#         out[i + j] = out[i + j] + 1
#     print(out)
# count = sum(out)
# print(f"сумма {count}")
# for i in range(len(out)):
#     print(f"{i} выпал {out[i]} раз, вероятность {i} = {int(out[i]*100/count)}%")



# out = [0] * 13
# for i in range(1, 7):
#     for j in range(1, 7):
#         out[i + j] = out[i + j] + 1
# print(out)
# count = sum(out)
# print(f"сумма {count}")
# p = int(input("Leng - "))
# probability = round(out[p]*100/count)
# print(f"Prob {p} = {probability}%, IN ALL - {out[p]}")

# ===============================================
# ПРИМЕР ЭКЗА ПО ПРОБЭБИЛИТИ


# import csv
# brands = []
# prices = []
# months = [0] * 12

# for date, brand, price in csv.reader(open("prices.txt")):
#     price = int(price.strip(" $"))
#     brand = brand.strip()
#     months[int(date.split("-")[1]) - 1] += price
#     if brand in brands:
#         prices[brands.index(brand)].append(price)
#     else:
#         brands.append(brand) 
#         prices.append([price]) 
# medians = []
# for brand_prices in prices:
#     brand_prices = sorted(brand_prices)
#     ln = len(brand_prices)
#     if ln % 2 == 0:
#         medians.append((brand_prices[(ln // 2)] + brand_prices[ln // 2 - 1]) // 2)
#     else:
#         medians.append(brand_prices[ln // 2])

# out = [f"{brand}: ${price}" for brand, price in zip(brands, medians)]

# months = [[sales, month + 1] for month, sales in enumerate(months)]
# biggest_sales = max(months)

# out.append(
#     f"The biggest sales were in {biggest_sales[1]} month, profit: ${biggest_sales[0]}"
# )

# open("result.txt", "w").write("\n".join(out))


# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr)//2
#     if mid*2 == len(arr):
#         return (arr[mid]+arr[mid-1])/2
#     else:
#         return arr[mid]
# import csv
# brands = csv.reader(open("brands.txt"))
# prices = csv.reader(open("prices.txt"))
# brands_name = [[_ids, name]for _ids, name in brands]
# amount = [[_ids, price] for date, _ids, price in prices]
# res = [[]for i in range(len(brands_name))]
# for _id, price in amount:
#     res[int(_id)].append(int(price.strip(" $")))
# for s, a in zip(brands_name, res):
#     print(s[1],a, median(a))

# import csv

# def median(arr):
#     mid = len(arr) // 2
#     if mid * 2 == len(arr):
#         return (arr[mid] + arr[mid - 1]) / 2
#     else:
#         return arr[mid]
# brands = csv.reader(open("brands.txt"))
# prices = csv.reader(open("prices.txt"))
# brands_name = [[_ids, name] for _ids, name in brands]
# month = [0] * 5
# amount = [[date, brand_id, price] for date, brand_id, price in prices]
# result = [[] for i in range(len(brands_name))]
# for date, ids, cash in amount:
#     month[(int(date.split("-")[1]) - 1)] += int(cash.strip("$"))
#     result[int(ids)].append(int(cash.strip("$")))
# for (a,b,) in zip(brands_name,result,):
#     print(f"Name:{a[1]},{b}, median:{median(b)}")
# print(f"Месяц где было больше всего продаж:{month.index(max(month))+1} Сумма:{max(month)}")

# import csv

# def get_month(num):
#     match num:
#         case 1:
#             return "January"
#         case 2:
#             return "February"
#         case 3:
#             return "March"
#         case 4:
#             return "April"
#         case 5:
#             return "May"
#         case 6:
#             return "June"
#         case 7:
#             return "July"
#         case 8:
#             return "August"
#         case 9:
#             return "September"
#         case 10:
#             return "October"
#         case 11:
#             return "November"
#         case 12:
#             return "December"

# def median (arr):
#     arr = sorted(arr)
#     mid = len(arr)//2
#     if mid*2 == len(arr)/2:
#         return (arr[mid] + arr[mid-1])
#     else:
#         return arr[mid]

# reader_brands = csv.reader(open("brands.txt"))
# reader_prices = csv.reader(open("prices.txt"))

# brands = [(id, name) for id, name in reader_brands]
# amount = [(date, id, price) for date, id, price in reader_prices]

# month = [0]*12
# result = [[] for i in range (len(brands))]

# for date, id, cash in amount:
#     month[(int(date.split("-")[1])-1)]+= int(cash.strip("$"))
#     result[int(id)].append(int(cash.strip("$")))

# for a, b in zip (brands, result):
#     print(f"Name:{a[1]},{b}, median:{median(b)} avg: {sum(b)/len(b)}")
# print(f"Месяц где было больше всего продаж:{get_month(month.index(max(month))+1)}")
# print(f"Сумма: {max(month)}")


# import csv

# reader_product = csv.reader(open("product.txt"))
# reader_price = csv.reader(open("price.txt"))

# product = [[id, name ]for id, name in reader_product]
# amount = [price for id, price in reader_price]
# count = 0
# arr =[]
# for i, name1 in enumerate(amount):
#     for j, name2 in enumerate(amount):
#         for k, name3 in enumerate(amount):
#             if int(name1)+int(name2)+int(name3)==50 and i<j<k:
#                 count+=1
#                 arr.append([i,j,k])
                
# x = []
# for id, product in product:
#    for i in arr:
#      for j in i:
#         if j == int(id):
#            x.append(product)
# print(x)
# print(count)

# import csv

# product = []
# for id, name, price in csv.reader(open("product.txt")):
#     product.append([int(price), name])
# out = []
# for v1 in range(len(product)):
#     for v2 in range (v1+1,len(product)):
#         for v3 in range (v2+1,len(product)):
#             if product[v1][0]+product[v2][0]+product[v3][0]==50:
#                 out.append([v1,v2,v3])
# open("result.txt","w").write("\n".join([f"{product[v1][1]},{product[v2][1]},{product[v3][1]}"for v1,v2,v3 in out]))


# =====================================================================

# import csv


# def avg_time(arr):
#     if len(arr):
#         s = 0
#         for hour, minute in arr:
#             s += int(hour) * 60 + int(minute)
#         avg = s / len(arr)

#         hours = int(avg / 60)
#         mins = int(avg % 60)
#         hours = hours if hours > 9 else "0" + str(hours)
#         mins = mins if mins > 9 else "0" + str(mins)
#         return f"{hours}:{mins}"


# def late_count(arr, time):
#     count = 0
#     if len(arr):
#         hour, minute = time.split(":")
#         threshold = int(hour) * 60 + int(minute)
#         for hour, minute in arr:
#             t = hour * 60 + minute
#             if t > threshold:
#                 count += 1
#         return count


# def who_was_late(arr, time, input_date):
#     print("LATE STUDENTS", input_date)
#     hour, minute = time.split(":")
#     threshold = int(hour) * 60 + int(minute)
#     for name, date, time in arr:
#         hour, minute = time.split(":")
#         t = int(hour) * 60 + int(minute)
#         if input_date == date and t > threshold:
#             print(name, time)
#     print("")


# def get_attend_dates(arr, student_name):
#     attended_dates = set()
#     for name, date, time in arr:
#         if name == student_name:
#             attended_dates.add(date)
#     return attended_dates


# def filter_table(arr, student_name):
#     sub_arr = []
#     attended_dates = set()
#     print(f"{student_name} stats:")
#     for name, date, time in arr:
#         if name == student_name:
#             hour, minute = time.split(":")
#             sub_arr.append((int(hour), int(minute)))
#             attended_dates.add(date)
#     missed_dates = dates - attended_dates
#     if missed_dates:
#         print("missed dates:", ", ".join(missed_dates))
#     else:
#         print("no missed dates")
#     print(f"attendance: {int((len(attended_dates) / len(dates)) * 100)}%")
#     print("avg time:", avg_time(sub_arr))
#     print("was late", late_count(sub_arr, "10:00"), "times")
#     print("")


# def general_stats(students, timetable, dates):
#     print("GENERAL STUDENT STATS")
#     print("average time:",avg_time([time.split(":") for name, date, time in timetable]),)
#     who_lates_the_most(students, timetable)
#     who_attends_the_most(students, timetable, dates)
#     highest_and_lowest_attendance(timetable, dates)


# def who_was_in(timetable, qtime, qdate):
#     qtimes = [int(i) for i in qtime.split(":")]
#     count = 0
#     for name, date, time in timetable:
#         if qdate == date:
#             time = [int(i) for i in time.split(":")]
#             if time[0] >= qtimes[0] and time[1] >= qtimes[1]:
#                 count += 1
#     print(f"{qdate} at {qtime} {count} students were in the class")


# def who_lates_the_most(students, timetable):
#     late_count = [0 for name in students]
#     for name, date, time in timetable:
#         time = [int(i) for i in time.split(":")]
#         if time[0] >= 10 and time[1] > 0:
#             late_count[students.index(name)] += 1
#     mx = max(zip(late_count, students))
#     print(f"{mx[1]} was late most often, he/she was late {mx[0]} times")


# def who_attends_the_most(students, timetable, dates):
#     wasnt = [0 for name in students]
#     for student in students:
#         attended = get_attend_dates(timetable, student)
#         for idate in dates:
#             if idate not in attended:
#                 wasnt[students.index(student)] += 1
#     wasnt = min([[count, name] for count, name in zip(wasnt, students)])
#     print(f"{wasnt[1]} attends the most, he/she missed {wasnt[0]} classes")


# def highest_and_lowest_attendance(timetable, dates):
#     dates = list(dates)
#     attendance = [0 for i in dates]
#     for name, date, time in timetable:
#         attendance[dates.index(date)] += 1
#         # print(attendance, dates)
#     attended = [[attd, date] for attd, date in zip(attendance, dates)]
#     mx = max(attended)
#     mn = min(attended)
#     print(f"Highest attendent was {mx[1]}, {mx[0]} students was attended")
#     print(f"Lowest attendent was {mn[1]}, {mn[0]} students was attended")


# def get_stats(students, timetable, dates):
#     for student_name in students:
#         filter_table(timetable, student_name)

#     who_was_late(timetable, "10:05", "10-10-2023")

#     general_stats(students, timetable, dates)

#     who_was_in(timetable, "10:08", "10-11-2023")


# timetable = [[name, date, time] for i, name, date, time in csv.reader(open("university.txt"))]
# students = [name for i, name in csv.reader(open("student_list.txt"))]
# dates = set([date for name, date, time in timetable])

# get_stats(students, timetable, dates)

# ==========================================================================================
# prob/ 12.10.23
# Sashas version


# import csv
# from datetime import datetime

# now = [datetime.now().day, datetime.now().month, datetime.now().year]

# def general_stat(purch: list):
#     if len(purch):
#         print("GENERAL STATISTICS:")
#         prices = [int(i[9].strip("$")) for i in purch]
#         print(f"Median car price: ${median(prices)}")
#         colors = [i[8] for i in purch]
#         print(f"The most popular color is {most(colors)[1]}")
#         models = [i[6] for i in purch]
#         print(f"The least sold car model is {least(models)[1]}")
#         years = [int(i[7]) for i in purch]
#         print(f"Average car model year is {average(years)}")
#         ages = [[int(j) for j in i[3].split(".")] for i in purch]
#         print(f"Median customer age is {median_age(ages)}")
#         names = get_full_names(purch)
#         print(f"The most expensive car was purchased by {max(zip(prices, names))[1]}")
#         print("")
#         print(
#             f"List of car models purchased by customers older than 30: {','.join(list_models_purch_by_older(list(zip(ages, models))))}"
#         )
#         print("")


# def list_models_purch_by_older(sales: list, age: int = 30) -> list:
#     if len(sales):
#         out = set()
#         for birthdate, model in sales:
#             if get_age(birthdate) > age:
#                 out.add(model)
#         return out

# def get_full_names(purch: list) -> list:
#     if len(purch):
#         return [" ".join([i[0], i[1]]) for i in purch]

# def median(arr: list) -> int:
#     if len(arr):
#         arr = sorted(arr)
#         if len(arr) % 2:
#             return arr[len(arr) // 2]
#         return (len(arr // 2) + len(arr // 2 - 1)) / 2


# def get_count(arr: list) -> list:
#     if len(arr):
#         st = [[0, i] for i in set(arr)]
#         # print(st)
#         for i in st:
#             i[0] = arr.count(i[1])
#         # print(st)
#         return st


# def most(arr: list) -> list:
#     if len(arr):
#         return max(get_count(arr))


# def least(arr: list) -> list:
#     if len(arr):
#         return min(get_count(arr))


# def average(arr: list) -> int:
#     if len(arr):
#         return sum(arr) // len(arr)


# def get_age(birth: list, date: list = now) -> int:
#     if len(birth) == 3 and len(date) == 3:
#         age = date[2] - birth[2]
#         age -= 1 if date[1] < birth[1] else 0
#         age -= 1 if date[1] == birth[1] and date[0] < birth[0] else 0
#         return age


# def median_age(birth_dates: list) -> int:
#     if len(birth_dates):
#         ages = []
#         for i in birth_dates:
#             ages.append(get_age(i))
#         return median(ages)

# def sales_in(sales: list, state: str = "Colorado", city: str = "Denver"):
#     if len(sales) and len(state) and len(city):
#         states = [i[4] for i in sales]
#         cities = [i[5] for i in sales]
#         if state in states and city in cities:
#             print(f"Customers in {state}, {city}:")
#             names = get_full_names(sales)
#             count = 0
#             for name, s, c in zip(names, states, cities):
#                 if s == state and c == city:
#                     count += 1
#                     print(f"{count}. {name}")
#             print(f"Total {count} customers")
#         else:
#             print(f"There were no sales in {state}, {city}")
#         print("")

# def states_stats(sales: list):
#     if len(sales):
#         print("STATISTICS BY STATE:")
#         print("\n".join([f"{i[0]} sales in {i[1]}" for i in get_count([i[4] for i in sales])]))

# def print_stats(file: str = "car_dealership.txt"):
#     if len(file):
#         purchases = [i[1:] for i in csv.reader(open(file))]
#         general_stat(purchases)
#         sales_in(purchases)
#         states_stats(purchases)


# print_stats()

# ======================================================================================
# Saadats version

# import csv
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

# ==================================================================
# prob/ 18.10.23
# # VARIANCE
# x = [17,17,19,23,19,18,26,17,17,18,19]
# y = [65,55,30,27,25,35,47,30]

# avg = sum(x)/len(x)
# val = sum([(avg-i)**2 for i in x])/len(x)
# va = sum([(avg-i)**2 for i in y])/len(y)
# st = va**0.5
# std = val**0.5
# print(std)
# print(st)

# ANAMALY DETECTION\
# x = [17,17,19,23,19,18,26,17,17,18,19]
# y = [65,55,30,27,25,35,47,30]
# def is_anamaly(i,x,std,c):
#     if i>(x+std*c):
#         i<(x-std*c):
#         return True:
#     else:
#         return False

#
# -------------------------------------

# arr1 = [17, 17, 19, 18, 23, 19, 18, 26, 17, 17, 18, 16, 20, 21]
# arr2 = [30, 47, 35, 27, 30, 55, 65]

# def calculate_avg(data):
#     return sum(data) / len(data)

# avg_arr1 = calculate_avg(arr1)
# avg_arr2 = calculate_avg(arr2)

# def calculate_variance(data):
#     avg = calculate_avg(data)
#     variance = sum((avg - x) ** 2 for x in data) / (len(data))
#     return variance

# var_arr1 = calculate_variance(arr1)**0.5
# var_arr2 = calculate_variance(arr2)**0.5

# are_equal = avg_arr1 == var_arr1 and avg_arr2 == var_arr2

# print("Average of arr1:", int(avg_arr1))
# print("Average of arr2:", int(avg_arr2))
# print("Variance of arr1:", int(var_arr1))
# print("Variance of arr2:", int(var_arr2))
# print("AVGRAGE VS VARIANCE:", are_equal)
          
# ----------------------------------------------
# arr1 = [17, 17, 19, 18, 23, 19, 18, 26, 17, 17, 18, 16, 20, 21]
# arr2 = [30, 47, 35, 27, 30, 55, 65]

# avg_arr1 = sum(arr1)/len(arr1)
# avg_arr2 = sum(arr2)/len(arr2)

# var1 = sum((avg_arr1 - x) ** 2 for x in arr1) / (len(arr1))
# var2 = sum((avg_arr2 - i) ** 2 for i in arr2) / (len(arr2))
# variance_arr1 = var1**0.5 
# variance_arr2 = var2**0.5 

# def compare(a,b):
#     if avg_arr1 == variance_arr1 and avg_arr2 == variance_arr2:
#         return True
#     return False

# print("EQUAL OR NOT - ", compare(arr1,arr2))
# print("AVG_ARR1 - " , int(avg_arr1))
# print("AVG_ARR1 - " , int(avg_arr2))
# print("VARIANCE ARR1 - ", int(variance_arr1))
# print("VARIANCE ARR2 - ", int(variance_arr2))

# -----------------------------------------------
# Saadats version
# arr1 = [17, 17, 19, 18, 23, 19, 18, 26, 17, 17, 18, 16, 20, 21]
# arr2 = [30, 47, 35, 27, 30, 55, 65]

# def avg(arr):
#     return sum(arr)/len(arr)

# def variance(arr):
#     for i in arr:
#         sum= (avg(arr)-i)**2
#     # return sum
#     return (sum/len(arr))**0.5

# def compare(a,b):
#     if avg(a)== variance(a) and avg(b) == variance(b):
#         return True
#     return False
# print(compare(arr1,arr2))\

# ====================================================
# 15.10.23/STAT
# KREDIT
# m = 11800
# count = 0
# b = 120000

# i = (30/100)/12
# while b >= 0:
#     b =b*(i+1)- m 
#     count +=1
# print(count)

# ====================================================================
# 20.11.23/PROB
# CORRELATION COEFFICIEN
# arr1 = [1000000,900000,1500000,1300000,1200000]
# arr2 = [10000,9000,15000,13000,12000]

# def r(arr1,arr2):
#     avg_a, avg_b = sum(arr1)/len(arr1), sum(arr2)/len(arr2)
#     up,down1, down2 = 0,0,0
#     for a,b in zip(arr1, arr2):
#         up+=(a- avg_a)*(b-avg_b)
#         down1+=(a - avg_a)**2
#         down2+=(b- avg_b)**2
#     return up/(down1*down2)**0.5

# print(r(arr1,arr2))


# def find_divisors(number):
#     divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors

# number_to_check = 56
# result = find_divisors(number_to_check)

# print(f"Делители числа {number_to_check}: {result}")

# ==============================================================
# 22.11.23/ PS

# from random import randint
# from matplotlib import pyplot as plt

# N = 20
# arr = [0] * (N + 1)
# for i in range(10000):
#     s = sum([randint(0, 1) for j in range(20)])
#     arr[s] += 1
# print(arr)
# plt.plot(list(range(N + 1)), arr)
# plt.show()
# ----------------------------------------------
# NORMAL DISTRIBUTION
# from random import randint
# from matplotlib import pyplot as plt
# import math

# N = 200
# temp = []
# arr = [0] * (N + 1)
# for i in range(100000):
#     s = sum([randint(0, 1) for j in range(N)])
#     temp.append(s)
#     arr[s] += 1
# print(arr)

# avg = sum(temp) / len(temp)
# var = sum([(avg - i) ** 2 for i in temp]) ** 0.5 / N

# arr2 = [0] * N
# for x in range(N):
#     arr2[x] = 1 / (var * (2 * math.pi)) * math.exp2(-1 / 2 * ((x - avg) / var) ** 2)


# # # plt.plot(arr, color="red")
# plt.plot(arr2, color="green")
# plt.show()


# ---------------------------------------------------------------------------------

# GRAFT
# def r(a, b):
#     a_cap = avg(a)
#     b_cap = avg(b)
#     ln = min(len(a), len(b))
#     up = sum([(a_ - a_cap) * (b_ - b_cap) for a_, b_ in zip(a, b)])
#     down_a = sum([((a_ - a_cap) ** 2) for a_ in a])
#     down_b = sum([((b_ - b_cap) ** 2) for b_ in b])

#     r = up / (down_a * down_b) ** 0.5

#     return r


# # def r(arr1, arr2):
# #     a_cap, b_cap = sum(arr1) / len(arr1), sum(arr2) / len(arr2)
# #     up, down1, down2 = 0, 0, 0

# #     for a, b in zip(arr1, arr2):
# #         up += (a - a_cap) * (b - b_cap)
# #         down1 += (a - a_cap) ** 2
# #         down2 += (b - b_cap) ** 2

# #     return up / (down1 * down2) ** 0.5


# def avg(arr1):
#     return sum(arr1) / len(arr1)


# 1.1

# print(r([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


# ===========================================================================
# 13.12.23/ PS
# balance =100000
# m = 8000
# interest = 22
# count = 0
# a = 0
# m_i = interest/12/100
# while  balance >= 0:
#     balance += balance*m_i
#     a+=  balance *m_i
#     balance -= m
#     count +=1
#     print(count, round(balance *m_i),round(m-balance*m_i), round(balance))
# print(count,round(a))

# # ------------------------------------

# balance =100000
# interest = 22
# month_q = 12

# def month_payment(balance, interest, month_q):
#     return(balance + balance * interest / 100)/ month_q
# print(month_payment(balance, interest, month_q))

# -----------------------------------
arr = [1,3,5,6,4,3,3,9]
mid = len(arr)//2
def recursice_median(arr, mid):
    n = arr[-1]
    left_arr = []
    right_arr = []
    for i in arr[:-1]:
        if i<=n:
            left_arr.append(i)
        if i > n:
            right_arr.append(i)
    if len(left_arr) == mid:
        return n
    if len(left_arr)> mid :
        return recursice_median(left_arr,mid)
    else:
        return recursice_median(right_arr, mid- len(left_arr)-1)
print(recursice_median(arr, mid)) 

def median(arr):
    mid = len(arr)//2
    if mid*2 == len(arr):
        m1 = recursice_median(arr,mid)
        m2 = recursice_median(arr,mid+1)
    else:
        return recursice_median
    
print(median(arr))
