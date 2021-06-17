from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    def test_users_home_template(self):
        response = self.client.get('/lists/templates/')
        self.assertTemplateUsed(response,'home.html')