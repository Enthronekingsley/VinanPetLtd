from django.urls import path
from . import views
from .forms import ReportForm

urlpatterns = [
    path("", views.home, name="home"),
    path("report/", views.report, name="report"),

]