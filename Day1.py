print('hello world')
print('Day 1 - Python Print function')
print("The function is declared like this:")
print("print('what to print')")
print("Hello Stella\nMy names is....")  #anything after n is
print('Hello,','my names is Stella')
print("Hello,"+" my name is Stella")

print(" ")
print(" ")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the + sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

''''Python input Function
'''

Tell_me_your_name = input("What is your name? ")
print("Hello", Tell_me_your_name)
# print("Hellooo" + input("What is your name? "))

print(len(Tell_me_your_name))

'''Code that switches the values of  two variables
'''
# a = 3
# b = 5
# y = a store the value of a in a new variable y
# a = b change to b
# b = y change b to y which is stored the original value of a
# print(a)
# print(b)

a = input("a: ")
b = input("b: ")
y = a
a = b
b = y
print("a: " + a)
print("b: " + b)


'''Project 1:
1. Create a greeting for your program.

2. Ask the user for the city that they grew up in.

3. Ask the user for the name of a pet.

4. Combine the name of their city and pet and show them their band name.

5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
'''

print("Hello, welcome to the band Generator!")
name_of_city = input("Which city did you grow up in?: ")
pet_name = input("What is your pet's name?: ")
band_name = "The name of your band is"
print(band_name,name_of_city,pet_name)