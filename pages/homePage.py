from actions.actions import Actions
from pages.elementsPage import ElementsPage
from utility.loggerUtil import Log
from playwright.async_api import expect


class HomePage:
    IMAGE_TOOLS = "//*[@id='app']/header/a/img"
    IMAGE_SELENIUM = "//*[@id='app']/div/div/div[1]/a/img"
    LINK_ELEMENTS = "text=Elements"
    PAGE_TITLE = ".main-header"

    def __init__(self, page):
        self.page = page
        self.action = Actions(self.page)

    def verify_home_page(self):
        page_image = self.action.get_attribute(self.IMAGE_TOOLS, 'src')
        assert 'Toolsqa' in page_image, "page image is not displayed"
        assert 'Selenium' in self.action.get_attribute(self.IMAGE_SELENIUM, 'alt')

    def click_on_element(self):
        self.action.double_click(self.LINK_ELEMENTS)
        print("##################################################")
        Log.loggen().info(self.action.get_text("title: ", self.PAGE_TITLE))
        Log.loggen().info("logs")
        return ElementsPage(self.action)
