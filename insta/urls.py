"""insta app url Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from insta.views import IndexView, SignUp, MakePost, UserProfile, toggleFollow

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('post', MakePost.as_view(), name='makepost'),

    path('auth/signup', SignUp.as_view(), name='signup'),

    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),

    path('togglefollow', toggleFollow, name='togglefollow'),
]
