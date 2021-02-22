=====
Usage
=====

To use django-rest-avatar in a project, add it to your `INSTALLED_APPS`:

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
