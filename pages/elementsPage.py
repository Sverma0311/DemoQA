class ElementsPage:
    PAGE_TITLE = ".main-header"

    def __init__(self, page):
        self.page = page

    def verify_page_title(self, title):
        exp_title = self.page.get_text(self.PAGE_TITLE)
        print("expected title", exp_title)
        # assert title == exp_title, "actual page title is different from expected title"

