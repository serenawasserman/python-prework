from selectors import EpollSelector


def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")
#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing:
# def first_odds():
def first_odds():
    for value in range(1,100, 2):
        print(value)
first_odds()

def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list([1, 2, 3, 4, 5]))

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print("Leap year")
    elif a_year % 100 == 0:
        if a_year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Not a leap year")
is_leap_year(2000)