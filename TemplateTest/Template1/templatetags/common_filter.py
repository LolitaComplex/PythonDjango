from django import template

register = template.Library()

@register.filter
def commonFilter(value, args):
    return value + args
