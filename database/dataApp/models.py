from django.db import models


'''FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', 
    )'''
CLASSES = [
	('Form One(1)','Form One(1)'),
	('Form Two(2)','Form Two(2)'),
	('Form Three(3)','Form Three(3)'),
	('Form Four(4)','Form Four(4)'),
]

GENDER_CHOICES = [
	('M','Male'),
	('F','Female')
]

class Student(models.Model):
	name = models.CharField(max_length=60)
	updated = models.DateTimeField(auto_now = True)
	joined = models.DateTimeField(auto_now_add=True, null=True)
	county = models.CharField(max_length=20, default='Vihiga')
	gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=10)
	kcpe_year = models.IntegerField(default='')
	kcpe_marks = models.IntegerField(default='')
	pic = models.ImageField(upload_to='images', default='')
	form = models.CharField(max_length=15,default='Form One(1)',choices=CLASSES)
	password = models.CharField(max_length=25,default='')
	#joined = models.DateField(aut)

	def __str__(self):
		return self.name

# Create your models here.
