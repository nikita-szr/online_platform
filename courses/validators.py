from django.core.exceptions import ValidationError
from urllib.parse import urlparse


def validate_youtube_url(value):
    parsed_url = urlparse(value)
    if not parsed_url.netloc.endswith('youtube.com') and not parsed_url.netloc.endswith('youtu.be'):
        raise ValidationError("Разрешены только ссылки на youtube.com или youtu.be")