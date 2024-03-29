from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_products),
    path('accounts/', include('allauth.urls')),
    path('localaccount/', include('accounts.urls', namespace='localaccounts')),
    path('product/', include('store.urls', namespace='store')),
    path('cart/', include('cart.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
