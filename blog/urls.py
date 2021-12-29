from django.urls import path

from .views import blogListView

app_name=['blog']

urlpatterns = [
    path('inicio/', blogListView.as_view(), name='home'),
]