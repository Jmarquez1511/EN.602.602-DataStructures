from random import shuffle, seed
from pathlib import Path
import sys


# set seed for replicable results
seed(10)


def reverse_sample(size):
    reverse_list = [i for i in range(size-1, -1, -1)]
    return reverse_list


def ascending_sample(size):
    ascending_list = [i for i in range(size)]
    return ascending_list


def repeating_sample(size):
    unique = round(size * 0.825)
    repeat = round(size * 0.175)
    unique_list = [i for i in range(unique)]
    repeat_list = [i for i in range(repeat)]
    repeating_list = unique_list + repeat_list
    shuffle(repeating_list)
    return repeating_list


def shuffle_sample(size):
    shuffle_list = ascending_sample(size)
    shuffle(shuffle_list)
    return shuffle_list


def create_sample_files(sizes_list, types_list, type_names_list):

    for type_ in range(len(types_list)):
        for size in sizes_list:
            file_name = "Input/"+str(type_names_list[type_])+'_'+str(size)+'.txt'
            file = Path(file_name)
            samples = types_list[type_](size)
            original_stdout = sys.stdout
            with file.open('w') as file:
                sys.stdout = file
                print(str(size))
                print(str(type_names_list[type_]))
                for sample in samples:
                    print(sample)
                sys.stdout = original_stdout


if __name__ == "__main__":

    sample_sizes = [50, 100, 250, 500, 1000, 2000, 5000, 10000]
    sample_types = [shuffle_sample, reverse_sample, ascending_sample, repeating_sample]
    sample_names = ['random', 'reverse', 'ascending', 'repeating']
    path_name = '../Input/'
    create_sample_files(sample_sizes, sample_types, sample_names)
