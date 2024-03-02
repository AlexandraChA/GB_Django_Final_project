from django.core.management.base import BaseCommand
from MyApp.models import Client


class Command_delete(BaseCommand):
    help = "Delete client by id."

    def handle(self, id):
        pk = id
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')
        return client
