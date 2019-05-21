from django import template

register = template.Library()

@register.filter()
def myfilter(num):
    return num ** 2

