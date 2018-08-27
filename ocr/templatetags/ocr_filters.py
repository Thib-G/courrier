import re
from django import template

register = template.Library()

def surround(text, q, n=5):
    result = '... '
    for word in q.split():
        result += search_text(text, word, n) + ' ... '
    return result

def search_text(text, target, n):
    '''Searches for text, and retrieves n words either side of the text, which are retuned seperatly'''
    # https://stackoverflow.com/questions/17645701/extract-words-surrounding-a-search-word
    word = r"\W*([\w]+)"
    try:
        groups = re.search(r'{}\W*({}){}'.format(word*n,target,word*n), text, re.IGNORECASE).groups()
        return f"{' '.join(groups[:n])} {groups[n]} {' '.join(groups[n+1:])}"
    except AttributeError:
        return f"ERROR, word \"{target}\" not found in text \"{text}\""

register.filter('surround', surround)
