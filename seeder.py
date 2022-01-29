import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog.settings')

import django
django.setup()

from users.models import Profile
from django.contrib.auth.models import User
# from projects.models import Project
from faker import Faker

fake=Faker()

def populate(N=10):

    for person in range(N):
        #create fake data
        fake_password = fake.password()
        fake_firstname = fake.first_name()
        fake_lastname = fake.last_name()
        fake_email = fake_firstname.lower() + fake_lastname.lower()+'@gmail.com'
        fake_image = fake.image_url()
        fake_username= fake_firstname.lower() + fake_lastname.lower()+str(fake.pyint(min_value=1,max_value=99))
        fake_short_bio= fake.text(max_nb_chars=80)
        fake_bio = fake.text(max_nb_chars = 400 )
        fake_location=fake.city()+','+fake.country_code()
        fake_web = fake.uri()




        #Create new User
        user = User.objects.create(email = fake_email,username=fake_username,first_name=fake_firstname,last_name=fake_lastname,password=fake_password)
        profile = Profile.objects.create(user=user,name=user.first_name+' '+user.last_name,username=user.username,email=user.email)
        profile.profile_image_link=fake_image
        profile.location=fake_location
        profile.bio=fake_bio
        profile.social_github=fake_web
        profile.social_twitter=fake_web
        profile.social_website=fake_web
        profile.social_youtube=fake_web
        profile.social_linkedin=fake_web
        profile.save()

        #create project
        project = profile.project_set.create(title=fake_short_bio,description=fake_bio,featured_image=fake_image)

if __name__=='__main__':
    print('populating script!')
    populate(10)
    print("Populating complete")
