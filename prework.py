#Question 1: Write a function to print"hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below:  def hello_name(user_name):
def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for value in range(1,100, 2):
        print(value)

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    return max(a_list)

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type 
# (true/false): def is_leap_year(a_year):
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(bool(a_year % 4 == 0 and a_year % 100 != 0))
    elif a_year % 100 == 0:
        print(bool(a_year % 400 == 0))
    else:
        print(bool(a_year % 4 == 0))