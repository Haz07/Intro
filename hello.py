
#name = input("Name: ")
#print("Hello "+name)
#print(f"Hello {name}")
 
# n = int(input("Number: "))
# if n > 0:
#     print("n is positive")
# elif n < 0:
#     print("n is negative")
# else:
#     print("n is zero")

# name = "Harry"
# print(name[0])
# for character in name:
#     print(character)

#names = ["Harry", "James", "Peter"]
# names.append("Tony")
# names.append("Alice")
# names.sort()
# print(names)
# for name in names:
#     print(name)

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.remove(2)
# print(s)
# print(f"The set has {len(s)} numbers")

# coordinate = (10.0, 20.0) #tuple
# print(coordinate)

# for i in [0, 1, 2, 3, 4, 5]:
#     print(i)
# for i in range(6):
#     print(i)
 
# team = {"Tony": "Avengers", "Quill": "Guardians", "Murdock":"Defenders"}
# team["Chase"] = "Runaways"
# print(team["Tony"])
# print(team)

def square(x):
    return x * x

# for i in range(10):
#     print(square(i))

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(10, 20)
# print(p.x)
# print(p.y)



#Object Orientd Concepts


# class Airline():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)    
# flight = Airline(2)

# for person in names:
#     success = flight.add_passenger(person)
#     if success:
#         print(person + "added successfully")
#     else:
#         print("No available seats")



#DECORATORS
# def announce(f):
#     def wrapper():
#         print("About to run function")
#         f()
#         print("Function completed")
#     return wrapper
# @announce
# def hello():
#     print("Hello World!!!")

# hello()

# people = [
#     {"name": "Tony", "team": "Avengers"},
#     {"name": "Luke", "team": "Defenders"},
#     {"name": "Chase", "team": "Runaways"}
# ]
# def f(person):
#     return person["name"]
# people.sort(key=f)

# #LAMBDA FUNCTIONS
# people.sort(key=lambda person: person["name"])
# print(people)

# EXCEPTIONS
# import sys

# try:
#     x = int(input("x= "))
#     y = int(input("y= "))
# except ValueError:
#     print("Invalid Input")
#     sys.exit(1)
# try:
#     result = x/y
# except ZeroDivisionError:
#     print("Can't divide by zero")
#     sys.exit(1)

# print(x/y)
