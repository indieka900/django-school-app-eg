
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['password']
        
        
class UpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'