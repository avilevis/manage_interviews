from django.db import models
from phone_field import PhoneField
from core.choices_array_field import ChoiceArrayField
from agents_app.models import PlacementCompanyAgents


class Interview(models.Model):
    """interviewTable object"""
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=255)
    COMPANY_TYPE_CHOICES = [
        ('SU', 'Start Up'),
        ('MD', 'Medium'),
        ('BG', 'Big'),
    ]
    company_type = models.CharField(
        max_length=2,
        choices=COMPANY_TYPE_CHOICES,
    )
    company_contact_person = models.CharField(max_length=255, blank=True)
    company_contact_phone = models.CharField(blank=True, max_length=12)
    company_info = models.TextField(blank=True)
    logo_url = models.URLField(max_length=200, blank=True, null=True)

    placement_company = models.ForeignKey(PlacementCompanyAgents, on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ('DN', 'Did Not Start'),
        ('ST', 'Started'),
        ('RJ', 'Rejected'),
        ('PS', 'Passed')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0]
    )

    TECHNOLOGY_CHOICES = [
        ('NJ', 'Node.js'),
        ('PY', 'Python'),
        ('DJ', 'Django'),
        ('RB', 'Ruby'),
        ('TS', 'TypeScript'),
        ('RT', 'React'),
        ('AG', 'Angular'),
        ('VU', 'Vue.js'),
        ('SC', 'Scala'),
        ('AS', 'ASP'),
        ('GO', 'Go'),
        ('JQ', 'JQuery'),
        ('JS', 'JavaScript'),
    ]
    technology = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=TECHNOLOGY_CHOICES,
        ),
    )

    position = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'Interview'
