def even_odd(num):
  if(num%2==0):
    return True
  return False
# print(even_odd(121))

def swap_variables(num1, num2):
  num1=num1+num2
  num2=num1-num2
  num1=num1-num2
  print(num1, num2)
# swap_variables(205,101)

def check_prime(num):
  if num <= 1:
    return False
  elif num == 2:
    return True
  for i in range(2, int(num//2)+1):
    if num % i == 0:
      return False
  return True
# print(check_prime(2334))

def factorial(num):
  fact=1
  for i in range(1,num):
    fact=fact+fact*i
  return fact
# print(factorial(5))

def largest_among(num1, num2, num3):
  if(num1>num2 and num1>num3):
    return num1
  elif(num2>num1 and num2>num3):
    return num2
  else:
    return num3
# print(largest_among(10,20,3))

def sum_of_digits(num):
  sum_of=0
  for i in range(1, num+1):
    sum_of+=i
  return sum_of
# print(sum_of_digits(50))

def check_palindrome(num):
  origional = num
  reversed_num = 0
  while(num>0):
    rem= num%10
    reversed_num = reversed_num*10 + rem 
    num=num//10
  print(origional, reversed_num)

  if origional==reversed_num:
    return True
  return False
# print(check_palindrome(1291))
# check_palindrome(121)

def check_palindrome_string(str):
  return str == str[::-1]
print(check_palindrome_string("amanaplanacanalpanama"))