from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

# urlpatterns = [
#     path('', login_required(HomePageView.as_view()), name='home'),
# ]
