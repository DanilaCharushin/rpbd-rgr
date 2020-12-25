from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Phonebook API",
      default_version='v1',
      description="RPBD RGR, Detchik, Zemlyakov, AVT-715",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from core.views import (
    AllAPIView, OneAPIView,
    GenericUsersView, GenericUserView,
    GenericAddressesView, GenericAddressView,
    GenericTypesView, GenericTypeView,
    GenericPhonesView, GenericPhoneView
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
