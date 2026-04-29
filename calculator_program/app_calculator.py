import sys
import os

# Utusan si Python na isama ang "parent directory" (isang level pataas) sa paghahanap ng modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from system_error_logger.custom_exceptions import CalculatorError, InvalidOperationError

class AppCalculator:

    def __init__(self):
        self.is_running = True
    def display_menu(self):
        print("\n--- Simple App Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

    def get_user_numbers(self):
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        return first_number, second_number
    def perform_calculation(self, user_choice, first_number, second_number):
        if user_choice == '1':
            return first_number + second_number
        elif user_choice == '2':
            return first_number - second_number
        elif user_choice == '3':
            return first_number * second_number
        elif user_choice == '4':
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return first_number / second_number
        else:
            raise InvalidOperationError(f"Menu choice '{user_choice}' is not valid.")
    def run_application(self):
        while self.is_running:
            self.display_menu()
            user_choice = input("Choose an operation (1/2/3/4): ")
            try:
                if user_choice not in ['1', '2', '3', '4']:
                    raise InvalidOperationError(f"User attempted to select invalid option: {user_choice}")
                first_number, second_number = self.get_user_numbers()
                calculation_result = self.perform_calculation(user_choice, first_number, second_number)
                print(f"Result: {calculation_result} maangas")
            except ValueError:
                error_logger = CalculatorError("User entered letters or symbols instead of numbers.")
                print("Error: Invalid input! Please enter numbers only. (Error Logged)")
            except ZeroDivisionError as zero_error:
                error_logger = CalculatorError(str(zero_error))
                print("Error: Math violation! You cannot divide by zero. (Error Logged)")
            except InvalidOperationError as custom_error:
                print(f"Error: Please select a valid number from the menu. (Error Logged)")
            except Exception as general_error:
                error_logger = CalculatorError(str(general_error))
                print("An unexpected error occurred. (Error Logged)")
            finally:
                retry_choice = input("\nDo you want to try again? (y/n): ")
                if retry_choice.strip().lower() != 'y':
                    self.is_running = False
                    print("Thank you!")
if __name__ == "__main__":
    calculator_instance = AppCalculator()
    calculator_instance.run_application()