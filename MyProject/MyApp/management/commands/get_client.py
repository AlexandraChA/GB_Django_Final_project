from django.core.management.base import BaseCommand
from MyApp.models import Client


class Command_get(BaseCommand):
    help = "Get client by id."
    # def add_arguments(self, parser):
    #     parser.add_argument('id', type=int, help='Client ID')

    def handle(self, id):
        id = id
        client = Client.objects.filter(pk=id).first()
        self.stdout.write(f'{client}')
        return client
