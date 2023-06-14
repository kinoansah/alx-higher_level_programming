#!usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty or None
    if not a_dictionary:
        return None

    # Initialize the maximum score and corresponding key
    max_score = float('-inf')
    best_key = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the maximum
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
