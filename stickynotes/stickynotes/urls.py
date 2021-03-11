
from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'noteget/', views.NoteList.as_view()),
    path( 'notecreate/', views.NoteCreate.as_view()),
]