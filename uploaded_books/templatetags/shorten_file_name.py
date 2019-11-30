from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def shorten_file_name(value):
	# splits the string into a list and takes the last element - which is the extension, and adds "." in front of it
	extension = '.' + value.split('.')[-1]
	# takes everyother element but removes the extension - we could make it take the first element, but there might be a filename with dots mixed with the name
	value_without_ext = value.replace(extension, "")

	# returns the first 15 characters of the file name and the extension at the end
	return value_without_ext[:15] + extension
