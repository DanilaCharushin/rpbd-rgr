from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers

from core.views import GenericFIOView, GenericFIOSView, GenericAddressesView, \
    GenericAddressView, GenericPhoneView, GenericPhonesView, GenericTypeView, GenericTypesView

router = routers.DefaultRouter()

urlpatterns = [
    path('fios', GenericFIOSView.as_view()),
    path('fio/<int:id>', GenericFIOView.as_view()),
    path('addresses', GenericAddressesView.as_view()),
    path('address/<int:id>', GenericAddressView.as_view()),
    path('types', GenericTypesView.as_view()),
    path('type/<int:id>', GenericTypeView.as_view()),
    path('phones', GenericPhonesView.as_view()),
    path('phone/<int:id>', GenericPhoneView.as_view()),
    # path('fios', FIOSAPIView.as_view()),
    # path('fio/<int:id>', FIOAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html'))
]
