from typing import List


def find_biggest_name(names: List[str]) -> str:
    longest_name = ""
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name
