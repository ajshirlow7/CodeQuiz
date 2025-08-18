from django import template

register = template.Library()

@register.filter
def at_index(lst, idx):
    try:
        return lst[idx]
    except (IndexError, TypeError):
        return None
