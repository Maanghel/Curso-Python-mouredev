def calculate_average(*args):
    return sum(args) / len(args)

def calculate_median(*args):
    sorted_numbers = sorted(args)
    mid = len(args) // 2
    if len(args) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]