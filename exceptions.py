

def add_numbers(a, b):
    try:
        result = a + b
        print(f"\nThe result is: {result}")
    except TypeError as e:
        print(f"\nError: {e}") 
        print(f"\nPlease provide two integers as arguments when invoking this function.")

# Example usage
add_numbers(5, 10)
add_numbers(5, 5)
add_numbers(10, 5)


my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def get_value(dictionary, key):
     value = dictionary[key]
     print(f"The value for '{key}' is: {value}")

# Example usage
get_value(my_dict, "age")
get_value(my_dict, "name")
get_value(my_dict, "occupation")
