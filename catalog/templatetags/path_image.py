from django import template

from config.settings import BASE_DOMAIN

register = template.Library()


@register.simple_tag()
def mymedia(data):
    if data:
        return f'{BASE_DOMAIN}{data}'
    return '#'
