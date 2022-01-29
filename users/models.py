from django.db import models
from django.contrib.auth.models import User #ovo nam omogucava da koristimo User tabelu (ne moramo sami da je pravimo)
import uuid
from django.db.models.signals import post_save,post_delete #signal koji se dobija nakon sto je objekat sacuvan
from django.dispatch import receiver #drugi nacin za signals (decorators)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=300,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image_link = models.CharField(null=True,blank=True,max_length=400)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png') #po defaultu ce se cuvati u root/static/images jer smo tako podesili u settings
    # profiles/ znaci kad se nadjes u podeseni direktorijum za uploadovanje (root/static/images), udji u profiles/ i tamo cuvaj podatke
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering=['created']





