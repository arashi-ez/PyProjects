import math

"""strings (str)"""

# name = "kubernetes"
# res= name[0] + str(len(name[1:-1])) + name[-1]
# print(res)

# name = 'Sempiternal'
# print(name.lower())
# print(name.upper())
# print(f'not to forget the formating method {name}!')
# print(name.find("emp"))
# name_lower = name.lower()
# print(name.replace('s', 'l') , name.replace('l', 's')) #hah, here i changed both words. that means i can change to one single word each letter one by one.
# print('tern' in name )
# print(name)


""" 
operators 
order of operations

exponentiation 
multiplication or division
addition or subtruction
"""
# g = 9.81
# g_rounded = round(g)
# g_absolute = abs(-g)
# print(g_rounded)
# print(g_absolute)

"""math functions"""
# x = 17.03
# print(math.floor(x))
# print(math.sqrt(x))

"""if statement"""
# is_tasty = True
# if is_tasty:
#     print("Meal is pretty nice")
# elif is_tasty == False:
#     print("I just leave this food here")
# else :
#     print ("Meal is ok")
# print("bye")

# num = 11
# if num >= 10 and num % 2==0 :
#     print("nice")
# elif num >= 10 and num % 2 != 0:
#     print("ok")
# else:
#     print ("not ok")
    
    # Nice one
# have_money = False
# is_hungry = True
# if have_money and is_hungry:
#     print('eating')
# elif have_money == False or not is_hungry == False:
#     print('Not eating')
# else:
#     print("do not care")
    
"""Comparison Operators"""
# name = '1111111111111111111111111111111111111111111111111111111111111111'
# if len(name) < 3:
#     print('Name must be at least 3 chars')
# elif len(name)>50:
#     print('Name max: 50', f'Yours is {len(name)}')
# else:
#     print('Nice job')

"""Loops"""

'''     While Loop'''
# i = 1
# j = 5
# while i <= 5:
#     print("*" * j)
#     i+=1
#     j-=1

'''     For Loop'''

# _________________
# for item in ['Pascal', 'Snake', 'Camel']:
#     print(char) 
# _________________

# _________________
# for num in range(0, 100, 9):
#     print(num)
# _________________

# _________________
# res = 0
# price = [10, 20, 30]
# for item in price:
#     res += item
# print(res)
# _________________

'''     Nested Loop (zaloop inside zaloop)'''
# for x in range(4):
#     for y in range(3):
#         print(f'{x}, {y}')

"""Lists"""
# names = ['snake_case', 'PasclalCase', 'camelCase', 'Dash-Case', 'dot.case', 'Train-Case', 'MACRO_CASE']
# print(names[2:])

# numbers = [5,3,2,6,2,9,3]
# max = numbers[0]
# min = numbers[0]
# for num in numbers:
#     cond = num > max
#     if cond:
#         max = num
#     if num < min:
#         min = num
# print(max, min)
# nus = sorted(numbers)

"""2D Lists (matrix)"""
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[1][1])

"""List Operations"""
# numbers = [5,1,2,1,7,1,4]
# print(numbers)
# numbers.append(9)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# numbers.insert(3, 8)  
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.clear()
# print(numbers)
# print(numbers.count(1))

"""Tuples"""
# coordinates = (1,2,3)
# x,y,z = coordinates
# print(z)

"""Dictioneries"""
# customer = {
#     "name":"John Smith",
#     "age":30,
#     "is_Verified":True,
# }
# customer["birthdate"]= "Jan 1 2000"
# print(customer["birthdate"])

# message = input("$")
# words = message.split(' ')
# emojis = {
#     ":)" : "(●'◡'●)",
#     ":(" : "(T_T)",
#     "B|" : "(⌐■_■)",
#     ":|" : "(¬_¬ )",
# }
# output=""
# for word in words:
#     output += emojis.get(word, word)+ " "
# print(output)

"""Functions""" #print + def => None (if no return)
                #
# def greeting(name1, name2):
#     print(f"Hi {name1}")
#     print(f"Hello {name2}")
    
# greeting("John", name2 = "Marry")

# def square(n):
#     return n * n

# print(square(11))

"""Exceptions"""
# try: 
#     age = int(input('Age: '))    
#     print(age)
# except ZeroDivisionError:
#     print('Cannot be: 0.')
# except ValueError:
#     print('Invalid value.')

"""Class"""
# class Display:
#     def __init__(self, brand, herz: float ):
#         self.brand= brand
#         self.herz = herz
        
#     def __str__(self):
#         return f"{self.brand}'s displays frames per second is {self.herz}"

# xiaomi = Display(brand="Xiaomi", herz= 120.0)
# sony = Display(brand="Sony", herz=60.0)
# print(xiaomi)
# print(sony)

"""Inharitance"""
# class Mamal:
#     def walk(self):
#         print('can walk')


# class Dog(Mamal):
#     def bark(self):
#         print("bark")


# class Cat(Mamal):
#     def purr(self):
#         print("meow")
        
# dog = Dog()
# cat = Cat()

# dog.walk()
# dog.bark()

# cat.walk()
# cat.purr()

from youtube_tweaks import lambda_simple

print(lambda_simple(20, 25))