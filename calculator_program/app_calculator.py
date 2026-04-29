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