import SourceCode.generatefiles as generatefiles
import SourceCode.readfiles as readfiles
import SourceCode.output as output
from pathlib import Path
from random import seed

# set seed for replicable results
seed(10)

sample_sizes = [50, 100, 250, 500, 1000, 2000, 5000, 10000]
types = [generatefiles.shuffle_sample, generatefiles.reverse_sample, generatefiles.ascending_sample,
         generatefiles.repeating_sample]
sample_names = ['random', 'reverse', 'ascending', 'repeating']

# from generatefiles.py
# Generate sample files based on the parameters above
generatefiles.create_sample_files(sample_sizes, types, sample_names)

# from readfiles.py
# read files
data_sets = readfiles.read_files('Input/')

# from output.py
# sort all files
output.sort_all(data_sets)
# save all output files
output.save_files(data_sets)
# save the dataframe into a csv for further analysis
output.create_df(data_sets)



