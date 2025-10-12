from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # You can add a profile view here later, e.g.:
    # path('profile/', ProfileView.as_view(), name='profile'),
]


