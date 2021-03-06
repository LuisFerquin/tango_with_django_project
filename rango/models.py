from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    url = models.URLField()
    class Meta:
        verbose_name_plural = "categories"
    def __unicode__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class PageAdmin(admin.ModelAdmin):
        list_display = ('title', 'category', 'url', 'views')
        list_filter = ['category']