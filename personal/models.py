from django.db import models

class Table(models.Model):
    title_one = models.CharField(max_length=100)
    title_two = models.CharField(max_length=100)
    title_three = models.CharField(max_length=100)
    title_four = models.CharField(max_length=100)
    title_five = models.CharField(max_length=100)
    title_six = models.CharField(max_length=100)

    def __str__(self):
        return self.title_one
