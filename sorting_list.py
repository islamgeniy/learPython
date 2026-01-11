"""
Given three numbers, output them in ascending order without using sort().
"""

def sort_three_numbers(a, b, c):
    if a <= b and a <= c:
        first = a
        if b <= c:
            second = b
            third = c
        else:
            second = c
            third = b
    elif b <= a and b <= c:
        first = b
        if a <= c:
            second = a
            third = c
        else:
            second = c
            third = a
    else:
        first = c
        if a <= b:
            second = a
            third = b
        else:
            second = b
            third = a
            
    return first, second, third

# Example usage
print(sort_three_numbers(3, 1, 2))  # Output: (1, 2, 3)
print(sort_three_numbers(9, 5, 7))  # Output: (5, 7, 9)
print(sort_three_numbers(4, 4, 2))  # Output: (2, 4, 4) 
