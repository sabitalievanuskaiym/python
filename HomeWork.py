import csv  

students = list(csv.reader(open("student_list.txt")))
classes = list(csv.reader(open("class_list.txt")))
credit = [credit for c_id, clas,credit in classes]
# class_name = [clas_name for  clas_name in classes ]
# st_name = [name for id,name,year,semester,c_id  in students ]

# 1)Find the average number of credits taken by all students in the dataset.
def avg_all(student_data, class_data):
    student_credits = {} 
    for st_id, name, year, semest, cl_id in student_data:
        for c_id, clas, credit in class_data:
            if name not in student_credits:
                student_credits[name] = 0
            if cl_id == c_id and name in student_credits:
                student_credits[name] += int(credit)

    total_credits = sum(student_credits.values())
    num_students = len(student_credits)

    return total_credits / num_students

average_credits = avg_all(students, classes)
print("--------------------------------------------------------------|")
print("1) Average total credits for all students-->", avg_all(students,classes))
print("--------------------------------------------------------------|")

#2) Find the median number of class credits.
def median_credit(credit):
    credit = sorted(credit)
    mid = int(len(credit)//2)
    if mid*2 == len(credit):
        return (credit[mid-1]+credit[mid])/2
    else:
        return credit[mid]
result = median_credit(credit)
print("2) Median number of class credits--> ", result)
print("--------------------------------------------------------------|")

# 3) Find the average of total credits each student had.
def avg_each_student_cr(students, classes):
    student_credits = {}
    
    for st_id, name, year, semester, cl_id in students:
        if name not in student_credits:
            student_credits[name] = []
        
        for c_id, clas, credit in classes:
            if cl_id == c_id:
                student_credits[name].append(int(credit))

    student_averages = []
    for student, credits in student_credits.items():
        if credits:
            average_credit = sum(credits) / len(credits)
            student_averages.append([student, average_credit])

    return student_averages

result = avg_each_student_cr(students, classes)
print("3) The average of total credits each student had--> ")
print(" ")
for student, average_credit in result:
    print(f"{student}-> Average Credits = {round(average_credit,3)}")
print("--------------------------------------------------------------|")

# 4) Find the variance of total credits taken by students.
def variance_total_credits(student_data, class_data):
    student_credits = {} 
    for st_id, name, year, semest, cl_id in student_data:
        for c_id, clas, credit in class_data:
            if name not in student_credits:
                student_credits[name] = 0
            if cl_id == c_id:
                student_credits[name] += int(credit)

    total_credits = list(student_credits.values())
    num_students = len(student_data)
    
    if num_students == 0:
        return 0

    avg = sum(total_credits) / len(total_credits)
    var = sum((avg - x) ** 2 for x in total_credits) / (len(total_credits))
    variance = var**0.5 
    return variance

variance = variance_total_credits(students, classes)
print("4) Variance of total credits taken by students--> ", round(variance,2))
print("--------------------------------------------------------------|")

#5) Print all classes that "David Beckham" has taken?
def student_taken_classes(arr1, arr2, student_name):
    class_dict = {c_id: clas for c_id, clas, _ in arr2}
    student_entry = [i for i in arr1 if i[1] == student_name]

    if not student_entry:
        return [] 

    student_id = student_entry[0][0] 

    student_classes = [class_dict[i[4]] for i in arr1 if i[1] == student_name]

    return student_classes

student_name = "David Beckham"
result = student_taken_classes(students, classes, student_name)

if result:
    print(f"5) All classes taken by {student_name}--> ")
    print(" ")
    for course in result:
        print(course)
else:
    print(f"{student_name} has not taken any classes.")

print("--------------------------------------------------------------|")

# 6) Find the maximum total credits taken by a student so far. And also print the name of the student.

def max_credit(arr1,arr2):
    d={}
    for st_id,name,year,semest,cl_id in arr1:
       for c_id, clas,credit in arr2:
        if name not in d:
            d[name]=0
        if cl_id==c_id and name in d:
         d[name]+=(int(credit))
    for key,val in d.items():
       if val==max(d.values()):
        return key,val
print("6) The maximum total credits taken by a student so far--> ")
print(max_credit(students,classes))

print("--------------------------------------------------------------|")

# 7) Print the classes that "LeBron James" took in "2023, Spring".
def student_taken_classes2(arr1,arr2,student,year,semester):
    student_list=[i for i in arr1 if i[1]==student and i[2]==year and i[3]==semester]
    student_classes=[]
    for i in student_list:
      for j in arr2:
        if i[4]==j[0]:
            student_classes.append(j[1])
    return student_classes
print("7) The classes that LeBron James took in 2023, Spring--> ")
student_classes = student_taken_classes2(students, classes, "LeBron James", "2023", "Spring")
for class_name in student_classes:
    print(class_name)
print("--------------------------------------------------------------|")

# 8) Return True if "Usain Bolt" attend any classes in "2024, Spring", else, False.
def student_attend(arr1,student,year,semester):
    for i in arr1:
     if i[1]==student and i[2]==year and i[3]==semester:
        return True
    else:
       return False   
print("8) Is Usain Bolt attend any classes in 2024, Spring--> ")
print(student_attend(students,"Usain Bolt","2024","Spring"))
print("--------------------------------------------------------------|")

# 9) Return True if "Maria Sharapova" has taken more classes than "Roger Federer", else, False.
def compare_credits(arr1,name1,name2):
    d={}
    for st_id,st_name,year,semester,cl_id in arr1:
        if st_name not in d:
            d[st_name]=0
        d[st_name]+=1
    return d[name1]>d[name2]
print("9) Is Maria Sharapova has taken more classes than Roger Federer--> ")
print(compare_credits(students,'Maria Sharapova','Roger Federer'))
print("--------------------------------------------------------------|")

# 11) Find the class name which is the longest of all.
def longest_name_class(arr):
    classes = [i[1] for i in arr]
    lens = [len(i[1]) for i in arr]
    longest_classes = [i for i in classes if len(i) == max(lens)]
    return longest_classes

print("11) Classes with the longest names-->")
longest_classes = longest_name_class(classes)
for class_name in longest_classes:
    print(class_name)
print("--------------------------------------------------------------|")

# 10) Find if there any students enrolled in the class "2022, Spring".
def were_any_students_date(arr1, arr2, year, semester):
    students_list = [i[1] for i in arr1 if i[2] == year and i[3] == semester]
    return students_list
year = "2022"
semester = "Spring"

enrolled_students = were_any_students_date(students, classes, year, semester)

print("10) Students who enrolled in the class in", year, semester,"-->")
print(" ")
for student in enrolled_students:
    print(student)
print("--------------------------------------------------------------|")
print(" ")
print("The code was written in a fit of perfectionism")
print(" ")
print("Thank you for your attention!")
print(" ")
