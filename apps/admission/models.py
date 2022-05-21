from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Admission(models.Model):
    date = models.DateTimeField(default=timezone.now)
    child_name = models.CharField(max_length=100, blank=False)
    class_join = models.IntegerField(default=1)
    international_id = models.CharField(max_length=20, blank=False)
    birth_date = models.DateField(default=timezone.now, blank=False)
    october_age = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=100, blank=False)

    is_joined_before = models.CharField(max_length=5, blank=False, default="NO")
    is_joined_name = models.CharField(max_length=100, blank=True, null=True)
    is_joined_duration = models.IntegerField(blank=True, null=True)

    siblings_count = models.CharField(max_length=5, blank=False, default="NO")
    siblings_count_name = models.CharField(max_length=100, blank=True, null=True)
    siblings_count_class = models.IntegerField(blank=True, default=1, null=True)

    phone_number = models.CharField(max_length=12, blank=False)
    email = models.EmailField()

    mother_name = models.CharField(max_length=100, blank=False)
    mother_phone_number = models.CharField(max_length=12)
    mother_job = models.IntegerField(blank=False, default=1)
    what_mother_job = models.CharField(max_length=100, blank=True, null=True)
    mother_qualification = models.CharField(max_length=10, blank=False, default='DB')
    mother_qualification_other = models.CharField(max_length=50, blank=True, null=True)

    father_name = models.CharField(max_length=100, blank=False)
    father_job = models.CharField(max_length=50, blank=False)

    father_qualification = models.CharField(max_length=10, blank=False, default='DB')
    father_qualification_other = models.CharField(max_length=50, blank=True, null=True)
    father_phone_number = models.CharField(max_length=12, blank=False, null=False)

    def __str__(self):
        return str(self.child_name)

    def get_absolute_url(self):
        return f"admission/{self.id}/"


@receiver(pre_save, sender=Admission)
def check_options(sender, instance, **kwargs):

    if instance.is_joined_before != "YES":
        instance.is_joined_name = None
        instance.is_joined_duration = None

    if instance.siblings_count != "YES":
        instance.siblings_count_name = None
        instance.siblings_count_class = None

    if instance.mother_job != 2:
        instance.what_mother_job = None

    if instance.mother_qualification_other and instance.mother_qualification != "OTHER":
        instance.mother_qualification_other = None

    if instance.father_qualification != "OTHER":
        instance.father_qualification_other = None


class Notification(models.Model):
    notif_type = models.CharField(max_length=100, verbose_name="Notification Type") # task, admission, ...etc
    sender = models.EmailField(blank=True, null=True) # anonymous user, real user
    rec = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="receiver") # admin, supervisor, ...etc
    read_notif = models.BooleanField(verbose_name="Notification Read", default=False) # False -> doesn't read
    notif_name = models.CharField(max_length=50, null=True, blank=True) # name of channels

    def __str__(self):
        return self.rec

    @property
    def get_notification_count(self):
        return self.objects.filter(rec=self.rec).filter(read_notif=False).count()
