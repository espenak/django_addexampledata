from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<username>'
    help = 'Create an exampleuser.'
    option_list = BaseCommand.option_list + (
        make_option('--password',
            dest='password',
            default="test",
            help='Password for the created user. Defaults to "test".'),
        make_option('--first-name',
            dest='first_name',
            default='',
            help='First name.'),
        make_option('--last-name',
            dest='last_name',
            default='',
            help='Last name.'),
        make_option('--is-staff',
            action='store_true',
            dest='is_staff',
            default=False,
            help='Set is_staff to True.'),
        make_option('--is-superuser',
            action='store_true',
            dest='is_superuser',
            default=False,
            help='Set is_superuser to True.'),
        )

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Username is required. See --help.')
        username = args[0]
        user = User(username=username,
                    first_name=options['first_name'],
                    last_name=options['last_name'],
                    is_superuser=options['is_superuser'],
                    is_staff=options['is_staff'])
        user.set_password(options['password'])
        user.full_clean()
        user.save()
