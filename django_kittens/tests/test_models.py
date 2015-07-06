from django_dynamic_fixture import G
from django.test import TestCase
from mock import patch, MagicMock

from ..models import Kitten, reddit_kitten


class GetRandomTest(TestCase):
    @patch('packaging_july2015.apps.kittens.models.random.random')
    @patch('packaging_july2015.apps.kittens.models.KittenManager._rand_inst')
    def test_calls_rand_inst(self, rand_inst_mock, random_mock):
        G(Kitten)
        random_mock.return_value = .00001
        Kitten.objects.get_random()
        self.assertTrue(rand_inst_mock.called)
        
    @patch('packaging_july2015.apps.kittens.models.random.random')
    @patch('packaging_july2015.apps.kittens.models.KittenManager.create_new')
    def test_calls_create_new(self, create_new_mock, random_mock):
        G(Kitten)
        random_mock.return_value = .9
        Kitten.objects.get_random()
        self.assertTrue(create_new_mock.called)


class RandInstTest(TestCase):
    def test_returns_inst(self):
        k = G(Kitten)
        res = Kitten.objects._rand_inst()
        self.assertEqual(res, k)


class CreateNewTest(TestCase):
    def setUp(self):
        self.kit = MagicMock()
        self.kit.url = 'abc.com'
        self.kit.thumbnail = 'cute.jpg'
        self.kit.title = 'My cute cat'

    @patch('packaging_july2015.apps.kittens.models.reddit_kitten')
    def test_saves_instance(self, reddit_kitten_mock):
        reddit_kitten_mock.return_value = self.kit
        Kitten.objects.create_new()
        kitten_count = Kitten.objects.count()
        expected = 1
        self.assertEqual(kitten_count, expected)

    @patch('packaging_july2015.apps.kittens.models.reddit_kitten')
    def test_returns_instance(self, reddit_kitten_mock):
        reddit_kitten_mock.return_value = self.kit
        kit = Kitten.objects.create_new()
        self.assertTrue(kit)
