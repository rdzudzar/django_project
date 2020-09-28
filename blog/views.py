from django.shortcuts import render, get_object_or_404
from .models import Post

from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin)
                                        
#This is when we create manual html page
# =============================================================================
#from django.http import HttpResponse
# def home(request):
#     '''
#     Function to create home page
#     
#     Parameters
#     ----------
#     request : 
# 
#     Returns
#     -------
#     HttpResponse with a page cotntent: Blog Home
# 
#     '''
#     return HttpResponse('<h1> Blog Home </h1>')
# =============================================================================

# =============================================================================
# Once we set up Post from DB, we no longer need dummy data 
# posts = [
#         {'author': 'rdzudzar',
#          'title': 'Blog post 1',
#          'content': 'First blog post content',
#          'date_posted': 'September 24th 2020'
#             },
#         {'author': 'Unknown',
#          'title': 'Blog post 2',
#          'content': 'Second blog post content',
#          'date_posted': 'September 24th 2020'
#             }
#     ]
# =============================================================================

#This is to connect the template
def home(request):
    
    context = {
        'posts':Post.objects.all()
        }
    return render (request, 'blog/home.html', context)

#Rewrite above home into Class based views
class PostListView(ListView):
    #create model which to query to create post
    model = Post
    #we need to change the template where its looking for
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    #order posts from newest to oldest
    ordering = ['-date_posted']
    #Paginator
    paginate_by = 5
    
class UserPostListView(ListView):
    #create model which to query to create post
    model = Post
    #we need to change the template where its looking for
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    #Paginator
    paginate_by = 5
    
    #it will get username if it exist, else it will give us 404
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    #so it automatically see current user as the post writer
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    #so it automatically see current user as the post writer
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #check if user is the author and then allow them to update the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    #check if user is the author and then allow them to delete the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):

    return render (request, 'blog/about.html', {'title':'About'})
