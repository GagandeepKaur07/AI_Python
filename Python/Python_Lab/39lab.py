# Task 1: Implementation of Local Scope
def local_scope_example():
    x =10
    print("local variable x:",x)
local_scope_example()

# Task 2: Implementation of Enclosing Scope (Nested Functions)
def outer_function():
    x=10

    def inner_function():
        print("Enclosing variable x from inner function",x)

    inner_function()
outer_function()

# Task 3: Implementation of Global Scope
x=10
def global_scope_example():
    print("Global variable x: ",x)
global_scope_example()
print("global variable x outside function :", x)

# Task 4 : Implementation of Modifying Global Variables 
x=10
def modify_global():
    global x
    x = 20
modify_global()
print("Global variable x after modification",x)