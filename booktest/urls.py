from django.urls import path
from . import views

urlpatterns = [
    path("data1/",views.TestModelView1.as_view()),
]