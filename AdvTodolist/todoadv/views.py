from django.shortcuts import render
from django.views.generic import View

class TaskList(View):
	def get(self,request):
		return render(request,'todoadv/task_list.html')
# Create your views here.
