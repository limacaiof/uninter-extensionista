from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='campaigns'),
    path('cadastrar', view=views.register, name='register'),
]
