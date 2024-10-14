from django.db import models #type:ignore
class Post(models.Model):
    title=models.CharField(max_length=250,null=False)
    author=models.CharField(max_length=300,null=False)
    content=models.CharField(max_length=300,null=False)


