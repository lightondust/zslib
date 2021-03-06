import sys, os
import traceback


def iter_n_items(iterator, n):
    """
    :param iterator: iterator, for list use iterator = iter(lst); res = iter_n_items(iterator)
    :param n:
    :return:
    """
    res = []
    count = 0
    for i in iterator:
        count += 1
        if count > n:
            break
        res.append(i)
    return res


def compare_list(a, b):
    print('a not in b')
    for i in a:
        if i not in b:
            print(i)

    print()
    print('b not in a')
    for i in b:
        if i not in a:
            print(i)


def log_error_to_file(file_path):
    with open(file_path, 'a') as f:
        traceback.print_exc(file=f)


def log_error(file_path, console=False):
    from zslib.util.datetime_util import get_time_now
    if console:
        print(str(get_time_now()))
        traceback.print_exc()
    else:
        print_to_file(file_path, str(get_time_now()))
        with open(file_path, 'a') as f:
            traceback.print_exc(file=f)


# package
def find_package_location(package_name):
    for path in sys.path:
        if path:
            try:
                if package_name in os.listdir(path):
                    return path
            except Exception:
                pass


def print_to_file(file_path, message):
    with open(file_path, 'a') as f:
        print(message, file=f)
