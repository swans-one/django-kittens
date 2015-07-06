Django Kittens
==============

Add kittens to your django project! This app collects kittens from the
`/r/aww`_ subreddit and displays them to users, who can then upvote or
downvote them. It also provides a "top kittens page"

This project was created to demonstrate how to package a django app
for distribution. It accompanies the presentation given at this
`Code & Supply: Django PGH Meetup`_.

.. _`Code & Supply: Django PGH Meetup`: http://www.meetup.com/Pittsburgh-Code-Supply/events/223471063/

.. _`/r/aww/`: http://www.reddit.com/r/aww

Installation and Configuration
------------------------------

Installing django-kittens is as simple as:

.. code-block::

    pip install django-kittens

It can be included in any Django app by adding ``'django-kittens'`` to
you ``INSTALLED_APPS`` setting.

This application can be further configured by adding some entries into
your django settings module.

.. code-block:: python

    REDDIT_USER_AGENT = 'packaging-kittens'
    KITTEN_FRESHNESS = 100
    KITTEN_HOMEPAGE = '/'

The config item ``REDDIT_USER_AGENT`` tells the reddit-api who is
making requests. Set this to something unique for your app. If left at
the default setting, your rate limit will be shared with any other
project that includes this app with the default setting.

The ``KITTEN_FRESHNESS`` setting controls what proportion of kittens
will be new, and can be set to any positive integer. A low freshness
level will tend to show the same collection of kittens over time,
while a high freshness level will constantly show new kittens.

The setting ``KITTEN_HOMEPAGE`` is the url that the "home" link on the
kittens pages will link to.


Contributing
------------

This project is not being actively developed. But, I'm happy to look
at pull requests.


License
-------

All code is licensed under the MIT license. See attached LICENSE.txt.
