from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('accounts/login/', views.login_view, name='login'),  # Login page
    path('accounts/logout/', views.logout_view, name='logout'),  # Logout page
]