from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="authors/", null=True, blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="articles/", null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default='draft')

    def __str__(self):
        return self.title
    
    @property
    def is_published():
        return self.status == 'published'
