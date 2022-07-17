# # write your code here
# import random
# print("Enter the number of friends joining (including you):")
# total_friends = int(input())
#
# all_friends = {}
# if total_friends <= 0:
#     print("No one is joining for the party")
# if total_friends >= 1:
#     print("Enter the name of every friend (including you)")
#     for each in range(total_friends):
#         name = input()
#         all_friends[name.title()] = 0
#     #print(all_friends)
#
#     print("Enter the total Bill value")
#     bill = float(input())
#     print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
#     lucky = str(input())
#     if lucky =='Yes':
#         luckyperson = random.choice(list(all_friends.keys()))
#         print("{0} is the lucky one!".format(luckyperson))
#         total_friends -= 1
#         luckyperson = ''
#     else:
#         print("No one is going to be lucky")
#
#     split_bill = round((bill / total_friends), 2)
#     for friend in all_friends:
#         if friend == luckyperson:
#             luckbill = 0
#             all_friends.update({friend: luckbill})
#         else:
#             all_friends.update({friend: split_bill})
#     print(all_friends)

# side_a = int(input())
# side_b = int(input())
# side_c = int(input())
#
# if side_a == side_b == side_c:
#     print("The triangle is valid!")
# else:
#     print("The triangle is not valid!")

# num_1 = int(input())
# num_2 = int(input())
#
# if num_1 > num_2:
#     print(num_1)
#     print(num_2)
# else:
#     print(num_2)
#     print(num_1)

# place `import` statement at top of the program
# import math
#
# # don't modify this code or the variables may not be available
# x, y = map(float, input().split(' '))
# print(math.copysign(x, y))

# don't modify this code or variable `x` may not be available
# import math
# x = int(input())
#
# # use factorial() here
# print(math.factorial(x))

# place `import` statement at top of the program
#
# import random
# # don't modify this code or variable `n` may not be available
# n = int(input())
#
# # put your code here
# random.seed(n)
# print(random.randint(-100, 100))
#
# class Elf:
#     height = 1.8
#     weapon = "longbow"
#     emotional_maturity = 125
#
# class Angel:
#     color = "white"
#     feature = "wings"
#     home = "Heaven"
#
#
# class Demon:
#     color = "red"
#     feature = "horns"
#     home = "Hell"
# #
#
# my_angel = Angel()
# print(my_angel.color)
# print(my_angel.feature)
# print(my_angel.home)
#
#
# bad_demon = Demon()
# print(bad_demon.color)
# print(bad_demon.feature)
# print(bad_demon.home)

# class Wild_Animal:
#     get_food_itself = "yes"
#     live_in_nature = "yes"
#     live_with_man = "no"
#
#
# new_aminal = Wild_Animal()
# new_aminal.get_food_itself = "no"
# print(new_aminal.get_food_itself)

# class NaijaBand:
#     genre = "rock"
#     n_members = 4
#     key_instruments = ["electric guitar", "drums"]
#
#
# my_band = NaijaBand()
# print(my_band.genre)
# print(my_band.n_members)
# print(my_band.key_instruments)

#
# class Movie:
#
#     def __init__(self, title, director, year):
#         self.title = title
#         self.director = director
#         self.year = year
#
#     def getmovie(self):
#         print('"{0}" ({1}, {2})'.format(self.title, self.director, self.year))
#
#
# titanic = Movie("Titanic", "James Cameron", "1997")
# star_wars = Movie("Star Wars", "George Lucas", "1977")
# fight_club = Movie("Fight Club", "David Fincher", "1999")
#
# titanic.getmovie()
# star_wars.getmovie()
# fight_club.getmovie()

#
# class RightTriangle:
#     def __init__(self, hyp, leg_1, leg_2):
#         self.c = hyp
#         self.a = leg_1
#         self.b = leg_2
#         # calculate the area here
#         #
#         self.c_square = self.c ** 2
#         self.b_square = self.b ** 2
#         self.a_square = self.a ** 2
#
#         self.area_s = (self.a * self.b) / 2
#
#
# # triangle from the input
# input_c, input_a, input_b = [int(x) for x in input().split()]
#
# # write your code here
#
# triangle_check = RightTriangle(input_c, input_a, input_b)
# if triangle_check.c_square == (triangle_check.b_square + triangle_check.a_square):
#     print(triangle_check.area_s)
# else:
#     print("Not right")


# class Student:
#
#     def __init__(self, name, last_name, birth_year):
#         self.name = name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         # calculate the student_id here
#         self.student_id = name[0] + last_name + birth_year
#
#     def getstudentid(self):
#         print(self.student_id)
#
#
# name = str(input())
# last_name = str(input())
# birth_year = input()
#
# prepare_id = Student(name, last_name, birth_year)
# prepare_id.getstudentid()
#
# print('{0} and {2} met yesterday in {1}.'.format('Angelina Jolie', 'Paris', 'Leonardo DiCaprio'))

