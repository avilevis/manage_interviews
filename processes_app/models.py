from django.db import models
from interviews_app.models import Interview


class Processes(models.Model):
    """CompanyContactAgents table object"""

    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Interview, related_name='processes', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(default=None, blank=True, null=True)
    duration = models.DurationField(default=None, blank=True, null=True)
    meeting_with = models.CharField(max_length=255)
    meeting_content = models.TextField()

    def __str__(self):
        return '%s at %s with %s' % (self.date, self.start_time, self.meeting_with)

    class Meta:
        db_table = 'Processes'
