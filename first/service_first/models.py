from django.db import models

class Status( models.Model):
    description = models.CharField(max_length=500)
    body = models.TextField(max_length=500)
    code = models.IntegerField(null=False)
    def __str__(self):
        return self.code

class Job(models.Model):
    durability = models.IntegerField(null=False)
    category = models.CharField(max_length=200)
    subJobs = models.IntegerField(null = False, default= 0)
    def __str__(self):
        return self.category+"_"+self.durability+"_"+self.subJobs
