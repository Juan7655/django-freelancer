from django.urls import path

from .views import LoginPageView, logout_view

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_view, name='login'),
]
