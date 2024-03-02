from django.core.management.base import BaseCommand
from MyApp.models import Good


class Command_get_good(BaseCommand):
    help = "Get good by id."

    def handle(self, id):
        id = id
        good = Good.objects.filter(pk=id).first()
        self.stdout.write(f'{good}')
        return good