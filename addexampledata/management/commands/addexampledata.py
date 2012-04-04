from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.importlib import import_module

class Command(BaseCommand):
    args = '[myapp] [another_app] ...'
    help = ''

    def handle(self, *args, **options):
        appnames = args
        verbosity = int(options.get('verbosity', '2'))

        for appname in appnames:
            if not appname in settings.INSTALLED_APPS:
                raise CommandError('App not in INSTALLED_APPS: {0}'.format(appname))
        for appname in settings.INSTALLED_APPS:
            if appnames and not appname in appnames:
                continue
            modulepath = '{0}.exampledata'.format(appname)
            try:
                mod = import_module(modulepath)
            except ImportError, e:
                if appname in appnames:
                    raise CommandError('Could not import {0}'.format(modulepath))
                else:
                    if verbosity > 1:
                        print '{0} not found'.format(modulepath)
                    continue
            else:
                if verbosity > 0:
                    print 'Adding exampledata from:', modulepath
                mod.add_exampledata()
