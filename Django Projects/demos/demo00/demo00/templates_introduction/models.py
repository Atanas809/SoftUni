from django.db import models
from django.urls import reverse


# Create your models here.


class Company(models.Model):

    class Meta:
        verbose_name_plural = 'Companies'

    OPEN_POSITIONS = (
        ('DevOps', 'DevOps'),
        ('BackEnd', 'BackEnd'),
        ('FrontEnd', 'FrontEnd'),
        ('QA', 'QA'),
    )

    name = models.CharField(
        max_length=40,
    )

    description = models.TextField()

    employees = models.PositiveIntegerField()

    month_income = models.DecimalField(
        verbose_name='Monthly income',
        max_digits=8,
        decimal_places=5,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    modified_on = models.DateTimeField(
        auto_now=True,
    )

    hiring = models.BooleanField(
        null=True,
    )

    open_positions = models.CharField(
        max_length=15,
        choices=OPEN_POSITIONS,
        null=True,
    )

    company_email = models.EmailField(
        unique=True,
    )

    awards = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f'Company: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    deadline = models.DateField()

    def __str__(self):
        return f'Project name: {self.name}'


class CreditCard(models.Model):
    owner = models.OneToOneField(
        'Employee',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'Credit card owner: {self.owner.first_name}'


class Employee(models.Model):

    class Meta:
        ordering = ['last_name', 'first_name']

    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField(
        default=0,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
    )

    projects = models.ManyToManyField(Project)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Name {self.first_name} with ID: {self.pk}'


class Department(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(
        max_length=30,
    )

    slug = models.SlugField(
        unique=True,
        null=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def get_absolute_url(self):
        url = reverse('details page', kwargs={'pk': self.pk})

        return url
