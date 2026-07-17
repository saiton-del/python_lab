
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from utils import square, is_even, celsius_to_fahrenheit, greet

number = float(input("Enter a number: "))
name = input("Enter your name: ")

print(f"Square: {square(number)}")
print(f"Even: {is_even(number)}")
print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")
print(greet(name))
