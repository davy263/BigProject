from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django import forms
from .form import CreateUserForm
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'houses/Home.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name =  'houses/Home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 4


class PostListView2(ListView):
    model = Post
    template_name =  'houses/Houses.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 8


class PostListView3(ListView):
    model = Post
    template_name =  'houses/profile.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['location', 'price', 'details', 'Rent_or_Buy', 'Descriptions', 'image', 'image1', 'image2']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['location', 'price', 'details', 'Rent_or_Buy', 'Descriptions', 'image', 'image1', 'image2']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.agent:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.agent:
            return True
        return False


def houses(request):
    return render(request, 'houses/Houses.html', {'tittle': 'Explore Houses For Buy and Rent'})


def apartments(request):
    return render(request, 'houses/Apartments.html', )



def register(request):
    if request.user.is_authenticated:
        return redirect('Estate-home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created ' + user)
                return redirect('Estate-log in')

        context = {

            'form': form

        }
        return render(request, 'houses/Register.html', context)


def log_in(request):
    if request.user.is_authenticated:
        return redirect('Estate-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Estate-home')
            else:
                messages.info(request, 'Username or Password is Incorrect')

    context = {

    }

    return render(request, 'houses/Log in.html', context)


def log_out(request):
    logout(request)
    return redirect('Estate-home')





def home2(request):
    return render(request, 'houses/post_form.html', )



