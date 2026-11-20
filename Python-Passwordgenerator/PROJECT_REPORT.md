# Python Password Generator — Project Report

## 1. Project Title
Python Password Generator

## 2. Objective
To create a Python program that generates a random password of a length selected by the user.

## 3. Tools Used
- Python 3
- Notepad
- Windows Command Prompt

## 4. How the Program Works
1. The program asks the user for a password length.
2. It checks whether the length is at least 8.
3. It combines letters, numbers, and symbols.
4. It uses Python's `secrets` module to select random characters.
5. It displays the generated password.

## 5. Functions and Modules
- `generate_password(length)` — Generates the password.
- `main()` — Runs the program.
- `secrets` — Provides security-oriented random selection.
- `string` — Provides letters, digits, and punctuation symbols.

## 6. Test Cases

| Test | Input | Expected result |
|---|---|---|
| Generate password | 12 | Displays a 12-character password |
| Minimum length | 8 | Displays an 8-character password |
| Short length | 5 | Displays a minimum-length error |
| Invalid input | hello | Displays an input error |
| Negative length | -2 | Displays a minimum-length error |

Run these tests in CMD and confirm the actual results before marking them as passed.

## 7. Screenshots
Save screenshots of your own program in the `screenshots` folder:

- `password-output.png` — Successful password generation
- `password-error-test.png` — Error for a short password length

## 8. Learning Outcomes
I learned how to use Python functions, loops, modules, strings, user input, and error handling. I also learned how the `secrets` module can be used to generate security-sensitive random values.

## 9. Conclusion
The Python Password Generator is a beginner project that demonstrates basic Python programming and introduces secure random password generation.

## 10. Future Improvements
- Allow users to choose whether to include symbols or numbers.
- Ensure that each selected character category appears at least once.
- Add automated tests.