import sys, os


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


# package
def find_package_location(package_name):
    for path in sys.path:
        if path:
            try:
                if package_name in os.listdir(path):
                    return path
            except Exception:
                pass

