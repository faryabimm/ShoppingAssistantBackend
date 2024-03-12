from django.urls import path

from director import views

urlpatterns = [
    path("go/<str:identity>", views.GoView.as_view()),
]