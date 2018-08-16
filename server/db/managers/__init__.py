import datetime
from random import randint


def get_timebased_uuid():
    prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = randint(100000, 999999)
    return '{p}:{s}'.format(p=prefix, s=suffix)
