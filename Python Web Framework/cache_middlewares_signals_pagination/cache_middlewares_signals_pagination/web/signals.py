from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from cache_middlewares_signals_pagination.web.models import Employee

UserModel = get_user_model()


@receiver(signals.post_save, sender=Employee)
def handle_employee_creation(*args, **kwargs):
    print(args)
    print(kwargs)


# The result from kwargs when creates new employee
"""
{
'signal': <django.db.models.signals.ModelSignal object at 0x000002A5D97F03A0>, 
'sender': <class 'cache_middlewares_signals_pagination.web.models.Employee'>,
'instance': <Employee: Employee object (4)>,
'created': True,
'update_fields': None,
'raw': False,
'using': 'default',
}
"""


@receiver(signals.post_save, sender=UserModel)
def create_employee_using_user_model(instance, created, *args, **kwargs):
    if not created:
        return

    Employee.objects.create(
        user_id=instance.pk,
    )
