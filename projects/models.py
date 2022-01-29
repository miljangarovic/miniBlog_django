from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True) #null je database requirement a blank je  django(kada ga koristimo u formi) requirement
    featured_image = models.ImageField(null=True,blank=True,default='default.jpg') # slika ce se uplodovati u MEDIA_ROOT iz settings.py
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) #ovo polje ne moramo da unosimo

    def __str__(self):
        return self.title
    class Meta:
        ordering= ['-created','title']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
