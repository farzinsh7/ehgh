from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=120, null=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return self.question