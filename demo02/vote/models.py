from django.db import models


# Create your models here.


class Topics(models.Model):
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class Options(models.Model):
    option_name = models.CharField(max_length=50)
    time = models.IntegerField(default=0)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)

    def __str__(self):
        return self.option_name
