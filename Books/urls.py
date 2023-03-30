from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('creat/', views.BookCreatView.as_view(), name='book_create'),
    path('<int:pk>/edite', views.BookUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='delete_view'),

]
