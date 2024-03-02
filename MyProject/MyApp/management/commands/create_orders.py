from django.core.management.base import BaseCommand
from MyApp.models import Order
import datetime


class Command_create_order(BaseCommand):
    help = "Create order."
    def handle(self, client, total_price, order_date):
        order = Order(client=client, total_price=total_price,order_date = order_date)
        order.save()
        self.stdout.write(f'{order}')
        return order