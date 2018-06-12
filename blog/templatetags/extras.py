from django import template

register = template.Library()


@register.filter(name='more')
def more(value):

    if '<!--more-->' in value:
        nStr = '<!--more-->'
        nPos = value.index(nStr)
        nValue = value[nPos:]
        return nValue
    else:
        return value
