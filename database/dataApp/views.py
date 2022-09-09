from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
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
            room = form.save(commit=False)
            room.save()
            return redirect('students')
    context = {'form': form}

    return render(request, 'dataApp/register.html', context)

def ourList(request):
	li = []
	# form = StudentForm(request,['name'])
	students = Student.objects.order_by('name').values() # you can use all() instead of order_by('id') to retrieve random data
	#students = Student.objects.filter(name__startswith='J') and many more data retrieval
	# k = int(Student.objects.all().count())
	# for i in range(1,k+1):
	# 	li.append(i)
	# p = len(li)
	# if request.method == 'GET':
	# if form.is_valid():
	# 	name = form(search_box)
	# 	search = Student.objects.filter(name__contains='name')
	# 	context = {'search':search}
	# 	return render(request, 'dataApp/list.html', context)
	# else:
	students = Student.objects.order_by('name').values()
	filtered = Studifilter(request.GET, queryset=students)
	students = filtered.qs
	
	context = {'students':students, 'filter':filtered}

	return render(request, 'dataApp/list.html', context)

def updateStudi(request, pk):
	person = Student.objects.get(id=pk)
	form = StudentForm(instance=person)
	if request.method == 'POST':
		form = StudentForm(request.POST, request.FILES, instance=person)
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
