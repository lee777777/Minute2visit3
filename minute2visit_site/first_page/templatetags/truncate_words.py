from django import template

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    words = value.split()
    if len(words) <= num_words:
        return value
    return ' '.join(words[:num_words]) 

@register.filter
def remaining_words(value, num_words):
    words = value.split()
    if len(words) <= num_words:
        return ""
    return ' '.join(words[num_words:]) 