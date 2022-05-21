from .models import Notification
from django.contrib.auth.models import User


def admission_notification(sender):
    user_receiver = User.objects.get(is_superuser=True)

    Notification.objects.create(
        notif_type="admission",
        sender=sender,
        rec=user_receiver
    )
