# Interactive Personal Data Collector

## Project Overview

The **Interactive Personal Data Collector** is a simple Python console program that collects basic personal details from the user. It demonstrates Python fundamentals such as variables, user input, type conversion, formatted output, and working with the `datetime` module.

After collecting the information, the program:
- Displays the entered values.
- Shows the data type of each value.
- Displays each variable's memory address using `id()`.
- Estimates the user's birth year using the current year and entered age.

---

## Repository Contents

- `Submission_01.py` — the main submission script.
- `README.md` — project documentation.
- `output.csv` — sample output file.
- `output.pdf` — sample output file.
- `.gitignore` — ignore rules for this repository.

---

## Features

- Collects:
  - Name
  - Age
  - Height
  - Favourite Number
- Demonstrates:
  - `str`, `int`, and `float` data types
  - `input()` for user input
  - Type conversion with `int()` and `float()`
  - Formatted output using f-strings
  - `type()` and `id()` built-in functions
  - Use of the `datetime` module

---

## How to Run

1. Open a terminal in the project directory.
2. Run the script with:

```bash
python Submission_01.py
```

or, if your system uses `python3`:

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

> Note: Memory addresses shown by `id()` will differ each run.

---

## Concepts Demonstrated

- Variables
- User input
- Type casting
- Data types
- Formatted strings
- Built-in functions: `type()` and `id()`
- Module import (`datetime`)
- Basic arithmetic operations

---

## Limitations

- The program assumes valid numeric input for age, height, and favourite number.
- No error handling is currently implemented for invalid input.
- The birth year is approximate because it does not account for the user's exact birthday.

---

## Future Improvements

- Add input validation.
- Add exception handling with `try-except`.
- Validate age and height ranges.
- Save collected data to a CSV or text file.
- Add support for multiple entries.
- Add a graphical user interface (GUI).
