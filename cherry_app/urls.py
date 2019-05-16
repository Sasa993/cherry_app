from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from books.views import index
# from user_login.views import signup
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.admin import AdminSiteOTPRequired

admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
	path('2fa/', include(tf_urls)),
	path('twilio/', include(tf_twilio_urls)),
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	path('admin/', admin.site.urls),
	path('', index, name='index'),
	path('dashboard/', include('books.urls')),
	# path('accounts/', include('user_login.urls')),
	path('accounts/', include('allauth.urls')),
	path('invitations/', include('invitations.urls', namespace='invitations')),
	# path('invitations/accept-invite/accounts/signup/', signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
