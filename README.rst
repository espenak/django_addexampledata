Easily bundle example data with your django apps.

Install
=======

::

    $ pip install django_addexampledata


Setup
=====

Add ``'django_addexampledata'`` to ``INSTALLED_APPS``.



Usage
=====

``django_addexampledata`` provides two Django management commands:

    addexampledata
        Finds all apps with an ``exampledata.py``, and runs
        ``appname.exampledata.add_exampledata()`` on these apps.
        See the howto below for more info.

    createexampleuser
        Create an example user. See ``--help`` for the User attributes that can be set.
        Example::

            python manange.py createexampleuser grandma --is-superuser
            
        creates a superuser named grandma with password set to ``test``.
    

addexampledata howto
--------------------

Add ``exampledata.py`` to the root of your Django app (in the same directory as
``models.py``). Add an ``add_exampledata`` function to this module. Your
``exampledata.py`` may look something like this::

    from models import Page

    def add_exampledata():
        aboutus = Page.objects.create(title="About us",
                                      body="Hello cruel world")
        contactinfo = Page.objects.create(title="Contact info",
                                          body="Coming soon.",
                                          parent=aboutus)

As long as your Django app is in INSTALLED_APPS,
``<appname>.exampledata.add_exampledata`` is run each time you run::

    python manage.py addexampledata


addexampledata on specific apps
-------------------------------

You can specify the apps that you want to add example data for as arguments for
the command. Example::

    python manage.py addexampledata myapp myotherapp


addexampledata adds the same data each time it runs!
----------------------------------------------------

You can solve this in two ways:

1. *(reccommended)* Add a make target or something similar (we use a Fabric
   action) to reset your example database and re-run ``addexampledata``. Use
   this action whenever you change/add models or exampledata.
2. Check for existing items in ``add_exampledata()`` before inserting new data.
