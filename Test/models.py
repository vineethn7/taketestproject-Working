from django.db import models

# Create your models here.


class TestM(models.Model):
    TestName = models.CharField(max_length=255)
    MaxMarks = models.IntegerField()
    TimeDuration = models.IntegerField()
    PosMarks = models.IntegerField()
    NegMarks = models.IntegerField()

    InputTextFile = models.FileField(upload_to='Test/TestName/', blank=True, null=True)

    def __str__(self):
        return f'{self.TestName}'
