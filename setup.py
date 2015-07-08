import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'django_kittens/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='django-kittens',
    version=get_version(),
    description='Add kittens and kitten voting to your django project!',
    long_description=open('README.rst').read(),
    url='https://github.com/Wilduck/django-kittens',
    author='Erik Swanson',
    author_email='TheErikSwanson@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django :: 1.8',
    ],
    license='MIT',
    package_data={
        'django_kittens': [
            'templates/kittens/*.html',
            'static/kittens/*.css',
        ]
    },
    install_requires=[
        'django>=1.8',
        'praw',
    ],
    tests_require=[
        'django-nose',
        'mock>=1.0.1',
        'django-dynamic-fixture',
    ],
    setup_requires=[
        'nose>=1.0',
    ],
    test_suite="run_tests.run_tests",
    zip_safe=False,
)
