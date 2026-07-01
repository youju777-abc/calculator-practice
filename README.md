# Python Calculator Practice

This is a tiny Python project for practicing Git basics.

## Files

- `calculator.py`: contains simple calculator functions like `add(a, b)` and `subtract(a, b)`.
- `test_calculator.py`: checks that the calculator functions work correctly.

## Usage Examples

You can import the functions and use them like this:

```python
from calculator import add, subtract

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Run The Tests

From this folder, run:

```sh
python -m unittest
```

This command finds and runs the tests in `test_calculator.py`. If everything is working, the tests should pass.
