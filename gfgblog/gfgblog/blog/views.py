from django.shortcuts import render
from .models import posts
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse

# Create your views here.

# # create a function
# def geeks_view(request):
#     # create a dictionary to pass data to the template
#     context = {
#         "data" : "Gfg is the best",
#         "list" : [1,2,3,4,5,6,7,8,9,10]
#     }
#     # return response with template and context
#     return render(request, "geeks.html", context)

# class based views for posts
class postslist(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4

# class based view for each post
class postdetail(generic.DetailView):
    model = posts
    template_name = "post.html"