from django.db import models

# Create your models here.
from django.db import models
from author.models import Author

# Create your models here.

class TimeStampedBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Blog(TimeStampedBaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, related_name='author_blogs', on_delete=models.PROTECT)
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class BaseTimeStampModel(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class CoverImage(BaseTimeStampModel):
    image_link = models.URLField()
    blog = models.OneToOneField(Blog, related_name='blog_ci', on_delete=models.PROTECT)
