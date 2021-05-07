from selenium import webdriver #导入包 webdriver
import unittest

browser = webdriver.Chrome()  #默认webdriver是chrome
browser.get('http://localhost:8000') #本地网址
assert 'To-Do' in browser.title,"Brower title was"+browser.title
#设置网页标题

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower = webdriver.Chrome()

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get('https://localhost:8000')
        self.assertIn('To-Do',self.brower.title)
        self.fail('finish the test')

if __name__=='__main__':
    unittest.main(warnings="ignore")