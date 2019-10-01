from datetime import datetime
from pytz import timezone


def get_time_now(time_zone='Asia/Tokyo'):
    if time_zone:
        return datetime.now(timezone(time_zone))
    else:
        return datetime.now()


def print_now(other_info=None, time_zone=''):
    print('{}:{}'.format(get_time_now(time_zone=time_zone), other_info))


def get_today(time_zone=None):
    return get_time_now(time_zone=time_zone).date()


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