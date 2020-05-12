'''
we use Models to incorporate a database into a Django Project

In the settings.py file you can edit the ENGINE parameter used for DATABASES
To create an actual model, we use a class structure inside of the relevant applications models.py file 
This class object will be a subclass of Django's built-in class: django.db.models.Model
After we've set up the models we can migrate teh database

an example of the models class that would go into the models.py file of your application
    class Topic(models.Model):
        top_name = models.CharField(max_length=264,unique=True)
    class Webpage(models.Model):
        category = models.ForeignKey(Topic)
        name = models.CharField(max_length=264)
        url = models.URLField()
        
        def __str__(self):
            return self.name
After set up models we can migrate the database
    python manage.py migrate
    python manage.py makemigrations app1
    python manage.py migrate

In order to usue the more convenient Admin interface with models 
however , we need to register them to our application's admin.py file
    from django.contrib import admin
    from app.models import Models1,Model2
    admin.site.register(Model1)
    admin.site.register(Model2)

Then with the models and database created, we can use Django's fantastic Admin interface to interact with the database
To create a "superuser"
    python manage.py createsuperuser
providing a username, mail and password

We use a library to help populate with some test data called Faker and create a script to do this
'''



# step1:
#first_project/first_app/models.py
    from django.db import models
    #https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # Create your models here.
    class Topic(models.Model):
        top_name = models.CharField(max_length=264,unique=True)
        def __str__(self):
            return self.top_name

    class Webpage(models.Model):
        topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
        name = models.CharField(max_length=264,unique=True)
        url = models.URLField(unique=True)
        def __str__(self):
           return self.name

    class AccessRecord(models.Model):
        name=models.ForeignKey(Webpage,on_delete=models.PROTECT)
        date=models.DateField()
        def __str__(self):
            return str(self.date)

# step2:
    python manage.py migrate
    python manage.py makemigrations first_app
    python manage.py migrate
    
    # to test if migrate is successful , we use shell 
      python manage.py shell
      print("hello")
      from first_app.models import Topic
      print(Topic.objects.all())
      t=Topic(top_name="Social Network")
      t.save()
      print(Topic.objects.all())
      quit()
    
# step3:we use Admin interface to add data
#first_project/first_app/admin.py
    from django.contrib import admin
    from first_app.models import AccessRecord,Topic,Webpage
    # Register your models here.
    admin.site.register(AccessRecord)
    admin.site.register(Topic)
    admin.site.register(Webpage)
# creat a superuser
    python manage.py createsuperuser
    Username:
    Email address:
    Password:
#running server to check on website
    python manage.py runserver
    
#Test  we use library Faker to create this script
#install:  
    pip install Faker
    #https://faker.readthedocs.io/en/master/
    
#under first level create first_project/populate_first_app.py
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")
    import django
    django.setup()

    ##FAKE POP SCRIPT
    import random
    from first_app.models import AccessRecord,Webpage,Topic
    from faker import Faker

    fakegen=Faker()
    topics=['Search','Social','Marketplace','News','Game']

    def add_topic():
        t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]#shell command
        t.save()
        return t

    def populate(N=5):
        for entry in range(N):
            #get the topic for the entry
            top=add_topic()
            #create the fake data for that entry
            fake_url=fakegen.url()
            fake_date=fakegen.date()
            fake_name=fakegen.company()
            #create the new Webpage entry
            webpage=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
            #create a fake access record for that webpage
            acc_rec=AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

    if __name__=='__main__':
        print("populating script!")
        populate(20)
        print("populating complete!")
#test if it is right:
    python populate_first_app.py
#run website
    python manage.py runserver

    
