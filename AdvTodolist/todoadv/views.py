from django.shortcuts import render,redirect
from django.views.generic import View
from .models import task
from .forms import TaskForm

class TaskList(View):
	def get(self,request):
		form =TaskForm()
		tasks = task.objects.all()
		return render(request,'todoadv/task_list.html',context={'form':form,'tasks':tasks})

	def post(self,request):
		form = TaskForm(request.POST)

		if form.is_valid():
			new_task = form.save()
			return redirect('task_list-url')
		else:
			return redirect('task_list-url')
# Create your views here.
