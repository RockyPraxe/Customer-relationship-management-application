from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# Customer: Represents customer data. It includes user-related
# information like name, phone, email, and a reference to the associated User.
# Also, keeps track of the date the customer was created.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Unnamed Object"


# Tag: Represents product tags. Used to categorize products.
# It includes a name field to describe the tag.


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


# Product: Represents products that can be ordered.
# Contains fields for name, price, category, description, date created,
# and tags. Category is chosen from predefined choices.


class Product(models.Model):
    CATEGORY = (
        ('Nutritional supplement', 'Nutritional supplement'),
        ('Training aids', 'Training aids'),
            )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


# Order: Represents customer orders. It links a customer to a product,
# includes the order date, status (with predefined choices),
# and an optional note.


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
