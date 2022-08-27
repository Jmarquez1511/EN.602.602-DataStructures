The program was developed using Pycharm 2021.3.1 on Python 3.10.

The program can be run as a module with real inputs from the command line. I personally ran the program succesfully in Windows Powershell.

When running the file, the user must input:
    - The path to the frequency table,
    - the path to the text to be compressed or decompressed,
    - the character 'C' for compression or the character 'D' for decompression,
    - the instruction 'Y' for scanning and comparing the frequency table with the text previous to compression or 'N' for processing without comparing,
    - and the path to the output file.

An example for running the program while compressing and scanning and adding new characters to the frequency dictionary is:
python -m SourceCode FreqTable.txt ClearText.txt C Y OutputText.txt

The resulting output file will be stored as specified and there will also be a printout in powershell.


