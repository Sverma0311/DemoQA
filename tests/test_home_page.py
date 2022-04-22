import pytest

from pages.home_page import HomePage
from tests.baseTest import BaseTest
from ddt import ddt, data, unpack
from utility.dataReader import DataReader


@ddt
class TestHomePage(BaseTest):
    @pytest.mark.parametrize('a, b', DataReader.read_data_from_csv(".//test_data//homePage.csv"))
    def test_home_page(self, a, b):
        home_page = HomePage(self.page)
        home_page.verify_home_page()
        print(a, b)
