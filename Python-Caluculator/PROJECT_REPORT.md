# Python Calculator — Project Report

## 1. Project Title
Python Calculator

## 2. Objective
To create a simple Python program that performs basic arithmetic operations through a command-line menu.

## 3. Tools Used
- Python 3
- Notepad for writing and saving the code
- Windows Command Prompt (CMD) for running and testing the program

## 4. Features Implemented
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit option
6. Validation for invalid menu choices
7. Error handling for non-numeric input
8. Protection against division by zero

## 5. How the Program Works
1. The program displays a menu of operations.
2. The user selects an operation.
3. The program asks for two numbers.
4. It calls the function for the selected operation.
5. It displays the result.
6. The menu appears again until the user chooses Exit.

## 6. Functions Used
- `add(num1, num2)` — returns the sum.
- `subtract(num1, num2)` — returns the difference.
- `multiply(num1, num2)` — returns the product.
- `divide(num1, num2)` — returns the quotient and prevents division by zero.
- `calculator()` — displays the menu, accepts input, and controls the program.

## 7. Test Cases and Expected Results
Run each test in CMD and compare the displayed result with the expected result.

| Test | Input / Action | Expected result |
|---|---|---|
| Addition | Select 1; enter 10 and 5 | `Result: 15.0` |
| Subtraction | Select 2; enter 10 and 5 | `Result: 5.0` |
| Multiplication | Select 3; enter 10 and 5 | `Result: 50.0` |
| Division | Select 4; enter 10 and 5 | `Result: 2.0` |
| Decimal values | Select 1; enter 10.5 and 2.5 | `Result: 13.0` |
| Division by zero | Select 4; enter 10 and 0 | `Input error: Cannot divide by zero.` |
| Invalid menu choice | Enter 8 at the menu | `Invalid choice. Please select 1, 2, 3, 4, or 5.` |
| Non-numeric input | Enter `hello` when asked for a number | `Input error: Please enter numbers only.` |
| Exit | Enter 5 at the menu | `Thank you for using Python Calculator!` |

**Note:** These are expected results. Only mark a test as passed after you run it and confirm the output.

## 8. Screenshots
Save your own screenshots from CMD in the `screenshots` folder:
- `calculator-menu.png` — calculator menu
- `calculator-addition.png` — successful calculation
- `calculator-error-test.png` — division-by-zero error message

## 9. Conclusion
This project demonstrates basic Python programming concepts, including functions, user input, conditional statements, loops, and exception handling. It also demonstrates testing both normal calculations and invalid inputs.

## 10. Future Improvements
- Add a calculation history
- Add more mathematical operations
- Improve the display format
