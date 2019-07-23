import sys, os
import json
import pickle


def make_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        os.chmod(dir_path, mode=0o775)


def save_to_json(dict_obj, path):
    with open(path, 'w') as f:
        json.dump(dict_obj, f)


def save(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load(path):
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj


# package
def find_package_location(package_name):
    for path in sys.path:
        if path:
            try:
                if package_name in os.listdir(path):
                    return path
            except Exception:
                pass

# file I/O
def get_line_from_file(line_no, f):
    line = get_lines_from_file([line_no], f)[line_no]
    return line


def get_line_from_file_path(line_no, file_path):
    with open(file_path, 'r') as f:
        return get_line_from_file(line_no, f)


def get_lines_from_file(line_nos, f):
    lines = {}
    line_nos = list(set(line_nos))
    line_nos.sort()
    line_nos.reverse()

    for i, line in enumerate(f):

        if i == line_nos[-1]:
            lines[i] = line
            line_nos.pop()
            if not line_nos:
                break

    return lines


def get_lines_from_file_path(line_nos, file_path):
    with open(file_path, 'r') as f:
        return get_lines_from_file(line_nos, f)
