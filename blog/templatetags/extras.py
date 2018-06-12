from django import template

register = template.Library()


@register.filter(name='more')
def more(value):

    if '<!--more-->' in value:
        nstr = '<!--more-->'
        npos = value.index(nstr)
        nvalue = value[npos:]
        return nvalue
    else:
        return value
