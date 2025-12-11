🧮 Calculator Project

    A simple Python calculator project that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.
    This project includes:

    A Calculator class

    Unit tests using Python’s unittest module

    A CI/CD pipeline using GitHub Actions

    A documented codebase for learning and clarity

📁 Project Structure
    .
    ├── class_calculator.py
    ├── tests/
    │   └── test_class_calculator.py
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    └── README.md

🚀 Features

    Add two numbers

    Subtract two numbers

    Multiply two numbers

    Divide two numbers safely (handles divide-by-zero errors)

    Automated unit testing

    CI pipeline that executes on every commit/push

🧩 Calculator Class Overview

    The Calculator class accepts two numbers and exposes methods to perform arithmetic:

    Method	Description
    add()	Adds x and y
    subtract()	Subtracts y from x
    multiply()	Multiplies x and y
    divide()	Divides x by y (returns "ERR" on zero-div)
    🧪 Running Tests

    Tests are located inside the tests/ directory.

    Run all tests with:

    python -m unittest discover -v

🔧 GitHub Actions CI/CD

    This project includes a CI pipeline that:

    Installs Python

    Installs dependencies

    Runs all unit tests

    Deploys on the main branch (optional)

    The workflow file is located at:

    .github/workflows/ci.yml

▶️ Usage Example
    from class_calculator import Calculator

    calc = Calculator(10, 5)

    print(calc.add())        # 15
    print(calc.subtract())   # 5
    print(calc.multiply())   # 50
    print(calc.divide())     # 2.0

📌 Requirements

    Python 3.8+

    (optional) requirements.txt if you add dependencies later

📜 License

    This project is open-source.
    Feel free to use, modify, and learn from it.