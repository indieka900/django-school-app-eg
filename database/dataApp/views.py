from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


def home(request):
	return render(request,'dataApp/home.html')

def login(request):
	return render(request,'dataApp/login.html')

def register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'dataApp/register.html', context)

def ourList(request):
	li = []
	students = Student.objects.order_by('id') # you can use all() instead of order_by('id') to retrieve random data
	#students = Student.objects.filter(name__startswith='J') and many more data retrieval
	# k = int(Student.objects.all().count())
	# for i in range(1,k+1):
	# 	li.append(i)
	# p = len(li)
	context = {'students':students,}

	return render(request, 'dataApp/list.html', context)
# Create your views here.
