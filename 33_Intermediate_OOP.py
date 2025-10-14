#Question_6
# class Book:
#     def __init__(self,title,author,price,name):
#         self.title = title
#         self.author = author
#         self.price = price 
#         self.name = name
#         print(f"Name of Book: {self.name}")
#         print(f"Title: {self.title}")
#         print(f"Author : {self.author}")
#         print(f"Price : {self.price}")
        
        
# name = input("Name of book: ").capitalize()
# title = input(f"What's title of {name} book: ")
# author = input(f"Who is the author of {name} book: ")
# price = int(input("How much: "))
# pustak = Book(name,title, author, price)

#Question_7
# class Employee:
#     # old_company_name = "Google"      #class attribute
#     # TechCorp = "Software Engineer"
#     # new = input("new company name: ")
#     def __init__(self,name , salary, old_company_name,TechCorp,new_company,contact ):   #Constroctor
#         self.name = name 
#         self.salary = salary
#         self.old = old_company_name
#         self.tech = TechCorp
#         self.new = new_company
#         self.conts = contact
#     def info(self):         #Instance Attribute
#         print("---------New Employee Information-------")
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Working On: {self.old} ")
#         print(f"TechCorp: {self.tech}")
#         print(f"Now joining: {self.new}")
#         print(f"Contact Number: {self.conts}")
#         print("----------------------------")

# name = input("Enter your Name: ")
# old_company_name =  input("Enter your old company name: ")
# TechCorp =  input("In which field you were work: ")
# new_company =  input("Enter your new company name where you need to work : ")
# salary = int(input("Enter your Salary: "))
# contact = (input("Enter your Contact Number: "))

# emp = Employee(name, salary, old_company_name,TechCorp,new_company,contact)
# emp.info()

#Queation_8
# # class Circle:
# #     def __init__(self,radius):
# #         self.r = radius
# #     def get_area(self):
# #         area= (22/7)* (self.r)**2
# #         print(f"The area of circle is {area: .2f}")
# #     def get_circumfrance(self):
# #         c = 2*(22/7)*(self.r)
# #         print(f"Circumfrance of circle is {c: .2f}")
# # sphere = Circle(5)
# # sphere.get_area()
# # sphere.get_circumfrance()
        
# #Question_9 
# class Laptop:
#     def __init__(self,model,processor,ram, rom, screen, backlit,finger,price):
#         self.model = model
#         self.Processor = processor
#         self.RAM = ram
#         self.ROM = rom
#         self.Screen = screen
#         self.Backlit = backlit
#         self.Finger = finger
#         self.price = price
#     def info(self):
#         print("------HERE New Laptops With Exclusive Price-------")
#         print(f" Model: {self.model}")
#         print(f"Processor: {self.Processor}")
#         print(f"RAM: {self.RAM}")
#         print(f" ROM: {self.ROM}") 
#         print(f"SCREEN: {self.Screen}") 
#         print(f"Bakelit: {self.Backlit}") 
#         print(f" Finger: {self.Finger}")
#         print(f"Price: {self.price}")

# # model = input("Model: ")
# # processor = input("Processor:")
# # ram = input("RAM: ")
# # rom = input("ROM: ")
# # screen = input("SCREeN: ")
# # backlit = input("Backlit: ")
# # finger = input("Finger: ")
# # price = int(input("Price: "))
# hardware = Laptop(model,processor,ram, rom, screen, backlit,finger,price)

#Question_10 
# class Temperature:
#     def __init__(self, celsius, fahrenheit):
#         self.C = celsius
#         self.F = fahrenheit
#     def get_Celsius(self):
#         celsius = (self.F - 32)* 5/9
#         print(f"{self.F}°F to {self.C}°C: {celsius:.2f}°C")
#     def get_Fahrenheit(self):
#         Fahrenheit = (9/5 * self.C)+32
#         print(f" {self.C}°C to {self.F}°F : {Fahrenheit: .2f}°F")
# temp = Temperature(40,212)
# temp.get_Celsius()  #Temperature.get_Celsius(temp)
# temp.get_Fahrenheit()  #Temperature.get_Fahrenheit(temp) 