from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from wossname.models import Wossname

class WossnameTest(TestCase):

    def test_wossname_has_name(self):
        thing = Wossname.objects.create(name="Woss")
        self.assertEqual(thing.name, "Woss")
        self.assertEqual(str(thing), "Woss")
        self.assertEqual(unicode(thing), "Woss")
