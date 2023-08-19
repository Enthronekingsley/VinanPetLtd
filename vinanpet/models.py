from django.db import models

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=300)

    def __str__(self):
        return self.branch

class Product(models.Model):
    product = models.CharField(max_length=300)

    def __str__(self):
        return self.product


class Tank(models.Model):
    tank = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.tank

class Pump(models.Model):
    pump = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.pump


class VinanPetLtd(models.Model):
    transaction_Date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    entry_Date = models.DateTimeField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    tank_Opening = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    tank_Closing = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    tank_Difference = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE, null=True)
    pump_Opening = models.FloatField(null=True)
    pump_Closing = models.FloatField(null=True)
    pump_Difference = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    price = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    pos = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    cash = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    expenses = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    balance = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    amount_Deposited = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    teller_ID = models.IntegerField(null=True)
    teller = models.ImageField(upload_to="teller", null=True)
