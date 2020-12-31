from django.db import models
from phone_field import PhoneField


class PlacementCompanyAgents(models.Model):
    """CompanyContactAgents table """

    id = models.AutoField(primary_key=True)
    placement_company_name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255, blank=True, unique=True)
    agent_phone = PhoneField(blank=True)

    def __str__(self):
        return '%s@%s' % (self.agent_name, self.placement_company_name)

    class Meta:
        db_table = 'PlacementCompanyAgents'
        ordering = ['id']
