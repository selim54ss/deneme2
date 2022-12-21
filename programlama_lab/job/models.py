from django.db import models

class Job(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    ) 
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=300)
    image = models.ImageField(blank=True, upload_to='images/', null=True)
    detail = models.TextField()
    #userid = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    #category_id = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    price = models.FloatField()
    months = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)
    # Create your models here.
