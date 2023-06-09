from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    picture = models.TextField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png', null=True, blank=True)
    def __str__(self):
        return self.username

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    sleep = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    diary = models.TextField(blank=True)
    class Meta:
        unique_together = ('user', 'date')
    def __str__(self):
        return str(self.user) + ' ' + str(self.date)

class Water(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    def __str__(self):
        return str(self.entry.user) + ' ' + str(self.entry.date)

class Food(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    amount = models.CharField(max_length=50, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.entry.user) + ' ' + str(self.entry.date)

class Exercise(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    calories = models.IntegerField(null=True, blank=True)
    links = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return str(self.entry.user) + ' ' + str(self.entry.date)