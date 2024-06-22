from django.contrib import admin
from django.urls import include
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('demo/', include('demo.urls')),
    path('<version>/demo-version/', include('demo.urls')),
]
