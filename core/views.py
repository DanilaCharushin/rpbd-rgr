from loguru import logger
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User, Type, Address, Phone
from core.serializers import UserSerializer, AddressSerializer, TypeSerializer, PhoneSerializer


class GenericUsersView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericUserView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = []
    authentication_classes = []

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
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = []
    authentication_classes = []

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
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = 'id'
    permission_classes = []
    authentication_classes = []

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
    permission_classes = []
    authentication_classes = []

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
    permission_classes = []
    authentication_classes = []

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class GenericPhonesView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    permission_classes = []
    authentication_classes = []

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
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()
    lookup_field = 'id'
    permission_classes = []
    authentication_classes = []

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


def get_type_by_type_name(type_name):
    return Type.objects.get(name=type_name)


class AllAPIView(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request):
        data = []
        types = Type.objects.all()
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        users = User.objects.all()

        for user in users:
            address = next(filter(lambda a: a.user == user, addresses), None)
            user_phones = list(filter(lambda p: p.user == user, phones))
            result_phones = []
            for phone in user_phones:
                type_ = next(filter(lambda t: t.id == phone.type.id, types), "mobile")
                result_phones.append({
                    "id": phone.id,
                    "type": type_.name,
                    "number": phone.number
                })
            data.append({
                "id": user.id,
                "name": str(user),
                "phones": result_phones,
                "address": "" if not address else address.name
            })
        data.sort(key=lambda u: u["name"])
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        fio = data["name"].split()
        if len(fio) == 3:
            fio = {
                "last_name": fio[0],
                "first_name": fio[1],
                "father_name": fio[2]
            }
        elif len(fio) == 2:
            fio = {
                "last_name": fio[0],
                "first_name": fio[1],
                "father_name": ""
            }
        elif len(fio) == 1:
            fio = {
                "last_name": "",
                "first_name": fio[0],
                "father_name": ""
            }
        else:
            fio = {
                "last_name": "Иванов",
                "first_name": "Иван",
                "father_name": "Иванович"
            }

        user = User(**fio)
        user.save()

        Address(name=data["address"], user=user).save()

        for phone in data["phones"]:
            Phone(
                user=user,
                number=phone["number"],
                type=get_type_by_type_name(phone["type"])
            ).save()

        return Response(user.id, status=status.HTTP_201_CREATED)


class OneAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):
        user = User.objects.get(id=id)
        address = next(filter(lambda a: a.user == user, Address.objects.all()), None)
        phones = list(filter(lambda p: p.user == user, Phone.objects.all()))
        result_phones = []
        for phone in phones:
            type_ = next(filter(lambda t: t.id == phone.type.id, Type.objects.all()), "mobile")
            result_phones.append({
                "id": phone.id,
                "type": type_.name,
                "number": phone.number
            })
        data = ({
            "id": user.id,
            "name": str(user),
            "phones": result_phones,
            "address": "" if not address else address.name
        })

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = request.data
        logger.debug(data)
        fio = data["name"].split()
        if len(fio) == 3:
            fio = {
                "last_name": fio[0],
                "first_name": fio[1],
                "father_name": fio[2]
            }
        elif len(fio) == 2:
            fio = {
                "last_name": fio[0],
                "first_name": fio[1],
                "father_name": ""
            }
        elif len(fio) == 1:
            fio = {
                "last_name": "",
                "first_name": fio[0],
                "father_name": ""
            }
        else:
            fio = {
                "last_name": "Иванов",
                "first_name": "Иван",
                "father_name": "Иванович"
            }

        user = User.objects.get(id=id)
        for k, v in fio.items():
            setattr(user, k, v)
        user.save()

        address = Address.objects.get(user=user)
        address.name = data["address"]
        address.save()

        for phone_ in data["phones"]:
            phone_data = {
                "number": phone_["number"],
                "type": get_type_by_type_name(phone_["type"]),
                "user": user
            }
            logger.debug(phone_data)
            if "id" in phone_:
                phone = Phone.objects.get(id=phone_["id"])
                logger.debug(phone)
                for k, v in phone_data.items():
                    setattr(phone, k, v)
                phone.save()
                logger.debug(phone.to_json())
            else:
                Phone(**phone_data).save()

        return Response(id, status=status.HTTP_200_OK)

    def delete(self, request, id):
        user = User.objects.get(id=id)

        address = next(filter(lambda a: a.user == user, Address.objects.all()), None)
        if address:
            address.delete()

        phone_ids = map(lambda p: p.id, filter(lambda p: p.user == user, Phone.objects.all()))
        for phone_id in phone_ids:
            Phone.objects.get(id=phone_id).delete()

        user.delete()
        return Response(id, status=status.HTTP_200_OK)

