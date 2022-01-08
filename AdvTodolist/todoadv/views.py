from django.shortcuts import render,redirect
from django.views.generic import View
from .models import task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

class TaskList(View):
	def get(self,request):
		form =TaskForm()
		tasks = task.objects.all()
		return render(request,'todoadv/task_list.html',context={'form':form,'tasks':tasks})

	def post(self,request):
		form = TaskForm(request.POST)

		if form.is_valid():
			new_task = form.save()
			return JsonResponse({'tasks':model_to_dict(new_task)},status=200)
			# return redirect('task_list-url')
		else:
			return redirect('task_list-url')
class TaskComplete(View):
	def post(self,request,id):
		tasks = task.objects.get(id=id)
		tasks.completed = True
		tasks.save()
		return JsonResponse({'task':model_to_dict(tasks)}, status=200)

class Taskdelete(View):
	def post(self,request,id):
		tasks = task.objects.get(id=id)
		tasks.delete()
		return JsonResponse({'result':'ok'}, status=200)
# Create your views here.
