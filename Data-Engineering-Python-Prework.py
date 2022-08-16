# Question 1 - Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 

def hello_name(user_name):
    print("Hello " + user_name + "!")
    
hello_name('Bob')


# Question 2 - Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def odds(start, end):

    for num in range(start, end + 1):

        if num % 2 != 0:
            print(num, end = " ")
            
print(odds(0, 100))


# Question 3 - Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

print(max_num_in_list([1, 2, 8, 9]))


# Question 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):

    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)

year = 2021
print(is_leap_year(year))



# Question 5 - Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
  
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

numbers = [2, 3, 1, 4, 5]
print(is_consecutive(numbers))
