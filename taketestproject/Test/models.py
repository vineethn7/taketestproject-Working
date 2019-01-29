from django.db import models

# Create your models here.


class TestM(models.Model):
    TestName = models.CharField(max_length=100)
    MaxMarks = models.IntegerField()
    TimeDuration = models.IntegerField()
    PosMarks = models.IntegerField()
    NegMarks = models.IntegerField()
    InputTextFile = models.FileField()

    def __unicode__(self):
        return self.TestName
