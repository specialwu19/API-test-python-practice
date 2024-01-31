import time


def random_email():
    date = str(time.time())
    email = "mmm" + date + "@mail.com"
    return email


def is_array(a):
    return isinstance(a, (list, tuple, set))
