# (1) Returns all customers from the customer table
customers = Customer.objects.all()

# (2) Returns the first customer in the table
firstCustomer = Customer.objects.first()

# (3) Returns the last customer in the table
lastCustomer = Customer.objects.last()

# (4) Returns a single customer by name
customerByName = Customer.objects.get(name='Peter Piper')

# (5) Returns a single customer by ID
customerById = Customer.objects.get(id=4)

# (6) Returns all orders related to the customer
# (firstCustomer variable set above)
firstCustomer.order_set.all()

# (7) Returns the customer name for a specific order
order = Order.objects.first()
parentName = order.customer.name

# (8) Returns products from the products
# table with the value "Out Door" in the category attribute
products = Product.objects.filter(category="Out Door")

# (9) Order/Sort Objects by ID
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10) Returns all products with the tag "Sports" (Query Many-to-Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

# (11) Bonus
# Q: If the customer has more than 1 ball, how would
# you reflect it in the database?
# A: You would likely not want to store this
# value in the database but rather create a function to
# calculate it when needed.

# Returns the total count for the number
# of times a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# Returns the total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}

# RELATED SET EXAMPLE


class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)
    parent = ParentModel.objects.first()
# Returns all child models related to the parent
    parent.childmodel_set.all()
