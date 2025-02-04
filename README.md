# Python Average Calculation Bug

This repository demonstrates a common bug in Python functions that calculate averages: improper handling of non-numeric input. 

The `average_bug.py` file contains a function that calculates the average of a list of numbers. While it correctly handles the case of an empty list, it does not gracefully handle situations where the input list contains non-numeric values.  This will lead to a `TypeError`. 

The `average_solution.py` file provides a corrected version that uses exception handling to manage non-numeric data, providing more robust functionality. 