import os


def map_to_geeqie_collection(label_path_map, save_to_dir='./label_data'):
    header_lines = ['#Geeqie collection',
                    '#created with Geeqie version 1.4',
                    '#geometry: 0 28 1440 2532']
    header_strings = '\n'.join(header_lines) + '\n'
    end_strings = '#end'

    # make dir to save collection file
    if not os.path.exists(save_to_dir):
        os.mkdir(save_to_dir)
        os.chmod(save_to_dir, 0o777)

    # save collection files
    for label, path_list in label_path_map.items():
        label_file_path = os.path.join(save_to_dir, label) + '.gqv'
        with open(label_file_path, 'w') as f:
            f.write(header_strings)
            for path in path_list:
                f.write('"{}"\n'.format(path))
            f.write(end_strings)
        os.chmod(label_file_path, 0o777)


def file_list_from_gqv(gqv_path):
    file_list = []
    with open(gqv_path, 'r') as f:
        for line in f.readlines():
            line = line.replace('"', '').replace('\n', '')
            if line.endswith('.jpg') or line.endswith('.png'):
                file_list.append(line)

    return file_list


def label_path_map_from_gqv_list(geeqie_list):
    label_path_map = {}
    for gqv in geeqie_list:
        label = gqv.split('/')[-1].split('.')[0]
        file_list = file_list_from_gqv(gqv)
        label_path_map[label] = file_list

    return label_path_map
