# About functions

"""
#Creating A function

def print_name(name) :
        print("hello" + name)

print_name(" Chetali")
"""
"""
# Keyword arguments

def print_name(first, last) :
        print ("Hello" + " " + first + " " + last)

print_name("Chetali", "Bhatt") /
print_name(first = "Chetali", last = "Bhatt")
"""
"""
# Default arguments

def greet(name, msg = "Good Morning") :
       print("Hello" + " " + name + " " + msg)


greet("Mummy") / greet("Mummy", "Good night")
"""
#Return

def print_name(name) :
        return"Hello" + " " + name

print(print_name ("Disha"))


