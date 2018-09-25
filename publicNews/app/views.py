from django.shortcuts import render
from .models import Newspublic
from .forms import PublicForm
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def news_public(request):
    all_public = Newspublic.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(all_public,20)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'news.html',{
        'news':news,
        })

def detail_public(request,id):
    news = Newspublic.objects.get(pk=id)
    return render(request, 'detial.html',{
        'news':news,
        })

def public_upload(request):
    if request.method == 'POST':
        print("pass")
        form = PublicForm(request.POST, request.FILES)
        if form.is_valid():
            print("yeah")
            form.save()
            return redirect('/')
    else:
        print("error")
        form = PublicForm()
    return render(request, 'upload.html', {
        'form': form,
    })

def pub_update(request,id):
    u = Newspublic.objects.get(pk=id)
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
        'form': form,
    })

def public_delete(request,id):
   u = Newspublic.objects.get(pk=id).delete()
   return HttpResponseRedirect("/")

