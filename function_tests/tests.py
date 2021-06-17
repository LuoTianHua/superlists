from selenium import webdriver #导入包 webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
#browser = webdriver.Firefox( executable_path=r"C:\Program Files\Mozilla Firefox\firefox.exe")


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.brower = webdriver.Firefox()
    def tearDown(self):
        self.brower.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get(self.live_server_url)
        self.assertIn('To-Do',self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        inputbox = self.brower.find_element_by_id('id_new_item')

        inputbox.send_keys('Use peachcock feathers to make a fly')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: But peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')



        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: But peaceock feathers',[row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        self.fail('finish the test')