# nick = str(input())
# prof = str(input())
# # print("http://example.com/{nickname}/desirable/{profession}/profile".format(nickname=nick, profession=prof))
# input_word = str(input())
# word_count = len(input_word)
# print("{} has {} letters".format(input_word, word_count))
#
# # our class Ship
# class Ship:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#     # the old sail method that you need to rewrite
#     def sail(self, destination):
#         return "The {} has sailed for {}!".format(self.name, destination)
#
#
# black_pearl = Ship("Black Pearl", 800)
# ship_dest = str(input())
# final_dest = black_pearl.sail(ship_dest)
# print(final_dest)

# class Mountain:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     # create convert_height here
#     def convert_height(self):
#         foot = self.height / 0.3048
#         return foot

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     # create the method greet here
#     def greet(self):
#         print("Hello, I am {}!".format(self.name))
#
#
# new_person = Person(input())
# new_person.greet()

# class Lightbulb:
#     def __init__(self):
#         self.state = "off"
#
#     # create method change_state here
#     def change_state(self):
#         if self.state == "off":
#             self.state = "on"
#             print("Turning the light on")
#         else:
#             self.state = "off"
#             print("Turning the light off")
#
#
# class User:
#     def __init__(self, username):
#         self.username = username
#         self.friends = 0
#
#     # fix this method
#     def add_friends(self, n):
#         self.friends += n
#         print("{} now has {} friends.".format(self.username, self.friends))

# class Book:
#     def __init__(self, author, title, price, book_id):
#         self.author = author
#         self.title = title
#         self.price = price
#         self.book_id = book_id
#
#     # define the necessary method here
#     def __str__(self):
#         return "{0} by {1}. ${2}. [{3}] ".format(self.title, self.author, self.price, self.book_id)
#         # return book_details
# newbook = Book("George Orwell", "1984", 13.59, 1956789)
# print(newbook)

# class Patient:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     # create methods here
#     def __str__(self):
#         return "{0} {1}. {2}".format(self.name, self.last_name, self.age)
#     def __repr__(self):
#         return "Object of the class Patient. name: {0}, last_name: {1}, age: {2}".format(self.name, self.last_name, self.age)
#
# no_army = int(input())
# if no_army < 1:
#     print("no army")
# elif no_army < 10:
#     print("few")
# elif no_army < 50:
#     print("pack")
# elif no_army < 500:
#     print("horde")
# elif no_army < 1000:
#     print("swarm")
# else:
#     print("legion")


# a = int("5")
# print(a + 5)
# print(a * "5")
# print(ValueError)

# allError = dir(locals()['__builtins__'])
# errIndex = int(input())
# print(allError[errIndex])
#
# a = int(input())
# b = int(input())
# try:
#     result = (a / b)
# except ZeroDivisionError:
#     print("The Error!")
# else:
#     print(result)
# finally:
#     print("All completed")
#
# def exception_test():
#     a = 6
#     b = 0
#     c = a / b
#
# try:
#     exception_test()
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print(AssertionError)
# except ZeroDivisionError:
#     print(ZeroDivisionError)
# else:
#     exception_test()

# try:
#     name, surname = input().split(" ")
# except Exception:
#     print("You need to enter exactly 2 words. Try again!")
# else:
#     print("Welcome to out party ", name, surname)


# # create you classes here
# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Bird(Animal):
#     pass
#
#
# class Pigeon(Bird):
#     pass
#
#
# class Sparrow(Bird):
#     pass

# finish the function
# class Drinks:
#     pass
#
#
# class Pastry:
#     pass
#
#
# class Sweets:
#     pass
#
#
# def find_the_parent(child):
#
#     if issubclass(child, Drinks):
#         print("Drinks")
#     elif issubclass(child, Pastry):
#         print("Pastry")
#     elif issubclass(child, Sweets):
#         print("Sweets")
#
#

# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def get_perimeter(self):
#         return self.side1 + self.side2 + self.side3
#
#
# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         # finish the method
#         self.side = side
#         super().__init__(side, side, side)
#         perimeter = self.get_perimeter()
#         print(perimeter)
#
#
# EquilateralTriangle(9)

