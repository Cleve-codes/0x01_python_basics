

def case_converter(string: str, case: str) -> str:
    """
    Converts the case of the string to the specified case.
    :param string: The string to be converted.
    :param case: The case to which the string is to be converted.
    :return: The string after converting to the specified case.
    """
    if case == "upper":
        return string.upper()
    elif case == "lower":
        return string.lower()
    elif case == "title":
        return string.title()
    elif case == "capitalize":
        return string.capitalize()
    else:
        raise ValueError("Invalid case specified.")

# Tests
print(case_converter("Hello World", "upper"))  # HELLO WORLD