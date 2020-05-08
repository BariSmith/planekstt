from django_registration.forms import RegistrationFormUniqueEmail

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from . import views, admin
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]

