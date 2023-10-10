from django.db.models import signals
from django.dispatch import receiver

from common_web_tools.web.models import Student, Profile


@receiver(signals.post_save, sender=Student)
def handle_student_creation(instance, created, *args, **kwargs):
    if not created:
        return

    Profile.objects.create(
        student_id=instance.pk
    )
