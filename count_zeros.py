
#Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

#Examples:

#8=> returns true 
#6=> returns false

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))  # returns True
print(is_power_of_two(6))  # returns False
