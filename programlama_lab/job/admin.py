from django.contrib import admin
from . models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
# Register your models here.
