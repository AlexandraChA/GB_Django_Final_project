from django.shortcuts import render
import logging
from .management.commands.create_client import Command_create
from .management.commands.get_client import Command_get
from .management.commands.update_client import Command_update
from .management.commands.delete_client import Command_delete
from .management.commands.create_orders import Command_create_order
from .management.commands.create_products import Command_create_good
from .management.commands.get_order import Command_get_orders_clientID
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm
from random import choice, randint
from django.http import HttpResponse
import datetime
from .models import Good

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page was requested.')
    return render(request, "index.html")

def create_clients(request):
    logger.info('Page of creating users was requested.')
    names = ['Alex', 'John', 'Lisa']
    emails = ['a@mail.ru', 'j@gmail.com', 'l@example.com']
    phones = ['789567', '89996721', '908667']
    addresses = ['Moscow', 'Saint Petersburg', 'Kazan']
    for _ in range(5):
        name = choice(names)
        email = choice(emails)
        phone = choice(phones)
        city = choice(addresses)
        command = Command_create()
        command.handle(name, email, phone, city)
    return HttpResponse('Five clients were created')

def create_goods(request):
    logger.info('Page of creating products was requested.')
    names = ['Face mask', 'Lotion', 'Perfume', 'Mascara', 'Polish', 'Shower gel', 'Hands cream']
    for _ in range(10):
        name = choice(names)
        desc = f'Description for {name}'
        price = randint(15, 40)
        quantity = randint(10, 50)
        command = Command_create_good()
        command.handle(name, desc, price, quantity)
    return HttpResponse('Ten products were created')

def create_orders(request):
    logger.info('Page of creating orders was requested.')
    for _ in range(25):
        client = choice([3,4,5,6,7,8,9,10])
        command_client = Command_get()
        client = command_client.handle(client)
        goods_id = choice([1,2,3,4,5,6,7,8,9,10])
        goods = Good.objects.filter(id=goods_id)
        total_price = randint(30, 100)
        day = randint(1, 28)
        month = randint(1, 12)
        order_date = datetime.date(2024, month, day)
        command = Command_create_order()
        order = command.handle(client, total_price, order_date)
        order.goods.set(goods)
        order.save()
    return HttpResponse('Twenty five orders were created')

def get_client(request):
    logger.info('Get client by id page was requested.')
    command = Command_get()
    id = choice([1,2,3])
    client = command.handle(id)
    return HttpResponse(f'Client with id {id} is : {client}')

def get_all_client(request):
    logger.info('Get all clients page was requested.')
    clients = []
    command = Command_get()
    client = 0
    i = 1
    while client != None:
        client = command.handle(i)
        if client != None:
            clients.append(str(client))
        i += 1
    return HttpResponse(f'All clients are: {clients}')

def update_client_name(request):
    logger.info('Updating client page was requested.')
    command = Command_update()
    id = choice([1,2,3])
    name = choice(['George', 'Ron'])
    client = command.handle(id, name)
    return HttpResponse(f'Client {client} was updated')

def delete_client(request):
    logger.info('Deleting client page was requested.')
    command = Command_delete()
    id = choice([1,2,3])
    client = command.handle(id)
    return HttpResponse(f'Client {client} was deleted')

def get_client_orders(request, id):
    logger.info('Getting client orders page was requested.')
    command = Command_get_orders_clientID()
    orders, goods = command.handle(id)
    client_info = orders[0][orders[0].find('client:'):orders[0].find(', products')]
    context = dict()
    context['client_info'] = client_info
    final_orders_7 = []
    final_orders_30 = []
    final_orders_365 = []
    for i, ord in enumerate(orders):
        days_from_order = (datetime.datetime.strptime('2024-12-31', '%Y-%m-%d') - datetime.datetime.strptime(ord[ord.find('order date:')+12:], '%Y-%m-%d')).days
        if days_from_order <= 7:
            final_orders_7.append(f"Order №{i+1}: {ord[ord.find('total'):]}")
        if days_from_order <= 30:
            final_orders_30.append(f"Order №{i+1}: {ord[ord.find('total'):]}")
        if days_from_order <= 365:
            final_orders_365.append(f"Order №{i+1}: {ord[ord.find('total'):]}")
    context['client_orders_7'] = final_orders_7
    context['client_orders_30'] = final_orders_30
    context['client_orders_365'] = final_orders_365
    final_products_7 = []
    final_products_30 = []
    final_products_365 = []
    for k,v in goods.items():
        res_7 = [i for i in final_orders_7 if k in i]
        if res_7 != []:
            final_products_7.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
            final_products_30.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
            final_products_365.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
        res_30 =[i for i in final_orders_30 if k in i]
        if res_7 == [] and res_30 != []:
            final_products_30.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
            final_products_365.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
        res_365 = [i for i in final_orders_365 if k in i]
        if res_7 == [] and res_30 == [] and res_365 != []:
            final_products_365.append(f"Product №{i+1}{v[v.find(': '):v.find('descr')]} {v[v.find('price'):v.find(', quan')]}")
    context['client_orders_products_7'] = final_products_7
    context['client_orders_products_30'] = final_products_30
    context['client_orders_products_365'] = final_products_365
    if final_products_7 != []:
        context['client_orders_products_7'] = final_products_7
    else:
        context['client_orders_products_7'] = ['Товаров за данный период нет']
    if final_products_30 != []:
        context['client_orders_products_30'] = final_products_30
    else:
        context['client_orders_products_30'] = ['Товаров за данный период нет']
    if final_products_365 != []:
        context['client_orders_products_365'] = final_products_365
    else:
        context['client_orders_products_365'] = ['Товаров за данный период нет']
    return render(request, "get_client_orders.html", context = context)


def add_product_manually(request):
    logger.info('Uploading new product page was requested.')
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = form.cleaned_data['photo']
            logger.info(f'Получили {name=}, {desc=}, {price=}, {quantity=}.')
            good = Good(name=name, desc=desc, price=price, quantity=quantity, adding_date = datetime.datetime.now(), photo = photo)
            good.save()
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            message = 'Продукт сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'product_form.html', {'form': form, 'message': message})
