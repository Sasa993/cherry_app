from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def shorten_book_title(value):
	return value[:40] + "..." if len(value) > 40 else value
