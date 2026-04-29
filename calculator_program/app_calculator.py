import tkinter
import math
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from system_error_logger.custom_exceptions import CalculatorError, InvalidOperationError

class MaangasCalculatorGui:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("MAANGAS NA CALCULATOR")
        self.main_window.geometry("400x500")
        self.main_window.configure(bg="black")
        self.current_expression = ""
        self.setup_display()
        self.setup_buttons()