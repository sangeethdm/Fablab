from django.urls import path
from . import views

urlpatterns = [path(r"R.html",views.reserve, name='R'),path(r"", views.index, name='INDEX')]


