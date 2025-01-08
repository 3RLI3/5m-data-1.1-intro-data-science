# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.

def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number



# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.

def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    
    return sum(x**2 for x in numbers)


# Question 3

# Write a function that counts the number of vowels in a string.

def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    
    vowels = "aeiouAEIOU"  # Define vowels to be identified in the string 
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

    
# Question 4

# Write a function that counts the number of repeated characters in a string.

def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
   
    char_count = {} # Create a dictionary to store the count of each character in the string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1 # Increment the count of the character in the dictionary by 1 if it is found in the string 

    for key, value in char_count.items(): 
        if value > 1: # Check if the count of the specific character is greater than 1 (repeated character)
            return value
    return 0 # Return 0 if no repeated characters are found
        
      

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

