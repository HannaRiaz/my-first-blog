from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv', views.cv, name='cv'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='post_list'),
    # path('cropped', views.cropped, name='cropped'), 

]