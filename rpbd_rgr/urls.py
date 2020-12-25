from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

from core.views import (
    AllAPIView, OneAPIView,
    GenericUsersView, GenericUserView,
    GenericAddressesView, GenericAddressView,
    GenericTypesView, GenericTypeView,
    GenericPhonesView, GenericPhoneView
)

router = routers.DefaultRouter()

urlpatterns = [
    path('users', csrf_exempt(GenericUsersView.as_view())),
    path('user/<int:id>', csrf_exempt(GenericUserView.as_view())),
    path('addresses', csrf_exempt(GenericAddressesView.as_view())),
    path('address/<int:id>', csrf_exempt(GenericAddressView.as_view())),
    path('types', csrf_exempt(GenericTypesView.as_view())),
    path('type/<int:id>', csrf_exempt(GenericTypeView.as_view())),
    path('phones', csrf_exempt(GenericPhonesView.as_view())),
    path('phone/<int:id>', csrf_exempt(GenericPhoneView.as_view())),
    path('all', csrf_exempt(AllAPIView.as_view())),
    path('one/<int:id>', csrf_exempt(OneAPIView.as_view())),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html'))
]
