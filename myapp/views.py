from django.shortcuts import render #type:ignore
from myapp.models import Post #type:ignore
from django.template import loader #type:ignore
from django.http import HttpResponse #type:ignore
from django.core.paginator import Paginator,EmptyPage #type:ignore
def pagehtml(request):
    id=loader.get_template('index.html')
    return HttpResponse(id.render())
def index(request):
    posts=Post.objects.all() 
    p=Paginator(posts,3)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except EmptyPage:
        page_obj=p.page(p.num_pages)
    context={'page_obj':page_obj}
    return render(request,'index.html',context)
def display(request):
    id=loader.get_template('index1.html')
    return HttpResponse(id.render())


                                                          


