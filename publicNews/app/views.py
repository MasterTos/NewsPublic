from django.shortcuts import render
from .models import NewsPublic
from .forms import PublicForm
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def news_public(request):
    all_public = NewsPublic.objects.all().order_by('-date')
    return render(request, 'news.html',{'all_public':all_public})

def detail_public(request,id):
    news = NewsPublic.objects.get(pk=id)
    return render(request, 'detial.html',{'news':news})

def public_upload(request):
    if request.method == 'POST':
        form = PublicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PublicForm()
    return render(request, 'upload.html', {
        'form': form
    })

def pub_update(request,id):
    u = NewsPublic.objects.get(pk=id)
    if not u:
        print("error")
    if request.method == 'POST':
        form = PublicForm(request.POST, request.FILES,instance=u)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PublicForm(instance=u)
    return render(request, 'update_form.html', {
        'form': form
    })

def public_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = NewsPublic.objects.get(pk=id).delete()
   return HttpResponseRedirect("/")
