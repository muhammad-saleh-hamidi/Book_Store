from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.singUpView.as_view(), name='signup')
]
