from django.test import TestCase

# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        # Установки запускаются перед каждым тестом
        pass

    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(True)

    def test_something_that_will_fail(self):
        self.assertTrue(True)