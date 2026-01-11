"""
Given a number, determine whether it is:
- an integer
- a float with no decimal part
- a float with a decimal part
"""

def determine_variable(num):
    if isinstance(num, int):
        return "integer"
    elif isinstance(num, float):
        if num.is_integer():
            return "float with no decimal part"
        else:
            return "float with a decimal part"
    else:
        return "not a number"
    
# Example usage
print(determine_variable(5))          # Output: integer
print(determine_variable(5.0))        # Output: float with no decimal part
print(determine_variable(5.75))       # Output: float with a decimal part