from django.db import models

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

    class Meta:
        verbose_name_plural = 'People'
        ordering = ["name","last_name"]
