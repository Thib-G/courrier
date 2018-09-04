import re
import shlex
from django import template

import logging

register = template.Library()


def search_text(text, target, numchars):
    pattern = re.compile(f".{{,{numchars}}}{target}{{,{numchars}}}", re.UNICODE|re.IGNORECASE|re.DOTALL)
    result = re.search(pattern, text)
    if result:
        return result.group()
    return f"{target} not found in text;"

def surround(text, q, numchars=80):
    result = ' [...] '
    for word in shlex.split(q):
        result += search_text(text, word, numchars) + ' [...] '
    return result


register.filter('surround', surround)
