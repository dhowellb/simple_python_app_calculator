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
    def setup_display(self):
        self.display_variable = tkinter.StringVar()
        self.display_variable.set("0")
        self.display_label = tkinter.Label(
            self.main_window,
            textvariable=self.display_variable,
            font=("Arial", 24, "bold"),
            bg="black",
            fg="white",
            anchor="e",
            padx=20,
            pady=20
        )
        self.display_label.pack(expand=True, fill="both")