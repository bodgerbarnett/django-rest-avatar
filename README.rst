=============================
django-rest-avatar
=============================

.. image:: https://badge.fury.io/py/django-rest-avatar.svg
    :target: https://badge.fury.io/py/django-rest-avatar

.. image:: https://travis-ci.org/bodgerbarnett/django-rest-avatar.svg?branch=master
    :target: https://travis-ci.org/bodgerbarnett/django-rest-avatar

.. image:: https://codecov.io/gh/bodgerbarnett/django-rest-avatar/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bodgerbarnett/django-rest-avatar

A django app for handling user avatars using Django Rest Framework

Documentation
-------------

The full documentation is at https://django-rest-avatar.readthedocs.io.

Quickstart
----------

Install django-rest-avatar::

    pip install django-rest-avatar

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_avatar.apps.DjangoRestAvatarConfig',
        ...
    )

Add django-rest-avatar's URL patterns:

.. code-block:: python

    from rest_avatar import urls as rest_avatar_urls


    urlpatterns = [
        ...
        url(r'^', include(rest_avatar_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l
