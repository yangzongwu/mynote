import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")
import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen=Faker()
#Fake pop script
def populate(N=5):
    for entry in range(N):
        fake_firstname=fakegen.first_name()
        fake_lastname=fakegen.last_name()
        fake_email=fakegen.email()
        user=User.objects.get_or_create(First_Name=fake_firstname,Last_Name=fake_lastname,Email=fake_email)[0]
if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
