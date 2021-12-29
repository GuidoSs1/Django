from django.shortcuts import render,get_object_or_404
from django.views.generic import View

# Create your views here.
class blogListView(View):
    def get(self,request,*args,**kwargs):     
        context = {

        }
        return render(request,'blog_list.html', context)