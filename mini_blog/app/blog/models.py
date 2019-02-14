from django.db import models
import string, random

length = 5

def gen_id():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    cover = models.ImageField(upload_to="posts/", null=True)
    caption = models.CharField(max_length=150, null=True, blank=True)
    date =models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, default=gen_id(), editable=False, unique=True)

    def __str__(self):
        return self.title

class PageIcon(models.Model):
    icon = models.ImageField(upload_to="icon/", null=True)
    def __str__(self):
        return self.icon.url