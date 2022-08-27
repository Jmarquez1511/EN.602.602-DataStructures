from SourceCode.stack import Stack
from SourceCode.infixcheck import is_prefix_valid


def prefix_to_postfix(entry: dict):
    """
    Converts a prefix expression to a postfix expression. The function takes in a dictionary entry which is a
    dictionary. The function uses is_prefix_valid() to check if it is a valid prefix expression. If valid, a stack of
    class Stack is used to convert into a postfix expression. The function does not return anything but adds entries
    into the dictionary corresponding to the expression.
    :param entry:dict
    """
    # Print initial expression
    expression = entry['expression']

    # Stack for storing operands
    stack = Stack()
    # Valid symbols for mathematical operations
    valid_symbols = ['+', '-', '*', '/', '$']

    # Check if the expression is prefix valid
    if is_prefix_valid(expression):
        entry['valid'] = 1
        pass
    else:
        entry['valid'] = 0
        return

    # Parse through the expression
    for i in range(len(expression) - 1, -1, -1):
        # if token is operator
        if expression[i] in valid_symbols:

            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()
            # concatenate them as operand1 +
            # operand2 + operator
            temp = a + b + expression[i]
            stack.push(temp)

        # else if operand
        else:
            stack.push(expression[i])

    # printing final output
    # print(f'''Output postfix expression:{stack} \n''')
    entry['postfix'] = stack
    return
