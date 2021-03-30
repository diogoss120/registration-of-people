from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    years_old = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField()
    nickname = models.CharField(max_length=30, null=True, blank=True)
    obervation = models.CharField(max_length=50, null=True, blank=True)

    def info_to_dict(self):
        data = {}
        data["id"] = self.id
        data["last_name"] = self.last_name
        data["years_old"] = self.years_old
        data["birth"] = self.birth
        data["email"] = self.email
        data["nickname"] = self.nickname
        data["obervation"] = self.obervation
        return data

    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'People'
        ordering = ["name","last_name"]


#e, idade, data de
#nascimento, e-mail, apelido e observação;
#
"""
Os campos nome, sobrenome, idade, data de nascimento e e-mail são
obrigatórios;

"""