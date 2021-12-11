# velocity1 = 70
# velocity2 = 100
# time = 2

# distance = (velocity1 + velocity2) * time

# print(distance)

# velocity3 = 60
# velocity4 = 90
# time2 = 3

# distance2 = (velocity3 + velocity4) * time2
# print(distance2)


# def calculateDistance(v1, v2, t):
#     return (v1 + v2) * t

# vel1 = int(input('Enter velocity 1: '))
# vel2 = int(input('Enter velocity 2: '))
# time = int(input('Enter time: '))

# print(calculateDistance(vel1, vel2, time))


# def calculateSquare(x):
#     return x * x

# print(calculateSquare(10))


# def calcPow(base, exp):
#     return base ** exp

# print(calcPow(3, 4))

# def reverseList(list):
#     return list[::-1]

# print(reverseList([1,2,3]))

# def calcSum(a, b, *c):
#     acc = 0
#     for num in c:
#         acc += num

#     return a + b + acc

# print(calcSum(2,3))

# import math

# print(math.pow(2,3))

# def sayHello(name, surname):
#     print(f'Hi, {name} {surname}')

# sayHello(surname='Khakimbekov', name='Elbek')

# mentor = {
#     "name": "Elbek",
#     "surname": 'Khakimbekov',
#     "age": 22,
#     "isMarried": False
# }

# for key in mentor:
#     print(key, mentor[key])


# print(mentor.get('abc'))


# def abc(**args):
#     acc = 0
#     for key in args:
#         acc += args[key]
#     return acc

# print(abc(a = 4, b = 6, c = 10))


# def min(a, b):
#     if a < b: return a
#     elif a == b: return 'Equal'
#     else: return b

# print(min(10, 20))
# print(min(10, 5))
# print(min(10, 10))

# print(eval('1/2'))

# signs = {
#     'add': '+',
#     'subtract': '-',
#     'multiply': '*',
#     'divide': '/'
# }

# def calculator(a, b, action):
#     return eval(f'{a}{signs.get(action)}{b}')


# print(calculator('1', '3', 'add'))
# print(calculator('10', '6', 'subtract'))
# print(calculator('10', '6', 'multiply'))
# print(calculator('10', '6', 'divide'))
# print(calculator('10', '6', 'divider'))