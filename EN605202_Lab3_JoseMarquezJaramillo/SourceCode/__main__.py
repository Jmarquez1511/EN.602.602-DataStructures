# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m proj0'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
from SourceCode.output import processfiles

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("freq_file", type=str, help="Frequency File Name")
arg_parser.add_argument("in_file", type=str, help="Input File Name")
arg_parser.add_argument("dc", type=str, help="Input 'C' or 'D' for compression or decompression, respectively")
arg_parser.add_argument("ef", type=str, help="Input 'Y' or 'N' to scan for extra characters")
arg_parser.add_argument("out_file", type=str, help="Output File Name")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path = Path(args.in_file)
freq_path = Path(args.freq_file)
out_path = Path(args.out_file)
dc = args.dc
ef = args.ef

# Call the process file
processfiles(freq_path, in_path, dc, ef, out_path)

# Print to command the output file for reference
with out_path.open('r') as file:
    print(file.read())
