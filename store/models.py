from django.db import models


# Create your models here.
# check this link for more info: https://docs.djangoproject.com/en/4.1/ref/models/fields/

# notice !! django will create a table for each model in the database with the name of the model and an id field


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True,related_name='+')
    # related_name='+' means that we don't want to access the collection from the product model


class Product(models.Model):
    title = models.CharField(max_length=255)  # varchar(255)
    description = models.TextField()  # text
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)  # avoid float because of rounding issues
    inventory = models.IntegerField()  # int
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    last_update = models.DateTimeField(auto_now=True)  # datetime
# NOTICE!! if you want to add a reference to another model that is not defined yet, use the string name of the model
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    # on_delete=models.PROTECT will prevent the deletion of the collection if there are products that reference it
    promotions = models.ManyToManyField(Promotion) # many-to-many relationship


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # never delete order if customer is deleted ( it represents our sales )
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    payment_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # never delete order item if order is deleted
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # never delete order item if product is deleted
    quantity = models.PositiveSmallIntegerField()
    # positive small integer (0-255)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    # store the price at the time of purchase because it may change later


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)




