from . import views
from django.conf.urls import url


urlpatterns = [
	url(r'^posts/$', views.blog_list),
	url(r'^$',views.HomePageView.as_view()),
	# url(r'^about/$',views.AboutPageView.as_view()),
]