import sys
import os

# Utusan si Python na isama ang "parent directory" (isang level pataas) sa paghahanap ng modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from system_error_logger.custom_exceptions import CalculatorError, InvalidOperationError

class AppCalculator:

    def __init__(self):
        self.is_running = True