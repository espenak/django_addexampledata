from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.importlib import import_module


class Command(BaseCommand):
    args = '[myapp] [another_app] ...'
    help = ''

    def handle(self, *args, **options):
        appnames = args
        for appname in settings.INSTALLED_APPS:
            if appnames and not appname in appnames:
                continue
            modulepath = '{0}.exampledata'.format(appname)
            try:
                mod = import_module(modulepath)
            except ImportError, e:
                continue
            else:
                mod.add_exampledata()
