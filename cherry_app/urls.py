from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from books.views import index

urlpatterns = [
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	path('admin/', admin.site.urls),
	path('', index, name='index'),
	path('dashboard', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
