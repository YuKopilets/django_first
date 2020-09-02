from django.db import models


class Entry(models.Model):
    entry_text = models.TextField('entry_text')
    entry_date = models.DateTimeField('entry_date')

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
