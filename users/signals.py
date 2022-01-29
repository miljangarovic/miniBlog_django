from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver

# @receiver(post_save,sender=Profile) #drugi nacin za javljanje dodatnih informacija
def createProfile(sender, instance, created,**kwargs): #sender je klasa ciji se objekat mijenja, instance je objekat koji treba da bude updateovan, a created je boolean koji govori da li je update obavljen
    if created:
        user = instance #ovo ce da bude objekat klase User
        profile = Profile.objects.create( #na osnovu User objekta kreiramo Profile objekat gdje koristimo njegove podatke
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name + ' ' + user.last_name,
        )

def deleteUser(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False: #ako ga ne pravimo prvi put, nego ga updateujemo
        # user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()



post_save.connect(createProfile,sender=User) #svaki put kad je napravljen novi user, pokreni createdProfile funkciju, koja ce
# da napravi novi Profile objekat koji odgovara tom User objektu
# post_save.connect(updateUser,sender=Profile)

post_delete.connect(deleteUser,sender=Profile) # instance je profil koje se brise, a to ujedno poziva i funkciju deleteUser koja
#pomocu OneToOne relacije pronalazi User-a kojem odgovara profil koji se brise, i zatim brise datog user-a

