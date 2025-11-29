from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
