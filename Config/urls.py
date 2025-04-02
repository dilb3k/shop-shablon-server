from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Usersapp.urls')),  
    path('products/', include('ProductApp.urls')), 
    path('category/', include('CategoryApp.urls')),
    path('blog/', include('Blog.urls')),
    path('cart/', include('Cart.urls')),
    path('order/', include('Order.urls')),
    path('null/', include('Admin.urls')),
    path('like/', include('Like.urls')),
    path('comment/', include('Review.urls')),
    path('sale/', include('Promotion.urls')),
    path('chat/', include('Massage.urls')),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
