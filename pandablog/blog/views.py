from django.shortcuts import render

from .forms import PostModelForm
from django.views import generic
# CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Post
from django.views.generic.base import TemplateView



def about_view(request):
    context = {
    }

    return render(request, "about.html", context)


# def post_list_view(request, *args, **kwargs):
# 	queryset = Post.objects.filter(status=1).order_by('-created_on')
# 	context = {
# 		'post_list': queryset
# 	}
# 	template_name = 'index.html'
# 	return render(request, template_name, context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# class CreatePost(generic.CreateView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     form_class = PostModelForm
#     template_name = 'create_post.html'


def create_post_view(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
    	form.save()
    	form = PostModelForm()
    context = {
    	'form' : form
    }
    if request.user.is_superuser:
    	return render(request, "create_post.html", context)
    else:
    	return render(request, "permission.html", {})

# class CreatePost(TemplateView):
# 	template_name = 'create_post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


