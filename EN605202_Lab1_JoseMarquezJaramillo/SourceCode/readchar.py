def readfile(input_file) -> dict:
    """
    reads the file in the location specified character by character. As part of the function, characters that
    are non-alphanumeric nor valid sign operators are not considered to be parsed into the prefix expression.
    Both the original string and the parsed "clean" expressions from each line are stored in a dictionary for
    further analysis. The function returns a dictionary with line numbers as its keys.
    :param input_file: str
    :return: expressions-> dict
    """

    valid_symbols = ['+', '-', '*', '/', '$']

    # Initialize a dictionary to store all lines
    expressions = {}
    number = 1

    # Create a starter entry
    expressions[number] = {}
    # Within each entry start a list for the original string
    expressions[number]['string'] = []
    # and another one for the "clean expression"
    expressions[number]['expression'] = []

    # Loop through all the lines of the file
    with input_file.open('r') as opened_file:
        while True:
            char = opened_file.read(1)

            if not char:
                # Break at end
                break
            elif char == '\n':
                # If new line, initialize another line entry
                number += 1
                expressions[number] = {}
                expressions[number]['expression'] = []
                expressions[number]['string'] = []
            elif char.isalnum() or char in valid_symbols:
                # If alphanumeric or as part of the valid symbols then add to both the expression and string
                expressions[number]['expression'].append(char)
                expressions[number]['string'].append(char)
            else:
                # If another type of character then only add to the string
                # ignore for further analysis
                expressions[number]['string'].append(char)
                continue
    return expressions
