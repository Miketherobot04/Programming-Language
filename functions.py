# functions.py

def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.

    Parameters:
    a (int or float): The first number
    b (int or float): The second number

    Returns:
    int or float: The sum of a and b
    """
    return a + b


def string_length(s):
    """
    Calculate the length of a string.

    Parameters:
    s (str): The input string

    Returns:
    int: The length of the string
    """
    return len(s)


def update_dictionary(d, key, value):
    """
    Update a dictionary with a key-value pair.

    If the key exists, increment its value by the provided value.
    If the key does not exist, add it with the provided value.

    Parameters:
    d (dict): The dictionary to update
    key: The key to update or add
    value: The value to add or increment

    Returns:
    None
    """
    if key in d:
        d[key] += value
    else:
        d[key] = value
