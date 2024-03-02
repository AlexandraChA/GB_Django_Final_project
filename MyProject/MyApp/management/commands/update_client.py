from django.core.management.base import BaseCommand
from MyApp.models import Client


class Command_update(BaseCommand):
    help = "Update client name by id."

    def handle(self, id, name):
        id = id
        name = name
        client = Client.objects.filter(pk=id).first()
        client.name = name
        client.save()
        self.stdout.write(f'{client}')
        return client
