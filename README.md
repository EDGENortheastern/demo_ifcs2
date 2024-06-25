# Hello Name Application

Welcome to the Hello Name Application repository! This simple Tkinter-based GUI application allows users to enter their name, validates the input, and then displays a personalized greeting.

## The Design

### Functional Requirements

- The application shall display a window titled "Hello Name".
- The application window shall have dimensions 650x400 pixels.
- The background color of the application window shall be #d7aefc.
- The application shall display a label with the text "Enter your name in the box below".
- The application shall provide an input field for the user to enter their name.
- The application shall provide a "Submit" button. When clicked, the button shall trigger the action to output a name and a hello message.
- The application shall display the output below the submit button.

### Non-Functional Requirements

- The application shall have an intuitive and user-friendly interface.
- The application shall respond to user input within 1 second.
- The application shall handle invalid input gracefully without crashing.
- The application code shall be well-structured and documented.
- The application shall run on any system that supports Python and Tkinter.
- The application shall use appropriate font sizes and color contrasts for readability.
- The application design shall allow for easy addition of new features.

### Screen mockups

### Code Design

The code design is summarised in the class diagram below.

The `HelloName` class inherits from the `tk.Tk` class, which provides the foundational GUI window functionality. This inheritance allows `HelloName` to use and extend the methods and attributes of `tk.Tk` to create a customised application window with specific features for user interaction and input validation.

![class-diagram](HelloName.png)
