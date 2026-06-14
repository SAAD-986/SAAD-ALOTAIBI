def stats(numbers):
    """
    Takes a list of numbers and returns a tuple containing:
    (count, total, minimum, maximum, average)
    """
    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / count
    return (count, total, minimum, maximum, average)
data = [1, 2, 3, 4, 5]
count, total, minimum, maximum, average = stats(data)
print(f"Count:   {count}")
print(f"Total:   {total}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")

