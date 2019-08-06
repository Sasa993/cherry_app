from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def shorten_file_name(value):
	extension = value.split('.')[-1]

	return value[:15] + "." + extension
