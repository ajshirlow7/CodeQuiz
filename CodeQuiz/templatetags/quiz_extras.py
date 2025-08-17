from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def count_correct(answers):
    if not answers:
        return 0
    # answers is a list of tuples (text, is_correct)
    return sum(1 for a in answers if isinstance(a, (list, tuple)) and len(a) > 1 and a[1] is True)

@register.filter
def count_total(answers):
    if not answers:
        return 0
    # answers is a list of tuples (text, is_correct)
    return sum(1 for a in answers if isinstance(a, (list, tuple)))
