import string
from django.test import TestCase
from .models import UrlMapping
from .utils.path_generator import ShortPath

class UrlMappingTests(TestCase):
    def test_path_length(self):
        short_path = ShortPath().gen_path()
        self.assertIs(len(short_path), ShortPath.path_length)

    def test_path_valid_chars(self):
        short_path = ShortPath().gen_path()
        for c in short_path:
            self.assertIn(c, string.ascii_letters)

    def test_short_link_maps_back_to_original_url(self):

        test_url = 'https://www.example.com'

        # delete if record already exists
        try:
            m = UrlMapping.objects.get(original_url=test_url)
            m.delete()
        except:
            pass

        try:
            short_path = ShortPath().gen_path()
            m = UrlMapping(original_url=test_url, short_path=short_path)
            m.save()

            from_db = UrlMapping.objects.get(short_path=short_path)
            self.assertEqual(from_db.original_url, test_url)
        except:
            self.fail('Database read/write failure')
