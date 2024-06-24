import tkinter as tk
from tkinter import messagebox  # 🔴 Important: Importing the messagebox feature from tkinter

class HelloName(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello Name")  # 📛 Setting the window title
        self.geometry("650x400")  # 📐 Setting the window size and position
        self.bg_color = "#d7aefc"  # 🎨 Setting the background color
        self.font_size = 20  # 🖊️ Setting the font size
        self.config(bg=self.bg_color)  # 🖌️ Applying the background color

        # 👇 Creating the instruction text for the user
        self.lbl_instruction = tk.Label(self,
                                        text="Enter your name in the box below",
                                        bg=self.bg_color,
                                        font=('Arial', self.font_size))
        self.lbl_instruction.pack(pady=50)  # 📦 Packing the instruction label on the screen

        # 👇 Creating the input box for the user's name
        self.input_box = tk.Entry(self, font=('Arial', self.font_size))
        self.input_box.pack(pady=10)  # 📦 Packing the input box on the screen

        # 👇 Creating the submit button
        self.btn_submit = tk.Button(self,
                                    text="Submit",
                                    command=self.get_name,
                                    fg="dark green",
                                    font=('Arial', self.font_size))
        self.btn_submit.pack(pady=10)  # 📦 Packing the button on the screen

        # 👇 Creating the output box
        self.output_box = tk.Label(self,
                                    text="",
                                    bg=self.bg_color,
                                    font=('Arial', self.font_size))
        self.output_box.pack(pady=10)  # 📦 Packing the output box on the screen

    def get_name(self):
        my_name = self.input_box.get().strip()  # Retrieving the name input
        self.display_output(my_name)

    def display_output(self, name):
        # 👇 Checking for name presence and length
        if not self.presence_check(name):
            self.error_handler("Name cannot be left blank")
            return "Presence check failed"
        elif not self.length_check(name):
            self.error_handler("The name should be between 4 and 19 characters")
            return "Length check failed"
        else:
            decorated_name = self.decorate_name(name)  # 🌺 Decorating the name
            self.output_box.config(text=decorated_name)
            return "OK"
            
    def decorate_name(self, name):
        return f"Hello, {name.title()}!"  # 🌺 Returning the decorated name

    def error_handler(self, error_message):
        try:
            messagebox.showerror("Error", error_message)  # ❗ Displaying the error message
        except Exception as e:
            print(f"Something went wrong: {e}")
    
    def presence_check(self, name):
        return bool(name)  # 🤔 Checking if name is present
    
    def length_check(self, name):
        return 2 < len(name) <= 20  # 📏 Checking the name's length

if __name__ == "__main__":
    app = HelloName()
    app.mainloop()
