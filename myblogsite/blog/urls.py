# Django stores url of the links in urls.py file
# The urls.py match url and function in path inside urlpatterns array, once the specific path is requested, urls class
# match the function associated with the url. The function associated with each url is defined
# in views.py
from django.urls import pathfrom . import views
app_name = ‘blog’
urlpatterns = [
    path(‘’, views.all_blogs, name=‘all_blogs’),
    path(‘contact/’, views.contact, name=‘contact’),
    path(‘about/’, views.about, name=‘about’),
    path(‘<int:blog_id>/’, views.detail, name=‘detail’),]
