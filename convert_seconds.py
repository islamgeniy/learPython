"""
Write a program that converts seconds into HH:MM:SS format.
"""

def convert_seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

if __name__ == "__main__":
    input_seconds = int(input("Enter the number of seconds: "))
    result = convert_seconds_to_hhmmss(input_seconds)
    print(f"Converted time: {result}")
    
# Example usage
print(convert_seconds_to_hhmmss(3661))  # Output: 01:01:01
