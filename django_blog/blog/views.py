from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'blog/profile.html', {'form': form, 'success': True})
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


def home(request):
    return render(request, 'blog/home.html')


def posts(request):
    return render(request, 'blog/posts.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

