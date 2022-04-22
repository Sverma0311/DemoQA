from actions.actions import Actions
from utility.loggerUtil import Log


class HomePage:
    TITLE_HOME = "//*[@id='app']/header/a/img"

    def __init__(self, page):
        self.page = page
        self.action = Actions(self.page)

    def verify_home_page(self):
        exp_title = self.action.get_text(self.TITLE_HOME)
        Log.loggen().info(exp_title)
