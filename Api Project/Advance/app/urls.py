from django.urls import include, path

from app import views
from app.views import Flipkart_ApiViewset
from rest_framework import routers

# Router provide an easy way automatically determinig the the URL configuration.
router = routers.DefaultRouter()
router.register(r'Flipkart_Api', Flipkart_ApiViewset)

urlpatterns = [
    # path('',views.LoginApi),
    path('',include(router.urls)),
    path('login/',views.LoginApi.as_view()),
    
]