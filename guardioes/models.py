# coding: utf-8

import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField
import uuid


class GuardianDevice(models.Model):
    from nodeshot.core.nodes.models import Node
    identifier = models.CharField(_('Device'), max_length=100, unique=True)
    node = models.ForeignKey(Node, verbose_name=_('Node'))

    def __repr__(self):
        return "<GuardianDevice('{}')>".format(self.identifier)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.identifier = '{guardian_name}/{random_str}'.format(
                                  guardian_name=slugify(self.node.name),
                                  random_str=str(uuid.uuid4()).split('-')[-1])
        super(GuardianDevice, self).save(*args, **kwargs)


class GuardianData(models.Model):
    device = models.ForeignKey(GuardianDevice, verbose_name=_('Device'))
    collected_date = models.DateTimeField(_('Collected Date'))
    received_date = models.DateTimeField(_('Received Date'),
                                         default=datetime.datetime.now())
    data = JSONField(_('Data'))
