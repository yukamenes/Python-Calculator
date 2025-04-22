# Python-Calculator 🧮

A simple Python implementation of a calculator, where users can perform basic arithmetic operations with a clean console interface and custom ASCII art.

## Features ✨

- Performs **basic arithmetic** operations: +, -, *, /
- Supports **chained calculations** with previous results
- Displays a **custom ASCII logo**
- **Clears the console** for a tidy experience
- Handles **invalid inputs** and division by zero
- Provides a **graceful exit** option

## Installation 📦

Ensure you have Python 3.x installed. No additional packages are required.

## Usage 🚀

Run the script using:

```sh
python main.py
```

Follow the prompts to perform calculations:
```sh
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What's the first number?: 10
+
-
*
/
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, 'n' to start a new calculation, or 'e' to exit: e
Goodbye!
```

## Files 📂

- calculator.py - The main script for running the calculator
- art.py - Contains the ASCII logo displayed at start
- README.md - Project documentation

## License 📜

This project is released under the CC0 1.0 Universal license, allowing anyone to use, modify, and distribute it without restrictions.
