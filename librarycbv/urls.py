
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('books/', include('books.urls')),
  path('authors/', include('authors.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
