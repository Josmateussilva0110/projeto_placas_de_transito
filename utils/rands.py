import string
from random import SystemRandom
from django.utils.text import slugify

def ramdom_letters(k=5):
    return ''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=k))


def new_slugify(text, k=3):
    return slugify(text) + '-' + ramdom_letters(k)
