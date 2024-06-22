from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)
    demo_field = models.TextField(default='demo')
 
    class Meta:
        indexes = [
            models.Index(fields=['first_name']),
        ]

    def __str__(self):
        return f'{self.name}-{self.id}'