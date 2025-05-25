#assignment 3

while True:
    try:
      num1 = float(input('Enter a number: '))
      num2 = float(input('Enter the divisor for the number:'))
    
      result = num1/ num2
      print(f'The answer is :  {num1} / {num2} = {result} ')
      break

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a valid number !")
    except ValueError:
        print("Error: Invalid input. Please enter a number")
        