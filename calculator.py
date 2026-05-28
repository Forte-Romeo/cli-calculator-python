# Building a CLI calculator on Python based on the concepts learnt: Variables, Loops, Functions

#Defining all functions for this project (addition, subtraction, multiplication, division, exponent, and modulus)
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

     if b == 0:
          print("Invalid: Division by zero is not allowed.")
          return None
     return a / b

# Define a function to find exponent of a number
def exponent(a, b):
     return a ** b

# Define a function to find the remainder/modulus of two numbers
def modulus(a, b):
     return a % b

     
#Main dashboard function to handle user inputs and call required functions
def main():

     #Choosing your prefered operation
     operations = {
          '1': add,
          '2': subtract,
          '3': multiply,
          '4': divide,
          '5': exponent,
          '6': modulus
     }

     #Main Menu
     while True:
          print("\n===== CLI CALCULATOR =====")
          print("\n===== Menu: =====")
          print("1. Add")
          print("2. Subtract")
          print("3. Multiply")
          print("4. Divide")
          print("5. Exponent")
          print("6. Modulus")
          print("7. Exit")

          choice = input("Enter your choice: ")

          # EXIT
          if choice == '7':
               print("Exiting Calculator.")
               break

          # INVALID CHOICE
          if choice not in operations:
               print("Invalid choice.")
               continue
          
          #First number input
          while True:
               try:
                    num1 = float(input("Enter your first number: "))
                    break
               except ValueError:
                    print("Error: Invalid input. Please enter a valid number")

          # CONTINUOUS CALCULATION LOOP
          while True:

               #Second number input
               while True:
                    try:
                         num2 = float(input("Enter your second number: "))
                         break
                    except ValueError:
                         print("Error: Invalid input. Please enter a valid number")

               # Select function directly
               operation = operations[choice]

               # Calculate result
               result = operation(num1, num2)

               # Handle Failed Calculations
               if result is None:
                    print("Calculation failed.")
               else:
                    print(f"\nResult: {result}")

                    # Store result
                    num1 = result

               # Ask user if they want to continue
               continue_choice = input("\nDo you want to continue calculating with this result? (yes/no): ").lower()

               if continue_choice != "yes":
                    print("Returning to main menu...")
                    break
               
               # Ask for new operation
               print("\nChoose next operation:")
               print("1. Add")
               print("2. Subtract")
               print("3. Multiply")
               print("4. Divide")
               print("5. Exponent")
               print("6. Modulus")
          
               while True:
                    choice = input("Enter your choice: ")
                    if choice in operations:
                         break
                    else:
                         print("Invalid choice. Please select a valid option.")


# Run Program
if __name__ == "__main__":
     main()