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