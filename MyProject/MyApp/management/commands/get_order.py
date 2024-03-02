from django.core.management.base import BaseCommand
from MyApp.models import Order


class Command_get_orders_clientID(BaseCommand):
    help = "Get orders by client id."

    def handle(self, id):
        id = id
        orders = []
        goods = dict()
        order = Order.objects.filter(client_id=id)
        for ord in order:
            goods[str(ord)[str(ord).find('total price'): ]] = str(ord.goods.get())
            orders.append(str(ord))
        self.stdout.write(f'{orders}')
        return orders, goods