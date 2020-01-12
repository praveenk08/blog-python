from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    desc = models.TextField(max_length=200)
    pub_date = models.DateField()
    slug = models.CharField(max_length=150, default="")
    author = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title + ' by '  +self.author