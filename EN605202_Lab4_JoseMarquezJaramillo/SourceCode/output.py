from SourceCode.linkedlist import LinkedList, copy_list
from SourceCode.mergesort import merge_sort, natural_merge_sort
from datetime import datetime
from pathlib import Path
import SourceCode.quicksort as quicksort
import pandas as pd
import sys

sys.setrecursionlimit(1000000000)


def sort_quick(data_sets: dict) -> dict:
    global c
    global r
    for type in [2, 3, 5]:
        # run through quicksorts 2 and 3
        for data in ['ascending_50', 'random_50', 'reverse_50', 'repeating_50',
                 'ascending_100', 'random_100', 'reverse_100', 'repeating_100',
                 'ascending_250', 'random_250', 'reverse_250', 'repeating_250',
                 'ascending_500', 'random_500', 'reverse_500', 'repeating_500',
                 'ascending_1000', 'random_1000', 'reverse_1000', 'repeating_1000',
                 'ascending_2000', 'random_2000', 'reverse_2000', 'repeating_2000',
                 'ascending_5000', 'random_5000', 'reverse_5000', 'repeating_5000',
                 'ascending_10000', 'random_10000',  'reverse_10000', 'repeating_10000']:

            a_list = list(data_sets[data]['list'])
            begin = datetime.now()
            c, r = quicksort.all_quick_sorts(a_list, 0, len(a_list)-1, type)
            end = datetime.now()
            time_diff = end - begin
            time_diff = int(time_diff.total_seconds()*1000)
            data_sets[data]['sorts']['quicksort'+str(type)] = {}
            data_sets[data]['sorts']['quicksort'+str(type)]['sorted_list'] = a_list
            data_sets[data]['sorts']['quicksort'+str(type)]['comparisons'] = c
            data_sets[data]['sorts']['quicksort'+str(type)]['replacements'] = r
            data_sets[data]['sorts']['quicksort' + str(type)]['milliseconds'] = time_diff
            print(f'''n:{data_sets[data]['length']}, order:{data_sets[data]['order']}, sort: quicksort{str(type)}, '''
                  f'''Comparisons:{c}, Replacements:{r}''')

    for type in [1, 4]:
        # run through the rest of the quicksorts
        for data in ['ascending_50', 'random_50', 'reverse_50', 'repeating_50',
                 'ascending_100', 'random_100', 'reverse_100', 'repeating_100',
                 'ascending_250', 'random_250', 'reverse_250', 'repeating_250',
                 'ascending_500', 'random_500', 'reverse_500', 'repeating_500',
                 'ascending_1000', 'random_1000', 'reverse_1000', 'repeating_1000',
                 'ascending_2000', 'random_2000', 'reverse_2000', 'repeating_2000',
                 'random_5000', 'repeating_5000',
                  'random_10000', 'repeating_10000']:
            c, r = 0, 0

            a_list = list(data_sets[data]['list'])
            begin = datetime.now()
            c, r = quicksort.all_quick_sorts(a_list, 0, len(a_list)-1, type)
            end = datetime.now()
            time_diff = end - begin
            time_diff = int(time_diff.total_seconds()*1000)
            data_sets[data]['sorts']['quicksort' + str(type)] = {}
            data_sets[data]['sorts']['quicksort'+str(type)]['sorted_list'] = a_list
            data_sets[data]['sorts']['quicksort'+str(type)]['comparisons'] = c
            data_sets[data]['sorts']['quicksort'+str(type)]['replacements'] = r
            data_sets[data]['sorts']['quicksort' + str(type)]['milliseconds'] = time_diff
            print(f'''n:{data_sets[data]['length']}, order:{data_sets[data]['order']}, sort: quicksort{str(type)}, '''
                  f'''Comparisons:{c}, Replacements:{r}''')


