"""fantasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from stats import views as s_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', s_views.home_view, name='home_view'),
    path('passing/', s_views.passing_view, name='passing_view'),
    path('rushing/', s_views.rushing_view, name='rushing_view'),
    path('defense/', s_views.defense_view, name='defense_view'),
    path('quiz/', s_views.quiz_view, name='quiz_view'),
]
