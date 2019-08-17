from django.db import models


class Area(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class Pgs(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=510)
    amen = models.TextField(max_length=510)
    address = models.CharField(max_length=255)
    ph_no = models.CharField(max_length=30)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    category = models.ForeignKey('Gender', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
