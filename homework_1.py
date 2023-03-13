# # Task1
#
# name = input('What is your name?')
# surname = input('Input your surname: ')
# age = input('Input your age: ')
# email = input('Input your e-mail: ')
# password = input('Create your password: ')
#
#
# print('{} {} your login is {}, password is{}'.format(name, surname, email, password))

# Task2

# seconds = int(input('Input cont of seconds: '))
#
# hours = seconds // 3600
# minutes = seconds // 60

# Task3

# n = input('Input number: ')
#
# double_n = n + n
# triple_n = n + n + n
#
# result = int(n) + int(double_n) + int(triple_n)
# print(result)

# Task4

# earnings = int(input('Yuor earnings: '))
# costs = int(input('Your costs: '))
#
# profitability = earnings - costs
# profitability_coef = profitability / 1000
#
# if profitability > costs:
# print('You have a profitability! Its equal {}'.format(profitability_coef))
# num_of_emploee = int(input('Input number of emploees: '))
# coef_emploee = num_of_emploee * profitability_coef
# print(coef_emploee)
# elif profitability == costs:
# print('Your result is break even')
# else:
# print('You have not prifitabilyty')

# Task5

# num = int(input('Input num'))
# if 99 < num <= 999:
# summa = num // 100 + num % 100 // 10 + num % 10
# print(summa)
# else: print('It is not correct num, input num in range 100-999')
# 124 / 100 = 1,24
# 124 % 100 = 24 // 10
# 124 % 10 = 4

#Task6

# ticket_number = int(input('Input num of your ticket: '))
#
# left_part = ticket_number // 1000
# right_part = ticket_number % 1000
#
# if left_part == right_part:
# print('It is a happy ticket!')
# else:
# print('it is a ticket like a ticket, nothing special')

# Task5

# total = int(input('Input number of crains: '))
#
# katy_crains = total // 100 * 75
# mihael = katy_crains / 4
# andrew = mihael
#
# print(katy_crains, mihael, andrew)
#
# total = int(input('Input number of crains: '))
#
# mihael = total // 6
# katy = mihael * 4
# andrew = mihael
#
# print(katy, mihael, andrew)

# Task 8

m = int(input('Input m: '))
n = int(input('Input n: '))
k = int(input('Input k: '))

pl = m * n
if k % m == 0 and k < pl or k % n == 0 and k < pl:
    print('Yes')
else:
    print('No')