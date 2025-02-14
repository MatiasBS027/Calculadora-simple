# Simple Calculator

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

You can use the calculator by importing the `calculator` module from the `src` package. Here is an example of how to use it:

```python
from src.calculator import add, subtract, multiply, divide

result_add = add(5, 3)        # 8
result_subtract = subtract(5, 3)  # 2
result_multiply = multiply(5, 3)  # 15
result_divide = divide(5, 3)      # 1.666...
```

## Running Tests

To run the tests for the calculator, use the following command:

```
python -m unittest discover -s tests
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.