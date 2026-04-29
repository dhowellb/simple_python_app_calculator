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
    def setup_buttons(self):
        self.buttons_frame = tkinter.Frame(self.main_window, bg="black")
        self.buttons_frame.pack(expand=True, fill="both")
        button_grid_layout = [
            ["C", "√", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "^", "="]
        ]
        for row_index, row_content in enumerate(button_grid_layout):
            self.buttons_frame.rowconfigure(row_index, weight=1)
            for column_index, button_text in enumerate(row_content):
                self.buttons_frame.columnconfigure(column_index, weight=1)
                action_command = lambda current_text=button_text: self.handle_button_click(current_text)
                calculator_button = tkinter.Button(
                    self.buttons_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bg="white",
                    fg="black",
                    command=action_command
                )
                calculator_button.grid(row=row_index, column=column_index, sticky="nsew", padx=2, pady=2)