def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle case where all numbers are non-numeric
    return sum(numeric_numbers) / len(numeric_numbers) 