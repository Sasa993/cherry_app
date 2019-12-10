from django.core.exceptions import ValidationError


def validate_underscore(value):
	if "_" not in value:
		raise ValidationError("It needs to have an underscore (_)!")
	else:
		return value


def validate_alpha_before_underscore(value):
	if "_" in value:
		splited_value = value.split('_')
		if splited_value[0].isalpha():
			return value
		else:
			raise ValidationError("Before the underscore, letters are only allowed!")


def validate_digits_after_underscore(value):
	if "_" in value:
		splited_value = value.split('_')
		if splited_value[1].isdigit():
			return value
		else:
			raise ValidationError("After the underscore, digits are only allowed!")


def validate_two_letters(value):
	if "_" in value:
		splited_value = value.split('_')
		if len(splited_value[0]) == 2 or len(splited_value[0]) == 3:
			return value
		else:
			raise ValidationError("It is only allowed to have two or three letters before the underscore!")
