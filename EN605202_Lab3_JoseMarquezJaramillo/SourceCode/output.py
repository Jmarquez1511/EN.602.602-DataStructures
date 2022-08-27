from SourceCode.readfiles import readtext, readfreq
from SourceCode.huffmantree import createhuffman, preorderhuffman, decompresshuffman, compresshuffman, gethuffmancodes
import sys


def addfrequencies(expressions,frequencies):
    temp_freq = {}
    added = []
    for line in expressions:
        for char in expressions[line]['frequencies']:
            if char in temp_freq:
                temp_freq[char] += expressions[line]['frequencies'][char]
            else:
                temp_freq[char] = expressions[line]['frequencies'][char]

    for char in temp_freq:
        if char not in frequencies:
            frequencies[char] = temp_freq[char]
            added.append(char)
    return frequencies, added


def processfiles(freq_path, in_path, dc,ef, out_path):

    expressions = readtext(in_path)
    frequencies = readfreq(freq_path)

    if dc.upper() == 'D' or dc.upper() == 'DECOMPRESS':
        huffman = createhuffman(frequencies)
        action = 'decompressed'
        for line in expressions:
            decompression = decompresshuffman(huffman, ''.join(expressions[line]['upperstring']))
            expressions[line]['decompression'] = [c for c in decompression]
    else:
        if ef == 'Y':
            frequencies, added = addfrequencies(expressions,frequencies)

        action = 'compressed'
        improvement = 0
        huffman = createhuffman(frequencies)
        codes = gethuffmancodes(huffman, '', {})
        for line in expressions:
            compression = compresshuffman(codes, expressions[line]['upperstring'])
            expressions[line]['compression'] = compression
            expressions[line]['newbitcount'] = len(''.join(compression))
            lineimprovement = expressions[line]['bitcount'] - expressions[line]['newbitcount']
            expressions[line]['bitcountchange'] = lineimprovement
            improvement += lineimprovement

    original_stdout = sys.stdout
    with open(out_path, 'w') as file:
        sys.stdout = file

        print(f'''----------------------------------------PREORDER TREE-----------------------------------------''')
        preorderhuffman(huffman, 0)
        print(f'''----------------------------------------------------------------------------------------------''')
        print(f'''----------------------------------------OUTPUT SUMMARY----------------------------------------''')
        print(f'''File name: {in_path}''')
        if ef == 'Y' and len(added) > 0:
            print(f'''Scanned and added the following characters to the dictionary''')
            print(added)
        print(f'''Total number of lines {action}: {len(expressions)}''')
        if dc.upper() == 'D' or dc.upper() == 'DECOMPRESS':
            pass
        else:
            print(f'''Compression improvement of {improvement} bits''')
        print(f'''----------------------------------------------------------------------------------------------''')
        print(f'''---------------------------------------LINE BREAKDOWN-----------------------------------------''')
        for line in expressions:
            print(f'Line {line}')
            print(f'''Input: {''.join(expressions[line]['string'])}''')

            if dc.upper() == 'D' or dc.upper() == 'DECOMPRESS':
                print(f'''Decompressed string: {''.join(expressions[line]['decompression'])} \n''')
            else:
                print(f'''Valid String: {''.join(expressions[line]['validstring'])}''')
                print(f'''Compressed binary code: {''.join(expressions[line]['compression'])}''')
                print(f'''Bit count improvement: {expressions[line]['bitcountchange']} \n''')
        print(f'''----------------------------------------------------------------------------------------------''')
        print(f'''--------------------------------------FREQUENCY TABLE-----------------------------------------''')
        for i in frequencies:
            print(f'''{i}:{frequencies[i]}''')
        sys.stdout = original_stdout
