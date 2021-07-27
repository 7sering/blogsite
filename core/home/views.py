from django.shortcuts import render , redirect
from .form import BlogForm, BlogUpdate
from django.contrib.auth import logout
from .models import BlogModel

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

# Home View
def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)



# All Blogs view
def all_blogs(request):
    context = {}
    try:
        blog_objects = BlogModel.objects.filter(user = request.user)
        context['blog_objects'] = blog_objects
    except Exception as e:
        print(e)
    return render(request, 'all_blogs.html', context)



# Blog Detail View
def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html' , context)



# Register View
def register(request):
    return render(request, 'register.html')


# Login View 
def login(request):
    return render(request, 'login.html')




#Add Blogs View
def addblog(request):
    context = {'fm': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image'] 
            title = request.POST.get('title')
            user = request.user 
        if form.is_valid():
            content = form.cleaned_data['content']
        BlogModel.objects.create(user = user , title = title,content = content, image = image)
        return redirect('/')
    
    except Exception as e:
        print(e)
    
    return render(request, 'addblog.html', context)



#TODO blog updates
def blog_update(request, id):
    instance = BlogModel.objects.get(id = id)
    if request.method == 'POST':
        form = BlogUpdate(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BlogUpdate(instance=instance)
    return render(request,'update_blog.html', {'update_blog':form})
    



#Delete View
def delete_blog(request, id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/all-blogs/')



