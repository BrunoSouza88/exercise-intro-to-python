from typing import List


def find_average(numbers: List[int]) -> float:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average
