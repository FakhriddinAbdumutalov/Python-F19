from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Math ops
print(add(2,3), subtract(5,2), multiply(3,4), divide(10,2))

# String utils
print(reverse_string("hello"), count_vowels("OpenAI"))

# Geometry
print(calculate_area(3), calculate_circumference(3))

# File I/O
write_file("stocks_2017.csv", "Test content")
print(read_file("stocks_2017.csv"))
