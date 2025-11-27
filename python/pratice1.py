# Write a function that takes a string a and a number n as arguments. Return the nth character of a.

def get_char(a, b):
   # complete function here...
   return a[b-1]
      
print(get_char('abcd', 1)) # expected output: 'a'
print(get_char('zyxbwpl', 5)) # expected output: 'w'
print(get_char('gfedcba', 3)) # expected output: 'e


# Write a function count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

vowels = 'aeiou'
 
def count_vowels(str):
   # complete function here...
   vowels = ["e", "o", "u", "a", "i"]
   count = 0
   for char in str:
        for vowel in vowels:
            if char == vowel:
                count += 1
   return count
   """
   # another way:
   def count_vowels(str):
   count = 0
   for char in str:
      if char in vowels:
         count += 1
   return count
   """
print(count_vowels('hello world')) # expected output: 3
print(count_vowels('python')) # expected output: 1



# Write a function count_occurrences that takes a tuple and an element. The function should return the number of times the element appears in the tuple.
def count_occurrences(tpl, element):
    # complete function here...
    count = 0
    for sth in tpl:
        if sth == element:
            count += 1
    return count



print(count_occurrences((1, 2, 3, 2, 2, 4), 2))
# expected output: 3
print(count_occurrences((3, 3, 3, 3, 3, 4), 3))
# expected output: 5
print(count_occurrences(('a', 'b', 'c', 'd', 'c', 'b'), 'b'))
# expected output: 2



# Write a function remove_duplicates that takes a string and returns a new string with duplicate characters removed, keeping the first occurrence of each character.
def remove_duplicates(str):
    # complete function here...
    letters = []
    for char in str:
        if char in letters:
            continue
        else: 
            letters.append(char)
            str = ''.join(letters)
    return str

print(remove_duplicates('banana')) # expected output: 'ban'
print(remove_duplicates('vegetable')) # expected output: 'vegtabl'
print(remove_duplicates('difficulty')) # expected output: 'difculty'
 



# In the code below, we have dictionaries storing data about different people. Write a function can_vote that receives such a dictionary as input and returns True if the person has reached the minimum voting age min_age and False otherwise.
min_age = 18
 
alice = { 'age': 18, 'gender': 'female'}
bob = { 'age': 40, 'gender': 'male'}
charlotte = { 'age': 17, 'gender': 'female'}
 
# define function can_vote here...
def can_vote(name):
    if name["age"] > 17:
        return True
    else: 
        return False

 
print(can_vote(alice)) # expected output: True
print(can_vote(bob)) # expected output: True
print(can_vote(charlotte)) # expected output: False


# Write a function average_score that receives a list of grades of a particular student and returns the average grade.

alice = [85, 92, 78]
bob = [70, 88, 91]
charlie = [95, 91, 42]
 
# define function "average_score" here ...
def average_score(name):
    average = int(sum(name) / len(name))
    return average
 
print(average_score(alice)) # expected output: 85
print(average_score(bob)) # expected output: 83
print(average_score(charlie)) # expected output: 76
 





# Write a function that receives a dictionary where each key is a student's name and the corresponding value is a list of grades for that student. The function should return the total average grade for the entire class.
class_a = {
    'Alice': [85, 92, 78],
    'Bob': [70, 88, 91],
    'Charlie': [95, 91, 88],
    'Alex': [50, 66, 54]
}
class_b = {
    'David': [88, 77, 92],
    'Eve': [90, 85, 79],
    'Frank': [65, 72, 63],
    'Grace': [80, 82, 87]
}
 
# define function "average_score" here ...
def average_score(some_class):
    grades = []
    for person in some_class:
        grade = sum(some_class[person])/len(some_class[person])
        grades.append(grade)
    average = int(sum(grades)/len(grades))
    return average

"""
# another solution: 

def average_score(students):
   sum_averages = 0
   for student in students.values():
     sum_averages += (sum(student) / len(student))
   return sum_averages / len(students)
"""
 
print(average_score(class_a)) # expected output: 79
print(average_score(class_b)) # expected output: 80
 


# Write a function count_down that takes a positive integer start as input and returns a list of integers counting down from start to 0.

def count_down(start):
    # complete function here...
    count = start
    count_list = []
    count_list.append(start)
    while count > 0:
        count -= 1
        count_list.append(count)
    return count_list
 
 
print(count_down(3)) # expected output: [3,2,1,0]
print(count_down(5)) # expected output: [5,4,3,2,1,0]



# Write a function sum_natural_numbers that takes a positive integer n and returns the sum of all natural numbers from 1 to n.

def sum_natural_numbers(n):
    # complete function here...
    nums = []
    for num in range(1, n+1):
        nums.append(num)
    sum_nums = sum(nums)
    return sum_nums
   
print(sum_natural_numbers(5)) # expected output: 15
print(sum_natural_numbers(7)) # expected output: 28
print(sum_natural_numbers(77)) # expected output: 3003
 


# Write a function next_divisible that takes two integers, x and y, as arguments. 
# The function should check if x is divisible by y. If it is, return x. 
# If not, return the next higher natural number that is divisible by y.
# Hint: remember the modulo operator %? You could use it to check if a number is divisible by y.

def next_divisible(x, y):
   # complete function here...
   if x % y == 0:
       return x
   else:
       num = x
       while not num % y == 0:
           num += 1
       else: 
           return num
       
 
print(next_divisible(1, 23)) # expected output: 23
print(next_divisible(7, 3)) # expected output: 9
print(next_divisible(15, 7)) # expected output: 21
print(next_divisible(77, 76)) # expected output: 152
 


# Write a function minutes_between that calculates the number of minutes between two 
# given times of the day. The function should take two strings representing the times 
# in the format 'HH:MM' and return the total number of minutes between them.
# Hint: you may want to extract the hours and minutes from the given strings. 
# To transform a string like '12' to the integer 12, you can use the int('12') function.

def minutes_between(earlier, later):

    # complete function here...
    hour_earlier = int(earlier[0] + earlier[1])
    hour_e_to_min = hour_earlier * 60
    min_earlier = int(earlier[-2] + earlier[-1])
    all_min_earlier = hour_e_to_min + min_earlier

    hour_later = int(later[0] + later[1])
    hour_l_to_min = hour_later * 60
    min_later = int(later[-2] + later[-1])
    all_min_later = hour_l_to_min + min_later

    difference = all_min_later - all_min_earlier
    return difference

print(minutes_between('10:15', '11:16')) # expected output: 61
print(minutes_between('08:00', '19:47')) # expected output: 707


text = 'Hello World'
print(text.replace('l',''))

# if you do this like that: 
# text.replace('l','')
# print(text) <- the original text will be printed, so you have to assign to a var