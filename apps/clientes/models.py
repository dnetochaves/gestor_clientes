from django.db import models


class Docs(models.Model):
    type_name = models.CharField(max_length=100)
    number = models.IntegerField()
    note = models.TextField(null=True, blank=True)

    def listar_docs():
        return Docs.objects.all()

    def __str__(self):
        return self.type_name


class Person(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)
    doc = models.OneToOneField(
        Docs, null=True, blank=True, on_delete=models.PROTECT)
    
    def list_persons():
        return Person.objects.all()
    
    def __str__(self):
        return self.frist_name
