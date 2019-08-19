from django.shortcuts import render

from django.views import generic

from .models import Post
from django.views.generic.base import TemplateView


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

class CreatePost(TemplateView):
	template_name = 'create_post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


