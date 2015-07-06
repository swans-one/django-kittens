import os

from django.conf import settings


def configure_settings():
    """
    Configures settings for manage.py and for run_tests.py.
    """
    if not settings.configured:
        db_config = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'django_kittens',
        }

        settings.configure(
            TEST_RUNNER='django_nose.NoseTestSuiteRunner',
            NOSE_ARGS=['--nocapture', '--nologcapture', '--verbosity=1'],
            DATABASES={
                'default': db_config,
            },
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'django_kittens',
                'django_kittens.tests',
            ),
            ROOT_URLCONF='django_kittens.urls',
            DEBUG=False,
            MIDDLEWARE_CLASSES=(),
        )
