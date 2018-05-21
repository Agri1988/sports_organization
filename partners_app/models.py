from datetime import datetime

from PIL import Image
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse

class IdentityDocument(models.Model):
    document_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Наименование документа')
    document_serial = models.CharField(max_length=32, blank=False, null=False, verbose_name='Серия документа')
    document_number = models.CharField(max_length=32, blank=False, null=False, verbose_name='Номер документа')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    date_of_validity = models.DateField(verbose_name='Действителен до')
    issuing_authority = models.CharField(max_length=256, blank=False, null=False, verbose_name='Орган выдавший документ')

    class Meta:
        verbose_name = 'Документ удостоверяющий личность'
        verbose_name_plural = 'Документы удостоверяющие личность'

    def __str__(self):
        return ('{} {} {}'.format(self.document_name, self.document_serial, self.document_number))


class AbstractPartner(models.Model):
    last_name = models.CharField(max_length=256, blank=False, null=False, verbose_name="Фамилия")
    first_name = models.CharField(max_length=256, blank=False, null=False, verbose_name="Имя")
    patronymic = models.CharField(max_length=256, blank=False, null=False, verbose_name="Отчество")
    birthday = models.DateField(verbose_name="Дата рождения")
    personal_number = models.CharField(max_length=14, blank=True, null=True, verbose_name="Личный номер")
    identity_document = models.OneToOneField('IdentityDocument', verbose_name="Документ удостоверяющий личность",
                                             on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField(upload_to='image/partners_app/%Y/%m/%d/', default=None, blank=True, null=True,
                              verbose_name='Фотография')


class Client (AbstractPartner):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronymic)

    def get_absolute_url(self):
        return reverse('partners_app:detail_client', args=[self.id])


class Employee(AbstractPartner):
    date_of_employment = models.DateField(verbose_name='Дата приема на работу')
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronymic)

    def get_absolute_url(self):
        return reverse('partners_app:detail_employee', args=[self.id])
