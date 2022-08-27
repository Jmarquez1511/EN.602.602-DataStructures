from pathlib import Path


def readtext(input_file) -> dict:
    """
    reads the file in the location specified character by character. The text read is store in a dictionary with line
    numbers as keys and for which each line is another dictionary which stores the string as a list.
    :param input_file: file
    :return: expressions : dictionary
    """
    input_file = Path(input_file)

    # Initialize a dictionary to store all lines
    expressions = {}
    line = 1
    expressions[line] = {}
    expressions[line]['string'] = []
    expressions[line]['validstring'] = []
    expressions[line]['upperstring'] = []

    with input_file.open('r') as opened_file:
        while True:
            char = opened_file.read(1)
            if not char:
                expressions[line]['frequencies'] = buildfreqtable(expressions[line]['upperstring'])
                expressions[line]['bitcount'] = len(expressions[line]['upperstring']) * 8
                # break at end
                break
            elif char == '\n':
                expressions[line]['frequencies'] = buildfreqtable(expressions[line]['upperstring'])
                expressions[line]['bitcount'] = len(expressions[line]['upperstring'])*8
                # If new line, initialize another line entry
                line += 1
                expressions[line] = {}
                expressions[line]['string'] = []
                expressions[line]['validstring'] = []
                expressions[line]['upperstring'] = []

            else:
                expressions[line]['string'].append(char)
                if char.isalnum():
                    expressions[line]['validstring'].append(char.upper())
                    expressions[line]['upperstring'].append(char.upper())
                continue

    return expressions


def readfreq(freq_file) -> dict:
    """
    reads the frequency table one character at a time. This only works with the format of the table provided. As it
    reads the letter, it then concatenates the numbers in the line. This in case of frequencies higher than 9.
    :param freq_file:
    :return: dict
    """

    freq_file = Path(freq_file)

    freq_table = {}

    with freq_file.open('r') as opened_file:
        while True:
            char = opened_file.read(1)
            if not char:
                # break at end
                break
            elif char == '\n':
                # If new line, initialize another line entry
                del number
                continue
            elif char == ' ' or char == '-':
                # Ignore space and -
                continue
            elif char.isnumeric():
                # if character is numeric
                if freq_table[letter] is None:
                    # when the letter has no frequency initialize with this number
                    number = char
                    freq_table[letter] = int(number)
                else:
                    # when the character already has a frequency then concatenate with the previous
                    number = int(str(number) + char)
                    freq_table[letter] = number

            elif char.isalpha:
                # if character is a letter, initialize dictionary key
                letter = char
                freq_table[letter] = None

    return freq_table


def buildfreqtable(charlist):

    freq = {}
    for char in charlist:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


if __name__ == "__main__":

    dct = readtext('../Input/ClearText.txt')
    ft = readfreq('../Input/FreqTable.txt')
    print('A' in ft)
    print(dct)
    for key in ft:
        print(key)
