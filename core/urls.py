from django.contrib import admin
from django.urls import path
from store.views import homepage, signup_view, login_view, logout_view, dashboard_view, products_view, product_detail_view, customizer_view, devlog_view, contact_view, policies_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('products/', products_view, name='products'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/<int:product_id>/customize/', customizer_view, name='customizer'),
    path('devlog/', devlog_view, name='devlog'),
    path('contact/', contact_view, name='contact'),
    path('policies/', policies_view, name='policies'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

