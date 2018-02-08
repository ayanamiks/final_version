import json

from django.contrib.postgres.fields import JSONField
from django.db import models


class TestJSON(models.Model):
    data = JSONField()

    def __str__(self):
        return json.dumps(self.data, ensure_ascii = False)

    class Meta:
        managed = True
        db_table = 'test_json2'
