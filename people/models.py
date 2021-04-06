from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    years_old = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()
    nickname = models.CharField(max_length=30, null=True, blank=True)
    obervation = models.TextField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('edit-person', args=[int(self.id)])

    class Meta:
        verbose_name_plural = 'People'
        ordering = ["name","last_name"]
