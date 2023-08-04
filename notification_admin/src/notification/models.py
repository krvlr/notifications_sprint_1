import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TransportType(models.TextChoices):
    email = "email", _("email")
    websocket = "websocket", _("websocket")
    sms = "sms", _("sms")


class Group(models.TextChoices):
    subscribers = "subscribers", _("subscribers")
    everyone = "everyone", _("everyone")


class Timing(models.TextChoices):
    one = "one", _("one")
    week = "week", _("week")
    month = "month", _("month")


class Priority(models.TextChoices):
    high = "high", _("high")
    medium = "medium", _("medium")
    low = "low", _("low")


class Task(models.TextChoices):
    set_rating = "set_rating"
    user_registered = "user_registered"
    mass_sending = "mass_sending"


class Template(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    transport_type = models.CharField(
        _("transport_type"),
        choices=TransportType.choices,
        max_length=100,
    )
    task = models.CharField(
        _("task"),
        choices=Task.choices,
        max_length=100,
    )
    theme = models.TextField(_("theme"), blank=True, null=True)
    template_body = models.TextField(_("template_body"))

    class Meta:
        db_table = 'notification"."templates'
        verbose_name = _("template")
        verbose_name_plural = _("templates")

    def __str__(self):
        return self.name


class Schedule(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, verbose_name=_("template_schedule")
    )
    template_params = models.TextField(
        _("template_params"),
        blank=True,
        null=True,
    )
    group = models.CharField(
        _("group"),
        choices=Group.choices,
        max_length=100,
    )

    timing = models.CharField(
        _("timing"),
        choices=Timing.choices,
        max_length=100,
    )
    priority = models.CharField(
        _("priority"),
        choices=Priority.choices,
        max_length=100,
    )
    last_date = models.DateTimeField(_("last_date"), blank=True, null=True)
    planned_date = models.DateTimeField(_("planned_date"), blank=True, null=True)
    urgent = models.BooleanField(_("urgent"))

    class Meta:
        db_table = 'notification"."schedules'
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")

    def __str__(self):
        return self.name


class Configuration(UUIDMixin):
    class Meta:
        db_table = 'notification"."configs'
        verbose_name = _("config")
        verbose_name_plural = _("configs")

    name = models.SlugField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    value = models.CharField(_("value"), max_length=255)
