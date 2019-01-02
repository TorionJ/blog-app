from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

# reverse helps us to reference and object by its URL template name.
# Django docs recommends using self.id with get_absolut_url
# reverse grabs the post_detail absolute url from the urls.py and the primary key via args=[str(self.id)]