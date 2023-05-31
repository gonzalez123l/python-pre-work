# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been dfined as below.
def hello_name(user_name):
  print("hello " + user_name + "!")
  pass

hello_name('Leo')

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
     """a function that prints the odd numbers from 1-100 and returns nothing"""
       
     for num in range(100):

       if num % 2== 1:  # num%2!=0 will get the same result
           print(num)
    
first_odds() 
# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
  a_list.sort()
  return a_list[-1]
  pass  
print(max_num_in_list([1,2,3,4,5]))

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisble by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
  if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
    return True
  else:
    return False
print(is_leap_year(2023))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
#  """ a function to check to see if all numbers in list are consecutive numbers """
 a_list_sorted=sorted(a_list)
 for i in range(1,len(a_list)):   
        if  a_list_sorted[i] ==  a_list_sorted[i-1] + 1:
            return True
        else:
            return False

print(is_consecutive(a_list=[10, 12, 13, 15, 16]))
print(is_consecutive(a_list=[10, 11, 12, 13, 14, 15, 16]))