def sort_merge(data_sets):
    for data in ['ascending_50', 'random_50', 'reverse_50', 'repeating_50',
                 'ascending_100', 'random_100', 'reverse_100', 'repeating_100',
                 'ascending_250', 'random_250', 'reverse_250', 'repeating_250',
                 'ascending_500', 'random_500', 'reverse_500', 'repeating_500',
                 'ascending_1000', 'random_1000', 'reverse_1000', 'repeating_1000',
                 'ascending_2000', 'random_2000', 'reverse_2000', 'repeating_2000',
                 'ascending_5000', 'random_5000', 'reverse_5000', 'repeating_5000',
                 'ascending_10000', 'random_10000',  'reverse_10000', 'repeating_10000']:

        linked_list = LinkedList()
        linked_list.head = copy_list(data_sets[data]['linked_list'].head)
        head = linked_list.head
        begin = datetime.now()
        head, c, r = merge_sort(head)
        end = datetime.now()
        time_diff = end - begin
        time_diff = int(time_diff.total_seconds() * 1000)
        list_ = list(head.make_list())
        data_sets[data]['sorts']['mergesort'] = {}
        data_sets[data]['sorts']['mergesort']['sorted_list'] = list_
        data_sets[data]['sorts']['mergesort']['comparisons'] = c
        data_sets[data]['sorts']['mergesort']['replacements'] = r
        data_sets[data]['sorts']['mergesort']['milliseconds'] = time_diff
        print(f'''n:{data_sets[data]['length']}, order:{data_sets[data]['order']}, sort: Mergesort, '''
              f'''Comparisons:{c}, Replacements:{r}''')

        linked_list = LinkedList()
        linked_list.head = copy_list(data_sets[data]['linked_list'].head)
        head = linked_list.head
        begin = datetime.now()
        head, c, r = natural_merge_sort(head)
        end = datetime.now()
        time_diff = end - begin
        time_diff = int(time_diff.total_seconds() * 1000)
        list_ = list(head.make_list())
        data_sets[data]['sorts']['natural_mergesort'] = {}
        data_sets[data]['sorts']['natural_mergesort']['sorted_list'] = list_
        data_sets[data]['sorts']['natural_mergesort']['comparisons'] = c
        data_sets[data]['sorts']['natural_mergesort']['replacements'] = r
        data_sets[data]['sorts']['natural_mergesort']['milliseconds'] = time_diff
        print(f'''n:{data_sets[data]['length']}, order:{data_sets[data]['order']}, sort: Natural Merge Sort, '''
              f'''Comparisons:{c}, Replacements:{r}''')


def sort_all(data_sets):
    sort_quick(data_sets)
    sort_merge(data_sets)


def save_files(data_sets):
    for data in data_sets:
        for sort in data_sets[data]['sorts']:
            file_name = 'Output/' + str(data_sets[data]['length']) + '_' + str(data_sets[data]['order']) + '_' + str(sort) + '.txt'
            file_name = Path(file_name)
            original_stdout = sys.stdout
            with open(file_name, 'w') as file:
                sys.stdout = file
                print(data)
                print(sort)
                list_ = data_sets[data]['sorts'][sort]['sorted_list']
                for i in list_:
                    print(i)
            sys.stdout = original_stdout


def create_df(data_sets):
    sorts_dict = {'length': [], 'order': [], 'sorting_method': [], 'comparisons': [], 'replacements': [],
                  'milliseconds': []}
    for data in data_sets:
        for sort in data_sets[data]['sorts']:
            sorts_dict['length'].append(data_sets[data]['length'])
            sorts_dict['order'].append(data_sets[data]['order'])
            sorts_dict['sorting_method'].append(sort)
            sorts_dict['comparisons'].append(data_sets[data]['sorts'][sort]['comparisons'])
            sorts_dict['replacements'].append(data_sets[data]['sorts'][sort]['replacements'])
            sorts_dict['milliseconds'].append(data_sets[data]['sorts'][sort]['milliseconds'])

    df = pd.DataFrame(sorts_dict)
    df.to_csv('Analysis/Graphs/results.csv')


if __name__ == "__main__":
    sample_sizes = [50, 100, 250, 500, 1000, 2000, 5000, 10000]
    sample_types = [shuffle_sample, reverse_sample, ascending_sample, repeating_sample]
    sample_names = ['random', 'reverse', 'ascending', 'repeating']
    path_name = '../Input/'
    process_program(sample_sizes, sample_types, sample_names, path_name)



