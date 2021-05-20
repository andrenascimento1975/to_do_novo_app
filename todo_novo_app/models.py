from django.db import models
from django.contrib.auth.models import User

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.nome_grupo

class Sub_Grupos(models.Model):
    nome_subgrupo = models.CharField(max_length=100, null=False, blank=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='subgrupos')

    def __str__(self):
        return self.nome_subgrupo

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefa_grupos')
    sub_grupo = models.ForeignKey(Sub_Grupos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefa_subgrupos')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']