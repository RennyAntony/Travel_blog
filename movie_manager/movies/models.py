from django.db import models


# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    certified_by=models.CharField(max_length=200,null=True)

class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField()
    img=models.ImageField(upload_to='images/', null=True)
    censor_details=models.OneToOneField(
        CensorInfo,on_delete=models.SET_NULL,
        related_name='movie',null=True)
    def __str__(self):
        return self.title

class Director(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name 

#Commands to write inside python shell to create new objects after writing: 'python3 manage.py shell'

# >>> from movies.models import CensorInfo,MovieInfo
# >>> censor2=CensorInfo.objects.create(rating='a',certified_by="Sam")
# >>> censor2
# <CensorInfo: CensorInfo object (3)>
# >>> lol2=MovieInfo.objects.get(title="leo")
# >>> lol2
# <MovieInfo: leo>
# >>> lol2.censor_details=censor2
# >>> lol2.save()
# >>> lol2.censor_details
# <CensorInfo: CensorInfo object (3)>