import numpy as np


def array_describe(arr, print_data=True, return_data=False):

    arr_info = {
        'shape': arr.shape,
        'mean': np.mean(arr, axis=0),
        'range': np.array([np.min((arr), axis=0), np.max((arr), axis=0)]).T,
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