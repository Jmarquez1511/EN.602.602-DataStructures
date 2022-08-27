from pathlib import Path
from SourceCode.readchar import readfile
from SourceCode.infixcheck import is_prefix_valid
from SourceCode.conversion import prefix_to_postfix, flatten
import sys


def process_files(input_file: Path, output_file: Path):
    """
    Reads in the file using readfile(), then loops through the resulting dictionaries with prefix_to_postfix()
    to check if the expressions are valid, convert them, and add results to their corresponding dictionaries. An output
    file is generated as specified with a summary table and then specification for each line to the corresponding string
    read, the prefix expression processed, and corresponding conversion to postfix. In the cases where the lines do not
    contain valid prefix expressions, the output indicates it as well.
    Generates an output file
    :param input_file: string
    :param output_file: string
    :return:
    """
    original_stdout = sys.stdout
    expressions = readfile(input_file)
    evaluated = 0
    valid = 0
    invalid = []

    for i in expressions:
        evaluated += 1
        expression_ = list(expressions[i]['expression'])

        if is_prefix_valid(expression_):
            expressions[i]['valid'] = 1
            postfix = prefix_to_postfix(expression_)
            expressions[i]['postfix'] = flatten(postfix)
        else:
            expressions[i]['valid'] = 0
            invalid.append(i)

        valid += expressions[i]['valid']

    with open(output_file, 'w') as file:
        # Change the standard output to the file we created.
        sys.stdout = file
        print(f'''----------------------------------------OUTPUT SUMMARY----------------------------------------''')
        print(f'''File name: {input_file}''')
        print(f'''Total number of lines evaluated: {evaluated}''')
        print(f'''Number of lines containing valid prefix expressions:{valid}''')
        print(f'''Line numbers not containing valid prefix expressions:\n{invalid}''')
        print(f'''----------------------------------------------------------------------------------------------''')

        print(f'''---------------------------------------LINE BREAKDOWN-----------------------------------------''')
        for i in expressions:
            print(f'Line {i}')
            print(f'''Input:{''.join(expressions[i]['string'])}''')
            if expressions[i]['valid'] == 1:
                print(f'''Valid prefix expression: {''.join(expressions[i]['expression'])}''')
                print(f'''Postfix conversion:{''.join(expressions[i]['postfix'])}''')
                print(f'''----------------------------------------------------------------------------------------------''')
            else:
                print(f'''Line {i} does not contain a valid prefix expression''')
                print(f'''----------------------------------------------------------------------------------------------''')
        # Reset the standard output to its original value
        sys.stdout = original_stdout
