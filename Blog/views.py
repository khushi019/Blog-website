from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required
def homeView(request):
    blog = Blog.objects.all()
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = BlogForm()

    paginator = Paginator(blog,3)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'form': form,
        'blog': page_obj,
    }
    return render(request, 'blogs/home.html', context)


def signupView(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignUpForm()    
    return render(request,'blogs/signup.html',{'form':form})


def logoutView(request):
    return render(request,'blogs/logout-user.html')

@login_required
def profileView(request):
    if request.method=='POST':
        editForm=EditForm(request.POST or None, instance=request.user)
        profileForm=ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if editForm.is_valid() and profileForm.is_valid():
            editForm.save()
            profileForm.save()
            return redirect('profile')
    else:
        editForm=EditForm(instance=request.user)
        profileForm=ProfileForm(instance=request.user.profile)
    context={
        'editForm':editForm,
        'profileForm':profileForm,
    }    
    return render (request,'blogs/profile.html',context)

@login_required
def detailView(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=='POST':
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            instance=commentForm.save(commit=False)
            instance.name=request.user
            instance.blog=blog
            instance.save()
            return redirect('detail',id)
    else:
        commentForm=CommentForm()    
    context={
        'blog':blog,
        'commentForm':commentForm,
    }
    return render(request,'blogs/detail.html',context)

@login_required
def delete_view(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=='POST':
        blog.delete()
        return redirect('home')
    return render(request,'blogs/delete.html',{'blog':blog})

@login_required
def update_view(request,id):
    context={}
    blog=Blog.objects.get(id=id)
    form=BlogForm(request.POST or None,instance=blog)
    if form.is_valid():
        form.save()
        return redirect('detail',id)
    context['form']=form
    return render(request,'blogs/update.html',context)


@login_required
def share_view(request, id):
    blog =Blog.objects.get(id=id)
    sent = False

    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            blog_url = request.build_absolute_uri(f'/detail/{blog.id}/')
            subject = f"{request.user.get_full_name()} recommends you read {blog.title}"
            message = f"Read {blog.title} at {blog_url}\n\n" \
                      f"Personal message: {cd['body']}\n\n" \
                      f"The blogs content is:\n{blog.content}\n\n" \
                      f"Sent by {request.user.get_full_name()} ({request.user.email})"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = ShareForm()

    context = {
        'blog': blog,
        'form': form,
        'sent': sent,
    }

    return render(request, 'blogs/share.html', context)


