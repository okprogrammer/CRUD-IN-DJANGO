from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
from .models import PostModel
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Crud
#create
#retrieve
#update
#Delete
#List

def Home(request):
    return HttpResponse('<h1>Hey, I am coming from Home!</h1>') 

def post_model_create_view(request):

    ''' if request.method =='POST':
        print(request.POST) '''
    form = PostModelForm(request.POST or None)
    context={
        'form':form,
       
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        messages.success(request, 'Post has been created!')
        #return HttpResponseRedirect('/blog/{num}'.form(num=obj.id)) 
        context = {
            'form':PostModelForm()
        }
    template = 'create-view.html'
    return render(request,template,context)

def post_model_update_view(request,id=None):
    obj =get_object_or_404(PostModel,id=id)

    ''' if request.method =='POST':
        print(request.POST) '''
    form = PostModelForm(request.POST or None,instance=obj)
    context={
        'form':form,
        'object':obj
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        messages.success(request, 'Updated has been done!')
        return HttpResponseRedirect('/blog/{num}'.format(num=obj.id)) 
    template_path = 'update-view.html'
    return render(request,template_path,context)
    

def post_model_detail_view(request,id=None):
    obj =get_object_or_404( PostModel,id=id)
    context = {
        'object':obj,
    }
    template_path='detail-view.html'
    return render(request,template_path,context)

def post_model_delete_view(request,id=None):
    obj =get_object_or_404( PostModel,id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request,'Post deleted')
        return HttpResponseRedirect('/blog/')
    
    context = {
        'object':obj,
    }
    template_path='delete-view.html'
    return render(request,template_path,context)



#@login_required
def post_model_list_view(request):
    print(request.user)
    if request.user.is_authenticated():
        template_path='list-view.html'
    else:
        template_path='list-view-public.html'
        #raise Http404
    qs=PostModel.objects.all()
    print(qs)
    #return HttpResponse("some data"):
    
    context_dictionary={'object_list':qs}
    return render(request,template_path,context_dictionary)