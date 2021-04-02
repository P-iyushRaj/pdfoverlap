
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdffile/', views.Pdf_api.as_view()),

    path( 'noteget/', views.NoteList.as_view()),
    path( 'notecreate/', views.NoteCreate.as_view()),



    path('fax/', views.Fax_api.as_view()),
    path('voip/', views.Voip_api.as_view()),

    path('sign/', views.Sign_api.as_view()),

    path('signnow/', views.SignNow_api.as_view()),

    path('SignNowhtml/', views.SignNowhtmlform_api.as_view()),

    path('app/', include('app.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)