import pytz
from datetime import datetime

from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Talk


class TalkTests(TestCase):

    def test_create_talk(self):
        talk = Talk()
        talk.title = "talk 1 title"
        talk.code = "talk1code"
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        talk.save()

        talks = Talk.objects.filter(slug="talk-1-title")
        self.assertIs(talks.count(), 1)


    def test_create_talk_without_title(self):
        talk = Talk()
        talk.code = "talk2code"
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        with self.assertRaises(IntegrityError):
            talk.save()


    def test_create_talk_without_code(self):
        talk = Talk()
        talk.title = "talk 3 title"
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        with self.assertRaises(IntegrityError):
            talk.save()
