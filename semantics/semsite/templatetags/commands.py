from django.template import Library
import re
from html import unescape

register = Library()

@register.filter
def fix_text(string):
    string = re.sub('&nbsp;', ' ', string)
    string = re.sub('\n', ' ', string)
    string = re.sub('\r', ' ', string)
    return string