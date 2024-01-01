from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    # tags = TaggableManager()
    # counted_views = models.IntegerField(null=True, default=0)
    status = models.BooleanField(default=False,)
    # login_require = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[:10]
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
