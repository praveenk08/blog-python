from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from - " + self.name +"  " + self.email

class product(models.Model):
    product_id = models.AutoField
    product_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    desc = models.TextField(max_length=200)
    pub_date = models.DateField()
    slug = models.CharField(max_length=150, default="")
    author = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_title + ' by '  +self.author

