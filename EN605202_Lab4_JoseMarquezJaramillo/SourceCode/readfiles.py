import os
from pathlib import Path
from SourceCode.linkedlist import Node, LinkedList


def get_file_names(path_name):
    return os.listdir(path_name)


def read_files(path_name) -> dict:

    data_sets = {}

    file_names = get_file_names(path_name)

    for file in file_names:
        name = file.split('.')[0]
        data_sets[name] = {}
        with Path(path_name+file).open('r') as opened_file:
            data_sets[name]['length'] = opened_file.readline().split()[0]
            data_sets[name]['order'] = opened_file.readline().split()[0]
            data_sets[name]['list'] = []
            data_sets[name]['sorts'] = {}
            while True:
                try:
                    number = opened_file.readline().split()[0]
                    data_sets[name]['list'].append(int(number))
                except:
                    break

        head = Node(data_sets[name]['list'][0])
        linked_list = LinkedList()
        linked_list.head = head

        for number in data_sets[name]['list'][1:]:
            linked_list.add(number)

        data_sets[name]['linked_list'] = linked_list

    return data_sets


if __name__ == "__main__":
    data_sets = read_files('../Input/')
    print(data_sets['random_50'])







