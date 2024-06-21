from django.urls import path
from demo import views


urlpatterns = [
    # path('hello/', views.hello),
    # path('demo-version/', views.demo_version),
    path('custom-version/', views.DemoView.as_view()),
    path('another-custom-version/', views.AnotherView.as_view())
]