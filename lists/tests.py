from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
for lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_users_home_template(self):
        response = self.client.get('/',data = {'item_text':'A new list item'})
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        seconde_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(seconde_saved_item.text, 'Item the second')
        self.assertEqual(seconde_saved_item.text, 'Item the second')a