from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
#there're two type of views function base & class base views
from .models import Post

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request, id): #retrieve
    #instance = Post.objects.get(id=5)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)
    #return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list item
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)
    # if request.user.is_authenticated():
    #     context ={
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    #return render(request, "index.html", context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
