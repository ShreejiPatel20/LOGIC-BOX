# Pattern Generator and Number Analyzer

## Overview

This is a simple Python program that provides a menu with three options:

1. Generate a star (`*`) pattern.
2. Analyze a range of numbers by identifying even and odd numbers and calculating their sum.
3. Exit the program.

The program is menu-driven and uses basic Python concepts such as conditional statements, loops, and user input.

## Features

- Interactive menu-based interface
- Generates a right-angled star pattern
- Identifies whether each number in a given range is even or odd
- Calculates the total sum of all numbers in the selected range
- Handles invalid menu selections

## Technologies Used

- Python 3

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program using:

```bash
python Submission_02.py
```

## Program Flow

### Main Menu

```
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

### Option 1 – Generate a Pattern

- Enter the desired pattern size.
- The program prints a right-angled triangle using `*`.

Example:

```
Enter your Choice for the pattern: 5

*
**
***
****
*****
```

### Option 2 – Analyze a Range of Numbers

- Enter the starting number.
- Enter the ending number.
- The program:
  - Checks whether each number is even or odd.
  - Displays the result.
  - Calculates the sum of all numbers in the range.

Example:

```
Enter the start of range: 1
Enter the end of range: 5

1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd

The sum of numbers from 1 to 5 is: 15
```

### Option 3 – Exit

The program terminates with a goodbye message.

## Concepts Used

- Variables
- User Input
- Conditional Statements (`if`, `elif`, `else`)
- `for` Loops
- Arithmetic Operators
- String Multiplication
- Formatted Output (f-strings)

## File Structure

```
Submission_02.py
README.md
```

## Future Improvements

- Add input validation to prevent invalid entries.
- Support additional pattern types.
- Allow repeated execution without restarting the program.
- Improve the user interface with better menu navigation.

