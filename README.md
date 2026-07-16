Here’s a complete README.md file for your Python project.

# Interactive Personal Data Collector
##  Project Overview
The **Interactive Personal Data Collector** is a simple Python program that collects basic personal information from the user through the console. It demonstrates the use of Python variables, data types, user input, type conversion, formatted output, and the built-in `datetime` module.
After collecting the information, the program:
- Displays the entered data.
- Shows the data type of each variable.
- Displays the memory address of each stored variable using the `id()` function.
- Calculates the user's approximate birth year based on the current year and entered age.
---
## Features
- Collects user's:
  - Name
  - Age
  - Height
  - Favourite Number
- Uses appropriate Python data types:
  - `str`
  - `int`
  - `float`
- Displays:
  - User-entered values
  - Variable data types
  - Memory addresses
- Automatically calculates approximate birth year.
- Uses the current system year through the `datetime` module.

---
##  Project Structure
```
.
├── Submission_01.py
└── README.md
```
---
##  How to Run
### Step 1: Clone or Download the Project
Download the project files or clone the repository.
### Step 2: Open Terminal
Navigate to the project directory.
```bash
cd project_folder
```
### Step 3: Run the Program
```bash
python Submission_01.py
```
or
```bash
python3 Submission_01.py
```
---
## Sample Output
```
Welcome to the Interactive Personal Data Collector!
Please enter your name: John
Please enter your age: 20
Please enter your height: 5.9
Please enter your favourite number: 7
Thank you! Here is the information we collected:
Name: John (type: <class 'str'> Memory Address: 140242319854320)
Age: 20 (type: <class 'int'> Memory Address: 140242319821584)
Height: 5.9 (type: <class 'float'> Memory Address: 140242319856912)
Favourite Number: 7 (type: <class 'int'> Memory Address: 140242319821168)
Your birth year is approximately: 2006 (based on your age of 20)
Thank you for using the Personal Data Collector. Goodbye!
```
> **Note:** Memory addresses (`id()`) will be different each time the program is executed.
---
##  Concepts Demonstrated
- Variables
- User Input (`input()`)
- Type Casting (`int()`, `float()`)
- Data Types
- Formatted Strings (f-strings)
- Python Built-in Functions
- `type()`
- `id()`
- Importing Modules
- Working with Dates (`datetime`)
- Basic Arithmetic Operations
---
##  Program Workflow
1. Display a welcome message.
2. Ask the user to enter:
   - Name
   - Age
   - Height
   - Favourite Number
3. Store the inputs in variables.
4. Display the entered information.
5. Show the data type of each variable.
6. Show the memory address of each variable.
7. Calculate the approximate birth year.
8. Display a thank-you message.