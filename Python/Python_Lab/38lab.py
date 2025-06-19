# Task 1 :: Implementation of Positional Arguments
def greet(name,age):
    print(f"Hello {name}, you are {age} year.")
greet("Raman",30)

# Task 2 : Implementation of Keyword Arguments
def greet(name,age):
    print(f"Hello {name}, you are {age} years old .")
greet(age=30,name="Maria")

# Task 3: Implementation of Default Arguments
def greet(name,age=25):
    print(f"Hello {name}, you are {age} years old .")
greet("Ramar")
greet("Maria",30)

# Task 4: Implementation of Variable-Length Arguments
def print_number(*args):
    for number in args:
        print(number)
print_number(1,2,3,4,5)

# Task 5: Implementation of Keyword Variable-Length Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="kumar",profession="Engineer")
print_info(country="India",population=1.4e9,capital="New Delhi")

# Task 6: Implementation of Mixing Different Argument Types
def mixed_arguments(a, b=2, *args, **kwargs):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"args:{args}")
    print(f"kwargs:{kwargs}")
mixed_arguments(1,3,4,5,x=10,y=20)