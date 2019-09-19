from django.urls import path, include

from api import views


urlpatterns = [
    path('', views.UsersPosts.as_view(), name='get-posts'),
]
