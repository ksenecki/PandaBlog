from django import forms

from .models import Post

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

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
		widgets = {
			'content': SummernoteWidget(),
		}
