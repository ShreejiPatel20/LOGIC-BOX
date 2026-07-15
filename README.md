# Interactive Personal Data Collector

## Project Overview

The Interactive Personal Data Collector is a simple Python console application that gathers basic personal information from a user and demonstrates core programming concepts. It highlights variables, user input, type conversion, formatted output, and the use of Python's `datetime` module.

After the user provides their details, the program:
- Displays the entered values.
- Shows the data type of each value.
- Prints the memory address of each variable using `id()`.
- Estimates the user's birth year from their age.

---

## Repository Contents

- `Submission_01.py` — the main Python script.
- `README.md` — project documentation.
- `output.csv` — sample output file.
- `output.pdf` — exported sample output.
- `.gitignore` — repository ignore rules.

---

## Features

The program collects:
- Name
- Age
- Height
- Favourite number

It demonstrates:
- `str`, `int`, and `float` data types
- `input()` for user interaction
- Type conversion with `int()` and `float()`
- Formatted output using f-strings
- Built-in functions such as `type()` and `id()`
- The `datetime` module

---

## How to Run

1. Open a terminal in the project directory.
2. Run the script with:

```bash
python Submission_01.py
```

Or, if your system uses `python3`:

```bash
python3 Submission_01.py
```

---

## Sample Output

```text
Welcome to the Interactive Personal Data Collector!

Please enter your name: John
Please enter your age: 20
Please enter your height: 5.9
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: John (type: <class 'str'>, Memory Address: 140242319854320)
Age: 20 (type: <class 'int'>, Memory Address: 140242319821584)
Height: 5.9 (type: <class 'float'>, Memory Address: 140242319856912)
Favourite Number: 7 (type: <class 'int'>, Memory Address: 140242319821168)

Your birth year is approximately: 2006 (based on your age of 20)

Thank you for using the Personal Data Collector. Goodbye!
```

> Note: Memory addresses returned by `id()` will vary between runs.

---

## Concepts Demonstrated

- Variables
- User input
- Type casting
- Data types
- Formatted strings
- Built-in functions: `type()` and `id()`
- Module import with `datetime`
- Basic arithmetic operations

---

## Possible Improvements

- Add input validation
- Handle invalid input with `try` and `except`
- Validate age and height ranges
- Save collected data to a CSV or text file
- Support multiple entries
- Add a graphical user interface
