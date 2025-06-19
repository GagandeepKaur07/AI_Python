# Task 1: Define the Base Class Animal
class Animal:
    def speak(self):
        return "Animal Speaks"
class Dog (Animal):
    def speak(self):
        return "woof!"
class Cat (Animal):
    def speak(self):
        return "Meow"
def make_animal_speak(animal):
    print(animal.speak())


# Task 3: Use the Classes and Methods
if __name__ == "__main__":
    dog=Dog()
    cat=Cat()
    make_animal_speak(dog)
    make_animal_speak(cat)
