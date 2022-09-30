from django.db import models

# Create your models here.
class Ztype(models.Model):
    Category = models.CharField(max_length=50);

    def __str__(self):
        return self.Category


class Task(models.Model):
    title = models.CharField(max_length=80, null=True)
    ztype = models.ManyToManyField(Ztype, null=True, blank=True)
    script = models.CharField(max_length=400, null=True)
    iloc = models.CharField(max_length=100, null=True)
    banner = models.CharField(max_length=100, null=True)
    target_count = models.IntegerField(default=0)
    time = models.CharField(max_length=7, null=True)

    def __str__(self):
        return (str(self.id )+ self.title)

class Challange(models.Model):
    title = models.CharField(max_length=200, null=True)
    task = models.OneToOneField(Task, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
