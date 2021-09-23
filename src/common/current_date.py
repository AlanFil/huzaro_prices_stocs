from datetime import datetime
from time import time


def current_date():
    return datetime.fromtimestamp(time()).strftime('%Y-%m-%d_%H_%M')
