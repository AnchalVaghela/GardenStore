from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator,RegexValidator

# Create your models here.
CATEGORY_CHOICES =(
    ('PL','Plants'),
    ('T','Tools'),
    ('FE','Fertilizers'),
    ('DCP','Disease'),
    ('FL','Flowers'),
    ('P','Pots'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    #composition = models.TextField(default='')
    #prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    alphaSpaces = RegexValidator(r'^[a-zA-Z]+$')
    name=models.TextField(max_length=200,validators=[alphaSpaces])
    #locality = models.TextField(max_length=200,validators=[alphaSpaces])
    locality = models.CharField(max_length=200)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{10}$')
    mobile= models.CharField(validators=[phone_regex],max_length=11,blank=True)
    zip_regex=RegexValidator(regex=r'^\+?1?\d{6}$')
    zipcode = models.CharField(validators=[zip_regex],max_length=7,blank=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50,choices=STATUS_CHOICES,default="Pending")
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cart(self):
        return self.quantity * self.product.discounted_price


SERVICE_CHOICES = (
    ("Landscaping", "Landscaping"),
    ("Lawn Care", "Lawn care"),
    )
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user} | day: {self.day} | time: {self.time}"

class Wishlist (models .Model) :
    user=models.ForeignKey (User, on_delete=models.CASCADE )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)