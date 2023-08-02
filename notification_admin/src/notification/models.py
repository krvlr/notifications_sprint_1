import uuid

from django.db import models


# TODO add translation!


class TimeStampedMixin(models.Model):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TransportType(models.TextChoices):
    email = 'email',
    websocket = 'websocket'
    sms = 'sms'


class Group(models.TextChoices):
    subscribers = 'subscribers', 'Отправить подписчикам'
    everyone = 'everyone', 'Отправить всем'


class Timing(models.TextChoices):
    one = 'one', 'Один раз'
    week = 'week', 'Раз в неделю'
    month = 'month', 'Раз в месяц'


class Priority(models.TextChoices):
    high = 'high', 'Высокий приоритет'
    medium = 'medium', 'Средний приоритет'
    low = 'low', 'Низкий приоритет'


class Task(models.TextChoices):
    review_rated = 'review-reporting.v1.rated'
    user_registered = 'user-reporting.v1.registered'
    admin = 'admin-reporting.v1.event'


class Template(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True, null=True)
    channel = models.CharField(
        choices=TransportType.choices,
        max_length=100,
    )
    task = models.CharField(
        choices=Task.choices,
        max_length=100,
    )
    theme = models.TextField(blank=True, null=True)
    template = models.TextField()

    class Meta:
        db_table = 'notification\".\"templates'

    def __str__(self):
        return self.name


class Schedule(UUIDMixin, TimeStampedMixin):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True, null=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    template_params = models.TextField(
        'template_params',
        blank=True,
        null=True,
    )
    group = models.CharField(
        choices=Group.choices,
        max_length=50,
    )
    is_instant = models.BooleanField()
    next_planned_date = models.DateTimeField(blank=True, null=True)
    timing = models.CharField(
        choices=Timing.choices,
        max_length=50,
    )
    priority = models.CharField(
        choices=Priority.choices,
        max_length=50,
    )
    last_processed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'notification\".\"schedules'

    def __str__(self):
        return self.name


class Configuration(UUIDMixin):
    class Meta:
        db_table = 'notification\".\"configs'

    name = models.SlugField('name', max_length=255)
    description = models.TextField('description', blank=True, null=True)
    value = models.CharField('value', max_length=255)
