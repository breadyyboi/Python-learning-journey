bryan_age = 15 #Variable with a assigned value
zhang_age = 14  #integers
bryanHuynh_age = 15
kevin_age = 12
current_year = 2026

canada = "Canada" #string
dallas = "Dallas"

is_married = True #boolean
is_true = False 
is_light_on = True

boyfriend, girlfriend = "Bryan", "Aurora" #Multiple variables assigned to multiple values
print(boyfriend) #You can selectiely choose the variable you want
print(girlfriend)

print(type(bryan_age)) #Checks the data type of the variable
print(type(canada))
print(type(is_married))
print(len("Bryan")) #Checks the length of the variable
print(len("Aurora"))
print(abs(len("Bryan") - len("Aurora"))) #Finds the difference in length between the two names

number_one, number_two = 5, 4 
total = number_one + number_two #Operations with the vairables declared
diff = number_two - number_one
product = number_two * number_one 
division = number_one / number_two 
remainder = number_two % number_one #remainder
exponent = number_one ** number_two #exponent
floor_division = number_one // number_two #rounds down

radius =int(input("What is the radius of the circle?"))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print("The area of the circle is " + str(area_of_circle) + " and the circumference is " + str(circum_of_circle))

user_name = str(input("What is your name?")) #Asks user for input and saves it as a string
user_lastName = str(input("What is your last name?"))
user_country = str(input("What country are you from?"))
user_age = int(input("What is your age?"))
user_info = [user_name, user_lastName, user_country, user_age] #Saves the user's input into a list
help('keywords')