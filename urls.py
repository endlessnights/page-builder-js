from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sys/builder', views.page_builder, name='page_builder'),
    path('sys/save_components/', views.save_components, name='save_components'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
