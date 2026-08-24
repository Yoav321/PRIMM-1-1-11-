"""
Description of program here
First Last - Month Year
"""

def main() -> None:
    #takes the first user input
    num1: float = float(input("Enter a number: "))
    #takes the second user input 
    num2: float = float(input("Enter another number: "))
    #Stores the two inputs into a variable
    result: float = num1 // num2
    #prints the two numbers and the variable
    print(f"{num1} // {num2} = {result}")

if __name__ == "__main__":
  main()
