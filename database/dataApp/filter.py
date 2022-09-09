import django_filters
from django.forms.widgets import TextInput
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import * 

class Studifilter(django_filters.FilterSet):
	#start_date = DateFilter(field_name="joined",lookup_expr='gte')
	#end_date = DateFilter(field_name="joined",lookup_expr='lte')
	#name = django_filters.CharFilter(lookup_expr='iexact')
	#kcpe_marks = django_filters.NumberFilter()
	marks_gt = NumberFilter(field_name='kcpe_marks', lookup_expr='gt')
	marks__lt = NumberFilter(field_name='kcpe_marks', lookup_expr='lt')
	name = CharFilter(field_name="name", label='Name', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Student\'s name'}))
	country = CharFilter(field_name="county", label='County', lookup_expr='icontains')
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['pic','updated','password','joined','name','county','kcpe_marks','kcpe_year']