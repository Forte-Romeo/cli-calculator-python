# Building a CLI calculator on Python based on the concepts learnt: Variables, Loops, Functions

#Defining all functions for this project (addition, subtraction, multiplication, division, and exponent)
# Define a function to add two numbers
def add(a, b):
     return a + b

# Define a function to subtract two numbers
def subtract(a, b):
     return a - b

# Define a function to multiply two numbers
def multiply(a, b):
     return a * b

# Define a function to divide two numbers (with error handling)
def divide(a, b):
     try:
          result = a / b
     except ZeroDivisionError:
          print("Invalid: Division by zero is not allowed.")
          return None
     return result

# Define a function to find exponent of a number
def exponent(a, b):
     return a ** b

#Main dashboard function to handle user inputs and call required functions
def main():
     #Main Menu
     while True:
          print("\nCalculator Menu:")
          print("1. Add")
          print("2. Subtract")
          print("3. Multiply")
          print("4. Divide")
          print("5. Exponent")
          print("6. Exit")

          choice = input("Enter your choice: ")

          if choice == '6':
               print("Exiting Calculator.")
               break
          
          #User inputs
          while True:
               try:
                    num1 = float(input("Enter your first number: "))
                    break
               except ValueError:
                    print("Error: Invalid input. Please enter a valid number")

          while True:
               try:
                    num2 = float(input("Enter your second number: "))
                    break
               except ValueError:
                    print("Error: Invalid input. Please enter a valid number")

          #Perform the selected operation and displaying the result
          if choice == '1':
               result = add(num1, num2)
          elif choice == '2':
               result = subtract(num1, num2)
          elif choice == '3':
               result = multiply(num1, num2)
          elif choice == '4':
               result = divide(num1, num2)
          elif choice == '5':
               result = exponent(num1, num2)

          if result is not None:
               print(f"Result: {result}")

if __name__ == "__main__":
     main()