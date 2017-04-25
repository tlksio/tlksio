#!/usr/bin/env python

import os
import sys
import django

sys.path.append("/home/raul/tlksio")
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

from talks.models import Talk
talk = Talk.objects.order_by('?').first()

print(talk)
