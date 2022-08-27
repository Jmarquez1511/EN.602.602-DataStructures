from SourceCode.stack import Stack


def is_prefix_valid(expression: str) -> bool:
    """
    Helper function to determine if the prefix expression is a valid one or not. In order for a prefix expression to be
    valid it must meet:
    1. The total number of operands is one more than the number of operators.
    2. Any prefix of the expression not including the last two symbols must contain no less operators than operands.
    This function is later used in prefix_to_postfix() to not try and evaluate invalid prefix expressions
    :param expression: str
    :return: bool
    """
    valid_symbols = ['+', '-', '*', '/', '$']
    operands = Stack()
    operators = Stack()

    # Check if The total number of operands is one more than the number of operators
    # otherwise return false
    for i in range(len(expression)-1, -1, -1):
        symbol = expression[i]
        if symbol in valid_symbols:
            operators.push(symbol)
        elif symbol.isalpha():
            operands.push(symbol)
    if len(operands.items) != (1 + len(operators.items)):
        return False

    # Check if any prefix of the expression not including the last two symbols must contain no less
    # operators than operands, otherwise return false
    operands_ = Stack()
    operators_ = Stack()
    for i in range(len(expression)-3, -1, -1):
        symbol = expression[i]
        if symbol in valid_symbols:
            operators_.push(symbol)
        elif symbol.isalpha():
            operands_.push(symbol)
    if len(operators_.items) <= len(operands_.items):
        return False
    else:
        return True
