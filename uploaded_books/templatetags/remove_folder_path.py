from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def remove_folder_path(value):
	return value.split('/')[1]
