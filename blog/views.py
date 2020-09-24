from django.shortcuts import render

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

posts = [
        {'author': 'rdzudzar',
         'title': 'Blog post 1',
         'content': 'First blog post content',
         'date_posted': 'September 24th 2020'
            },
        {'author': 'Unknown',
         'title': 'Blog post 2',
         'content': 'Second blog post content',
         'date_posted': 'September 24th 2020'
            }
    ]

#This is to connect the template
def home(request):
    
    context = {
        'posts':posts
        }
    return render (request, 'blog/home.html', context)


def about(request):

    return render (request, 'blog/about.html', {'title':'About'})
