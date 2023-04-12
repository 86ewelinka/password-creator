#Password Generator Project
import random

# Creating a lists with alphabet, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Printing welcome to users
print("Welcome to the PyPassword Generator!\n")

# Creating wariables with user choice about how many letters,numbers and symbols want have in a password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Creating empty list to write a ready password
password=[]
letter = random.sample(letters, nr_letters)
password+=letter
number = random.sample(numbers, nr_numbers)
password+=number
symbol = random.sample(symbols, nr_symbols)
password+=symbol

# Shuffle letters, numbers and passwords to make password more safety
random.shuffle(password)
real_password = "".join(password)

# Printing created password
print(real_password)
