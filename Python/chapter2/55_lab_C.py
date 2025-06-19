#Task 1: Define Two Classes with the Same Method fly() and define function
class Bird:
    def fly(self):
        return "Flying high"
class Airplane:
    def fly(self):
        return "Flying through the skies"
def let_it_fly(entity):
    print(entity.fly())

#Task 2: Create Objects and Demonstrate Duck Typing
if __name__ == "__main__":
    bird=Bird()
    airplane=Airplane()

    let_it_fly(bird)
    let_it_fly(airplane)

