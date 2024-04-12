from django.db import models
from django.contrib.postgres.fields import ArrayField


class FoundOrgs(models.Model):
    orgs_names = ArrayField(models.CharField(max_length=255))
    orgs_ids = ArrayField(models.IntegerField(max_length=50))
    found_at = models.DateTimeField


class OrgsToMerge(models.Model):
    orgs_ids = ArrayField(models.IntegerField(max_length=50))

class MainOrg(models.Model):
    org_id = models.IntegerField(max_length=50)

