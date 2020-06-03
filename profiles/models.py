from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    about = models.CharField('О себе', max_length=1023, null=True, blank=True, default='')
    is_coach = models.BooleanField('Тренер', default=False)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Sections name', max_length=255,
                            help_text='Sections name max_length=255')
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coach")
    info = models.TextField('Info about group')
    price = models.IntegerField('Price per month')
    schedule = models.TextField()
    date_created = models.DateTimeField('Date created', default=timezone.now)

    class Meta:
        db_table = 'Section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['-date_created']


class Subscription (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Member')
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Team', related_name='members')
    date_started = models.DateTimeField('Date created', default=timezone.now)

