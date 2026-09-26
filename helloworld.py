import math
#PART 1
print(3+4) #simple caluclation
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4) 

print("Bryan") #printing string
print("Huynh")
print("United States of America")
print("I am enjoying 30 days of python")

print(type(10)) #checks data type
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(["Asabeneh","Python","Finland"]))
print(type("Bryan"))
print(type("Huynh"))
print(type("United States of America"))

print(10) #Integer number no decimal
print(2.5) #Float number with decimal
print(1+1j) #Complex letter in equation
print("Aurora") #String words
print(False) #Boolean true or false
print(["Bryan", "Aurora"]) #List ordered collection to store different data type items
print(("Bryan", "Aurora")) #Tuple ordered collection to store different data type items can't be changed
print({2,3.14,3,5}) #Set not ordered collection
print({"first name" : "Bryan", "Girlfriend's name" : "Aurora"}) #Dictionary unordered collection of key-value pairs
X1 = int(input("What is X1?")) #Asks user for inputs and saves them
Y1 = int(input("What is Y1?"))
X2 = int(input("What is X2?"))
Y2 = int(input("What is Y2?"))
Euclidean_distance = ((X2 - X1)**2 + (Y2 - Y1)**2) #Applies to user's input into the Euclidean formula
print("The distance in Euclidean space is:", math.sqrt(Euclidean_distance))
