from django import forms

from .models import Post


class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'slug',
			'author',
			'content',
			'status',
		]