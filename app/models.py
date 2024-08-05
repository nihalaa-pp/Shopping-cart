from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = {
    ('TAMILNADU','TAMILNADU'),
    ('KERALA','KERALA'),
    ('GOA','GOA'),
    ('KARNATAKA','KARNATAKA'),



}

CATEGORY_CHOICES=(
('VG','Vegitables'),
('FR','Fruits'),
('GH','Ghee'),
('CD','Curd'),
('IC','icecreams'),
('HM','Home and Kitchen'),
('ML','milk'),
('SS','Snacks Store'),
('CH','Cleaning & Household'),
('DS','Daily Staples'),
('BS','Beverages'),
('BH','beauty and hygiene'),


)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='products')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price   

class ProductVariant(models.Model):
    # Define fields for ProductVariant model
    product = models.ForeignKey('Product', related_name='variants', on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)
    variant_price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.title} - {self.variant_name}"