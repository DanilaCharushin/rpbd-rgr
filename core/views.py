from django.http import HttpResponse
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import FIO, Addresses, Type, Phones
from core.serializers import FIOSerializer, AddressesSerializer, TypeSerializer, PhonesSerializer


class GenericFIOSView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = FIOSerializer
    queryset = FIO.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericFIOView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = FIOSerializer
    queryset = FIO.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class GenericAddressesView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = AddressesSerializer
    queryset = Addresses.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericAddressView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = AddressesSerializer
    queryset = Addresses.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class GenericTypesView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericTypeView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class GenericPhonesView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = PhonesSerializer
    queryset = Phones.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericPhoneView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = PhonesSerializer
    queryset = Phones.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class FIOSAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = FIO.objects.all()
        serializer = FIOSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FIOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FIOAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id_):
        fio = self.__get_fio(id_)
        serializer = FIOSerializer(fio)
        return Response(serializer.data)

    def put(self, request, id_):
        fio = self.__get_fio(id_)
        serializer = FIOSerializer(fio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_):
        fio = self.__get_fio(id_)
        fio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def __get_fio(self, id_):
        try:
            return FIO.objects.get(id=id_)
        except FIO.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
