from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def get_file_extension(value):
	return value.split('.')[-1]
