import math
def area_circle(radius):
    if radius<0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def area_rectangle(length,width):
    if length <0 or width < 0:
        raise ValueError("Length and width no negative")
    return length*width

def area_triangle(base,height):
    if base <0 or height <0:
        raise ValueError("base and height wont be zero")
    return (base*height)/2

# Task 2: Main function to handle user input and calculate area
def main():
    try:
        print("select the shape to calculate")
        print("1. circle")
        print("2. rectangle")
        print("3. Triangle")
        choice=int(input("enter your choice (1/2/3):"))
        if choice==1:
            radius=float(input("Enter the radius of the circle:"))
            area=area_circle(radius)
            print(f"the area of circel is :{area:2f}")
        elif choice ==2:
            length=float(input("enter the length of the ractangle:"))
            width=float(input("enter the width of the ractangle:"))
            area=area_rectangle(length,width)
            print(f"area of rectangle {area:2f} ")
        elif choice==3:
            base=float(input("enter the base of the triangle:"))
            height=float(input("enter the height of the triangle :"))
            area=area_triangle(base,height)
            print(f"the are of triangle is : {area:2f}")
        else:
            print("invalid choice please select a valid option .")
    except ValueError as e:
        print(f"Error : {e}")
    except Exception as e:
        print(f"an unexpected error occurd :{e}")

if __name__ == "__main__":
    main()