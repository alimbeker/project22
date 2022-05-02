from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>150000000:
        raise ValidationError("maximum size is 150 mb")