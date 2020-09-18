from django.urls import path

from userapp import views

urlpatterns = [
    path("demo/", views.Demo.as_view()),
    path("users/", views.UserAPIView.as_view()),
]