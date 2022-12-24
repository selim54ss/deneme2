from django.db import models


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    ) 
    title = models.CharField(max_length=50, null=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(blank=True, max_length=400)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title


class Job(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    ) 
    
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=300, help_text="")
    image = models.ImageField(blank=True, null=True)
    detail = models.TextField()
    category_id = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    months = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)
    # Create your models here.

    def __str__(self):
       return self.title

    