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
