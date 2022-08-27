def valid_operator(operator: str):
    """
    Helper function to identify valid operators
    :param operator: str
    :return: bool
    """
    # Valid symbols for mathematical operations
    valid_symbols = ['+', '-', '*', '/', '$']
    if operator in valid_symbols:
        return True
    else:
        return False


def flatten(list_of_lists: list):
    """
    Recursively flattens a list of lists
    :param list_of_lists: list
    :return: list
    """
    if len(list_of_lists) == 0:
        # If the list is empty return it
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        # If the first item of the list is a list, recursively call the function
        # starting at item o
        # then item 1 and concatenate
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


def prefix_to_postfix(expression_: list):
    """
    Converts a prefix expression to a postfix expression. The function takes in a list which contains the expression.
    The function returns a list which the postfix expression.
     param expression_:
    """
    if len(expression_) == 0:
        return

    else:
        op = expression_.pop(0)
        op1 = prefix_to_postfix(expression_) if valid_operator(expression_[0][0]) else expression_.pop(0)
        op2 = prefix_to_postfix(expression_) if valid_operator(expression_[0][0]) else expression_.pop(0)

        postfix = list()
        postfix.append(op1)
        postfix.append(op2)
        postfix.append(op)

        return postfix
