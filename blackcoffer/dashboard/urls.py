from django.urls import include, path

from . import views

app_name = "dashboard"

urlpatterns = [
    # path("", views.home, name="index"),
    path("likelihood/", views.likelihood, name="likelihood"),
    path("intensity/", views.intensity, name="intensity"),
    path("relevance/", views.relevance, name="relevance"),
    path("", views.industry_summary_list, name="filter"),
]
