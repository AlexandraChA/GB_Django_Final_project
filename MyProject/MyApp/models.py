from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    registr_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, phone_nimber: {self.phone_number}, address: {self.address}, registratind date: {self.registr_date}'

class Good(models.Model):
    name = models.CharField(max_length=100)
    desc =  models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    adding_date = models.DateField(auto_now_add = True)
    photo = models.ImageField(upload_to='media/',blank=True)


    def __str__(self):
        return f'Product: {self.name}, description: {self.desc}, price: {self.price}, quantity: {self.quantity}, adding date: {self.adding_date}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'Order, client: {self.client}, products: {self.goods}, total price: {self.total_price}, order date: {self.order_date}'

    def get_good(self): 
        return ",".join([str(p) for p in self.goods.all()])
