def is_prefix_valid(expression_: list) -> bool:
    """
    Helper function to determine if the prefix expression is a valid one or not. In order for a prefix expression to be
    valid it must meet:
    1. The total number of operands is one more than the number of operators.
    2. Any prefix of the expression not including the last two symbols must contain no less operators than operands.
    This function is later used in prefix_to_postfix() to not try and evaluate invalid prefix expressions
    :param expression_: str
    :return: bool
    """
    valid_symbols = ['+', '-', '*', '/', '$']
    operands = list()
    operators = list()

    # Check if The total number of operands is one more than the number of operators
    # otherwise return false
    for i in range(len(expression_)-1, -1, -1):
        symbol = expression_[i]
        if symbol in valid_symbols:
            operators.append(symbol)
        elif symbol.isalpha():
            operands.append(symbol)
    if len(operands) != (1 + len(operators)):
        return False

    # Check if any prefix of the expression not including the last two symbols must contain no less
    # operators than operands, otherwise return false
    operands_ = list()
    operators_ = list()
    for i in range(len(expression_)-3, -1, -1):
        symbol = expression_[i]
        if symbol in valid_symbols:
            operators_.append(symbol)
        elif symbol.isalpha():
            operands_.append(symbol)
    if len(operators_) <= len(operands_):
        return False
    else:
        return True
