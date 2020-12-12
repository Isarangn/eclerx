from django.db import models

# Create your models here.

class Test(models.Model):
    no = models.IntegerField(null=True, blank=True)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)
    corans = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = "onlineexam"