# class Robot:
#     def __init__(self, name, variety):
#         self.name = name
#         self.variety = variety
#         print("Robot")
#
#     def get_info(self):
#         return "{} is a {} robot".format(self.name, self.variety)
#
#
# class ServiceRobot(Robot):
#     def __init__(self, name):
#         self.name = name
#         self.variety = "service"
#         super().__init__(self.name, self.variety)
#
#
# chappi = ServiceRobot("Chappi")
# print(chappi.get_info())
#
# class Mammal:
#     def __init__(self):
#         self.bio_class = "mammal"
#
#     def greet(self):
#         print("I am a {}!".format(self.bio_class))
#
#
# # create class Dolphin here
# class Dolphin(Mammal):
#     def __init__(self):
#         super().__init__()
#         self.greet()
#         self.bio_class = "dolphin"
#
# dolph = Dolphin()
# dolph.greet()
#
# class Account:
#     def __init__(self, media, username, n_followers):
#         self.media = media
#         self.username = username
#         self.n_followers = n_followers
#         print("Account")
#
#
# # create the class here
# class InstagramAccount(Account):
#     def __init__(self, username, n_followers, n_following):
#         super().__init__("Instagram", username, n_followers)
#         self.n_following = n_following
#
# acc = InstagramAccount("dhihu8", 2840, 7438)

# class NotInBoundsError(Exception):
#     def __str__(self):
#         return "There is an error!"

# def check_integer(num):
#     if int(num) >= 45 <= 67:
#         return num
#     else:
#         raise NotInBoundsError
#
# def error_handling(num):
#     try:
#         numcheck = check_integer(num)
#     except NotInBoundsError as err:
#         print(err)
#     else:
#         print(numcheck)

# error_handling(60)

# class NegativeSumError(Exception):
#     pass
#
#
# def sum_with_exceptions(a, b):
#     c = a + b
#     try:
#         if c < 0:
#             raise NegativeSumError
#     except NegativeSumError:
#         return NegativeSumError
#     else:
#         return (c)
#
# output = sum_with_exceptions(-1,-1)
# print(output)
# class WordError (Exception):
#     pass
#
# def check_w_letter(word):
#     for w in word:
#         if w == 'w':
#             raise WordError
#     return word
#
# print(check_w_letter("Net"))


# class NotWordError(Exception):
#     def __init__(self, word):
#         self.message = word + " is not a word, sorry!"
#         super().__init__(self.message)
#
#
# def check_word(word):
#     if '0' in word:
#         raise NotWordError(word)
#     else:
#         return word
#
# def error_handling(word):
#     try:
#         word_check = check_word(word)
#     except NotWordError as err:
#         print(err)
#     else:
#         print(word_check)

# def discounts(x, y):
#     pd = ((x - y) / x) * 100
#     print(pd)
#     try:
#         assert pd > 50.0, "Discount is Less than 50%"
#     except AssertionError as err:
#         print(err)
#     else:
#         retrun "I will buy it!"
#
#
# discounts(100, 75)

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# d = x / y
# assert d > 5, "Your number is less than 5 or equal to 5!"
# assert d < 14, "Your number is more than 14 or equal to 14!"
# print("Your number is", d)

# def even(x):
#     ev = x % 2
#     assert ev == 0, 'Not Even Number'
#     return x
#
#
# print(even(6))
#
# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(s)

# n = int(input())
#
# n_init = 2
#
# while n_init < n:
#     print(n_init)
# #     n_init += 2
#
# i = 0
# a = 'a'
# while i < 8:
#     a *= 2
#     i += 1
# print(a)


# counter = 0
# max_value = 0
# while counter < 10:
#     counter = counter + 1
#     max_value = max_value + counter
#     print("max value :", max_value)
#     if max_value > 15:
#         break
#     counter = counter + 1
#     print("Counter", counter)
#
# i = 10
# while i > 0:
#     i -= 2
#     if i % 2 == 1:
#         break
#     else:
#         i -= 2
# else:
#     print("End.")
#     print(i)

# scores = input().split()
# # put your python code here
# i = 0
# c = 0
# gameover = 0
# for x in scores:
#     while i < 3:
#         if x == 'C':
#             c += 1
#             break
#         if x == 'I':
#             i += 1
#             break
#     else:
#         print("Game over")
#         print(c)
#         gameover = 1
#         break
# if gameover != 1:
#     print("You won")
#     print(c)


# import random
#
#
# random.seed(3)
# # call the function here
# alpha=0.9
# beta=0.1
# print(random.betavariate(alpha, beta))
#
# import random
#
#
# # work with this variable
# n = int(input())
#
# random.seed(n)
# print(random.uniform(0, 1))


class City:
    all_cities = []

    def __init__(self, name, year):
        self.name = name
        self.year = year

ny = City("New York", 1624)
ny.all_cities.append("New York")

stockholm = City("Stockholm", 1187)
stockholm.all_cities = ["Stockholm"]
stockholm.all_cities.append("Stockholm")
print(stockholm.all_cities)
print(ny.all_cities)
print(City.all_cities)