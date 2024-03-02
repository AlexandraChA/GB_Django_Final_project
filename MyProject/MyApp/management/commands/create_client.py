from django.core.management.base import BaseCommand
from MyApp.models import Client
import datetime


class Command_create(BaseCommand):
    help = "Create client."
    def handle(self, name, email, phone, city):
        client = Client(name=name, email=email,
        phone_number=phone, address=city, registr_date = datetime.date(2024, 2, 17))
        client.save()
        self.stdout.write(f'{client}')
