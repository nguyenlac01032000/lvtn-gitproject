from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.med_detail, name='med_detail'),
    path('search', views.search, name='search'),
]
