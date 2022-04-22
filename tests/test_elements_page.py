import pytest

from pages.homePage import HomePage
from tests.baseTest import BaseTest
from utility.dataReader import DataReader


class TestElementsPage(BaseTest):
    # @pytest.mark.parametrize('title', DataReader.read_data_from_csv("elementsPage.csv"))
    def test_elements_page(self):
        element_page = HomePage(self.page)
        element_page.click_on_element()\
            .verify_page_title("Elements")
