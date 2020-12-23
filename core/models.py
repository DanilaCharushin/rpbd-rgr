from django.db import models


class Type(models.Model):
    type_name = models.TextField('Тип телефона', max_length=16, null=False)

    def __str__(self):
        return "{}".format(self.type_name)


class FIO(models.Model):
    first_name = models.TextField('Имя', max_length=16, null=False)
    last_name = models.TextField('Фамилия', max_length=16, null=False)
    father_name = models.TextField('Отчество', max_length=16, null=False)

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.father_name)

    class Meta:
        verbose_name = 'ФИО'
        verbose_name_plural = 'ФИО'


class Addresses(models.Model):
    address = models.TextField('Адрес', max_length=64, null=False)
    fio_id = models.ForeignKey(FIO, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{}, {}".format(self.address, self.fio_id)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Phones(models.Model):
    phone = models.TextField('Номер телефона', max_length=32, null=False)
    fio_id = models.ForeignKey(FIO, on_delete=models.CASCADE, null=False)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{}, {}, ({})".format(self.phone, self.fio_id, self.type_id)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
