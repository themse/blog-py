from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.caption}'


class Post(models.Model):
    title = models.CharField(max_length=50, validators=[
        MinLengthValidator(3), MaxLengthValidator(50)
    ])
    slug = models.SlugField(null=False, unique=True)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("blog-post-detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f'{self.title}'
