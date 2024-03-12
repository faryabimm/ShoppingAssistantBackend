from django.urls import path

from director import views

urlpatterns = [
    path("<str:identity>", views.GoView.as_view()),
]