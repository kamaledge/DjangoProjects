from django.db import models
from django.contrib.auth.models import User
from django.forms import fields


# Create your models here.



STATE_CHOICES = (
('Andra Pradesh','Andra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu and Kashmir','Jammu and Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madya Pradesh','Madya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Orissa','Orissa'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telagana','Telagana'),
('Tripura','Tripura'),
('Uttaranchal','Uttaranchal'),
('Uttar Pradesh','Uttar Pradesh'),
('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
('Chandigarh','Chandigarh'),
('Dadar and Nagar Haveli','Dadar and Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Delhi','Delhi'),
('Lakshadeep','Lakshadeep'),
('Pondicherry','Pondicherry'),
('West Bengal','West Bengal'),
)

class Resume(models.Model):
    name = models.CharField(max_length=70)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100, null=True)
    prfile_image = models.ImageField(upload_to='ProfileImg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)


