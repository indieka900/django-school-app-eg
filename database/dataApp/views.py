from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm,UpdateForm
from django.contrib.auth.models import User
from .filter import Studifilter


def home(request):
	return render(request,'dataApp/home.html')

def login(request):
	return render(request,'dataApp/login.html')

def register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # generate a unique password with 8 characters for the user
            password = User.objects.make_random_password(length=8)
            # set the password for the user (without hashing)
            user.password = password
            # save the user to the database
            user.save()
            return redirect('students')
    context = {'form': form}

    return render(request, 'dataApp/register.html', context)

def ourList(request):
	li = []
	# form = StudentForm(request,['name'])
	students = Student.objects.order_by('name').values()
	students = Student.objects.order_by('name').values()
	filtered = Studifilter(request.GET, queryset=students)
	students = filtered.qs
	
	context = {'students':students, 'filter':filtered}

	return render(request, 'dataApp/list.html', context)

def updateStudi(request, pk):
	person = Student.objects.get(id=pk)
	form = UpdateForm(instance=person)
	if request.method == 'POST':
		form = UpdateForm(request.POST, request.FILES, instance=person)
		if form.is_valid():
			form.save()
			return redirect('students')
	context = {'form':form}
	return render(request, 'dataApp/register.html', context)

def viewStudi(request, pk):
	person = Student.objects.get(id=pk)
	context = {'persons':person}
	return render(request, 'dataApp/profile.html', context)

def deleteStudi(request, pk):
	persons = Student.objects.get(id=pk)
	if request.method == 'POST':
		persons.delete()
		return redirect('students')
	context = {'persons':persons}
	return render(request, 'dataApp/delete.html', context)
# Create your views here.
