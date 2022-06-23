from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=100)
    primarycat=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    miniimage=models.ImageField(upload_to='ecom/', default='')
    slug=models.SlugField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text=models.CharField(max_length=254, verbose_name='Preview Text')
    detail_text=models.CharField(max_length=254, verbose_name='Detail Text')
    price=models.FloatField(default=0)

    def __str__(self):
        return self.name



