from django import template
import html
from html.parser import HTMLParser

register = template.Library()


@register.filter(name='more')
def more(value):
    if '<!--more-->' in value:
        nstr = '<!--more-->'
        npos = value.index(nstr)
        nvalue = value[:npos]
        html_parser = HTMLParser()

        newtitle = html_parser.unescape(nvalue)
        return newtitle
    else:
        return value
