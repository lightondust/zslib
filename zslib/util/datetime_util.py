from datetime import datetime


def print_now(other_info=None):
    print('{}:{}'.format(datetime.now(), other_info))


def get_today():
    return datetime.now().date()


def get_time_for_file_name(precision='minute'):
    """
    :param precision: 'm', 'h', 's', 'd'
    :return:
    """
    if precision in ['minute', 'm']:
        return datetime.strftime(datetime.now(), '%Y%m%d%H%M')
    elif precision in ['hour', 'h']:
        return datetime.strftime(datetime.now(), '%Y%m%d%H')
    elif precision in ['second', 's']:
        return datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    elif precision in ['day', 'd']:
        return datetime.strftime(datetime.now(), '%Y%m%d')


def jp_string_to_datetime(jp_str, date_format='%Y年%m月%d日'):
    return datetime.strptime(jp_str, date_format)