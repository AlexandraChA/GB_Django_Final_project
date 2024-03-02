from django.core.management.base import BaseCommand
from MyApp.models import Good
import datetime


class Command_create_good(BaseCommand):
    help = "Create product."
    def handle(self, name, desc, price, quantity):
        good = Good(name=name, desc=desc,
        price=price, quantity=quantity, adding_date = datetime.date(2024, 2, 17))
        good.save()
        self.stdout.write(f'{good}')
