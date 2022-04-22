import pytest

from pages.homePage import HomePage
from tests.baseTest import BaseTest
from ddt import ddt, data, unpack
from utility.dataReader import DataReader


class TestHomePage(BaseTest):
    # @pytest.mark.parametrize('a, b', DataReader.read_data_from_csv(".//testData//homePage.csv"))
    def test_home_page(self):
        home_page = HomePage(self.page)
        home_page.verify_home_page()
