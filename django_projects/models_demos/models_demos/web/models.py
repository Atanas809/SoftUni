from django.db import models
from django.urls import reverse

from models_demos.core.review_validator import validate_review_length


# Create your models here.

class AuditMixin(models.Model):
    class Meta:
        abstract = True

    # This will be automatically set when created
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )


class Department(AuditMixin, models.Model):
    name = models.CharField(
        max_length=30,
    )
    owner = models.CharField(
        max_length=40,
    )

    slug = models.SlugField(
        unique=True
    )

    def __str__(self):
        return f"Department ID: {self.pk}"

    def get_absolute_url(self):
        url = reverse('department details', kwargs={'pk': self.pk, 'slug': self.slug})

        return url


class Projects(AuditMixin, models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    name = models.CharField(
        max_length=30,
    )
    deadline = models.DateField()

    def __str__(self):
        return f'Project ID: {self.pk}'


class CreditCard(models.Model):
    employee_id = models.IntegerField(
        primary_key=True,
    )


class Employees(models.Model):
    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name_plural = 'Employees'

    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    # VARCHAR(40) => string with max length 40
    first_name = models.CharField(
        max_length=40,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        verbose_name='Seniority level:',
        max_length=20,
        choices=LEVELS,
    )

    age = models.PositiveIntegerField(
        default=0,
    )

    # int >= 0
    experience_years = models.PositiveIntegerField()

    # Text => text with unlimited length
    review = models.TextField(
        validators=(validate_review_length,)
    )

    # This will be automatically set when created
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    start_date = models.DateField(
        null=True,
    )

    email = models.EmailField(
        unique=True,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # One to Many:
    department_id = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        verbose_name='Department',
    )

    # Many to Many:
    project_id = models.ManyToManyField(Projects)

    card = models.ForeignKey(
        CreditCard,
        on_delete=models.CASCADE,
        null=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk} Name: {self.full_name}'


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=30,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
