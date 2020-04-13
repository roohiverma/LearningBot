from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView

# for blog_list
def blog_list(request):
	post = Post.objects.all()
	context = {
	'blog_list':post

	}
	return render(request,"blog/blog_list.html",context)

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'blog/index.html', context=None)

class AboutPageView(TemplateView):
	template_name ="blog/about.html"			

