class Exception_My:
  def calculate(self, a, b):
    try:
        result = a / b
        return f"The result of {a} divided by {b} is {result}."
    # except ZeroDivisionError:
    #     return "Error: Division by zero is not allowed."
    # except TypeError:
    #     return "Error: Invalid input type. Please provide numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    finally:
        print("Execution completed.")


  def invalid_input(self):
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            return self.calculate(a, b)
        except ValueError:
            raise TypeError("Invalid input type. Please provide numbers.")   

exception = Exception_My()
# print(exception.calculate(10, 2))  # Valid case
# print(exception.calculate(10, 0))  # Division by zero
print(exception.invalid_input())  # Invalid input type