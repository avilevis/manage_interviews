from django import template

register = template.Library()


@register.filter()
def get_type(value):
    if type(value) == list:
        return 'list'
    elif type(value) == dict:
        return 'dict'
    return 'other'
