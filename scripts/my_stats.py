# my_stats.py
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def minimum(numbers):
    min_value = numbers[0]
    for n in numbers:
        if n < min_value:
            min_value = n
    return min_value