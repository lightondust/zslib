from datetime import datetime


def get_today():
    return datetime.now().date()


def jp_string_to_datetime(jp_str, date_format='%Y年%m月%d日'):
    return datetime.strptime(jp_str, date_format)