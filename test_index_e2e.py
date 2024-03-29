import unittest
from selenium import webdriver

class E2ETests(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(exectuable_path)  #not able to download the driver
        self.driver.get('http://localhost:5000')
    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity',self.driver.title)
    def test_page_heading_is_named_entity_finder(self):
        heading=self._find("heading").text
        self.assertEqual('Named Entity Finder',heading)
    def test_page_has_input_for_text(self):
        input_element=self._find('input-text')
        self.assertIsNotNone(input_element)
    def test_page_has_button_for_submit_text(self):
        submit_button=self._find('find-button')
        self.assertIsNone(submit_button)
    def test_submitting_sentence_create_table(self):
        input_element=self._find('input-text')
        submit_button=self._find('find-button')
        input_element.send_kets('France and Germany share border in Europe')
        submit_button.click()
        table=self._find('ner-table')
        self.assertIsNot(table)
    def _find(self,val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')