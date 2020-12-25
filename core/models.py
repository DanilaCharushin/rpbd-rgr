from django.db import models


class Type(models.Model):
    name = models.TextField(verbose_name='Тип телефона', max_length=16, null=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class User(models.Model):
    first_name = models.TextField(verbose_name='Имя', max_length=16, null=False)
    last_name = models.TextField(verbose_name='Фамилия', max_length=16, null=False)
    father_name = models.TextField(verbose_name='Отчество', max_length=16, null=False)

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.father_name)

    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "father_name": self.father_name,
        }

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Address(models.Model):
    name = models.TextField(verbose_name='Адрес', max_length=64, null=False)
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='address', on_delete=models.CASCADE,
                             null=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.user)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "user": self.user.to_json()
        }

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Phone(models.Model):
    number = models.TextField('Номер телефона', max_length=32, null=False)
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='phones', on_delete=models.CASCADE,
                             null=False)
    type = models.ForeignKey(Type, verbose_name='Тип', related_name='phones', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{}, {}, ({})".format(self.number, self.user, self.type)

    def to_json(self):
        return {
            "id": self.id,
            "number": self.number,
            "user": self.user.to_json(),
            "type": self.type,
        }

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
