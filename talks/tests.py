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

    def test_create_talk_fail_unique_code(self):
        t1 = Talk()
        t1.title = "talk 2 title"
        t1.code = "talk2code"
        t1.created = datetime.now(pytz.utc)
        t1.updated = datetime.now(pytz.utc)
        t1.save()

        t2 = Talk()
        t2.title = "talk 2 title"
        t2.code = "talk2code"
        t2.created = datetime.now(pytz.utc)
        t2.updated = datetime.now(pytz.utc)

        with self.assertRaises(IntegrityError):
            t2.save()

    def test_create_talk_fail_without_title(self):
        talk = Talk()
        talk.code = "talk3code"
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        with self.assertRaises(IntegrityError):
            talk.save()

    def test_create_talk_fail_without_code(self):
        talk = Talk()
        talk.title = "talk 3 title"
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        with self.assertRaises(IntegrityError):
            talk.save()

    def test_create_talk_same_title_different_code(self):
        t1 = Talk()
        t1.title = "talk 4 title"
        t1.code = "talk4code"
        t1.created = datetime.now(pytz.utc)
        t1.updated = datetime.now(pytz.utc)
        t1.save()

        t2 = Talk()
        t2.title = "talk 4 title"
        t2.code = "talk5code"
        t2.created = datetime.now(pytz.utc)
        t2.updated = datetime.now(pytz.utc)
        t2.save()

        talks = Talk.objects.filter(slug="talk-4-title-talk5code")
        self.assertIs(talks.count(), 1)

