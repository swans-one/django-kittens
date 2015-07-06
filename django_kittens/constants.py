from django.conf import settings

KITTEN_HOMEPAGE = getattr(settings, 'KITTEN_HOMEPAGE', '/')
KITTEN_FRESHNESS = getattr(settings, 'KITTEN_FRESHNESS', 100)
REDDIT_USER_AGENT = getattr(settings, 'REDDIT_USER_AGENT', 'django-kittens')
