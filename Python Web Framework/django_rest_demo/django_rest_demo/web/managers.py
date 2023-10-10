from django.db.models import Manager


class DepartmentManager(Manager):
    def get_or_create_by_name(self, name):
        try:
            return self.model.objects.filter(name=name).get()
        except self.model.DoesNotExist:
            return self.model.objects.create(
                name=name,
            )
