import numpy as np
from numpy import ndarray


def value_to_index(value, arr):
    return values_to_indices([value], arr)[0]


def values_to_indices(values, arr: ndarray):
    return np.array([(arr < v).sum() for v in values])


def array_describe(arr, print_data=True, return_data=False):

    arr_info = {
        'shape': arr.shape,
        'mean': np.mean(arr, axis=0),
        'range': np.array([np.min(arr, axis=0), np.max(arr, axis=0)]).T,
        'std': np.std(arr, axis=0)
    }

    labels = ['shape', 'mean', 'range', 'std']

    if print_data:
        for label in labels:
            print('{}:\n{}\n'.format(label, arr_info[label]))

    if return_data:
        return arr_info


def standard_normalize(arr, detail=False, specified=False, std=None, mean=None):
    """
    :param arr:
    :param std:
    :param mean:
    :param specified:
    :param detail:
    :return: arr or arr, mean, std
    """

    if not specified:
        std = np.std(arr, axis=0)
        mean = np.mean(arr, axis=0)

    arr_norm = (arr - mean) / std

    if detail:
        return arr_norm, mean, std

    else:
        return arr_norm


def array_divide_random(arr, ratio=0.9):

    dim = arr.shape[0]
    id_all = np.random.choice(dim, dim, replace=False)
    cut_pos = int(dim*ratio)
    arr_shuffle = arr[id_all]

    return arr_shuffle[:cut_pos], arr_shuffle[cut_pos:]


def cross_validation_set(arr, ratio=0.9, random=True):

    dim = arr.shape[0]
    id_all = np.random.choice(dim, dim, replace=False)

    cut_length = dim - int(dim * ratio)
    arr_shuffle = arr[id_all]

    if random:
        arr = arr_shuffle

    cross_set = []
    for step in range(int(arr.shape[0] / cut_length)):
        start = step * cut_length
        end = start + cut_length
        arr_test = arr[start:end]
        arr_train = np.vstack((arr[:start], arr[end:]))

        data_ = [arr_train, arr_test]

        if len(cross_set) >= int(1/ratio):
            break

        cross_set.append(data_)

    return cross_set

