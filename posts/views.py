from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm # import PostForm from forms.

# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None) # if dont use "or None", "This field id required" appears beside each field.
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    # check if data is valid and then add it into database.
    # form = PostForm() # create a form inherited from PostForm
    # if request.method == "POST":
    #     print (request.POST)
    #     title = request.POST.gett("title")
    #     POST.objects.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    # context = {
    #     "title" : "Detail"
    # }
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List"
    }

    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
