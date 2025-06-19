# Task 1: Define the Printer Class with a Single Method
class Printer:
    def print_message(self, message,times=1):
        for _ in range(times):
            print(message)
# Task 2: Use the Printer Class
if __name__ == "__main__":
    printer = Printer()

    printer.print_message("Hello")
    printer.print_message("Hello",3)
    

