import time
from utility.loggerUtil import Log


class Actions:
    BUTTON_YEAR = "//*[contains(@style,'visibility: visible')]//button[contains(@id,'cal--Head-B2')]"
    BUTTON_MONTH = "//*[contains(@style,'visibility: visible')]//button[contains(@id,'cal--Head-B1')]"
    YEARS = "//*[contains(@style,'visibility: visible')]//div[contains(@id,'cal--YP')]/div/div"
    MONTHS = "//*[contains(@style,'visibility: visible')]//div[contains(@id,'cal--MP')]/div/div"
    DAYS = "//*[contains(@style,'visibility: visible')]//*[contains(@id,'-cal--Month0-days')]/div[not(@aria-disabled)]"
    PREV_ARROW = "//*[contains(@style,'visibility: visible')]//button[contains(@id,'-cal--Head-prev')]"
    NEXT_ARROW = "//*[contains(@style,'visibility: visible')]//button[contains(@id,'-cal--Head-next')]"
    BUTTON_OK = "//*[contains(@style,'visibility: visible')]//button[contains(@id,'OK')]"
    TEXTBOX_FILTER = "input[placeholder='Filter']"
    BUTTON_OK = "//bdi[text()='OK']/parent::span/parent::span/parent::button"

    def __init__(self, page):
        self.page = page

    def locator(self, locator):
        self.page.locator(locator)

    def click(self, locator=None, index=None):
        if locator is not None and index is not None:
            self.page.locator(locator).nth(index).click(force=True)
        else:
            self.page.locator(locator).click(force=True)

    def fill(self, locator, text):
        self.page.locator(locator).press('Control+A')
        self.page.locator(locator).press('Delete')
        self.page.locator(locator).fill(text)

    def check_on_checkbox(self, locator=None, index=None):
        if locator is not None and index is not None:
            if not self.page.locator(locator).nth(index).is_checked():
                self.page.locator(locator).nth(index).check(force=True)
        else:
            if not self.page.locator(locator).is_checked():
                self.page.locator(locator).check(force=True)

    def uncheck_on_checkbox(self, locator):
        if self.page.locator(locator).is_checked():
            self.page.locator(locator).uncheck()

    def check_on_radiobutton(self, locator=None, index=None):
        if locator is not None and index is not None:
            if not self.page.locator(locator).nth(index).is_checked():
                self.page.locator(locator).nth(index).check()
        else:
            if not self.page.locator(locator).is_checked():
                self.page.locator(locator).check()

    def uncheck_on_radiobutton(self, locator):
        if self.page.locator(locator).is_checked():
            self.page.locator(locator).uncheck()

    def select_by_value(self, locator, value):
        return self.page.locator(locator).select_option(value)

    def select_by_index(self, locator, index):
        return self.page.locator(locator).select_option(index=index)

    def select_by_name(self, locator, name):
        return self.page.locator(locator).select_option(label=name)

    def get_text(self, locator=None, index=None):
        if locator is not None and index is not None:
            return self.page.locator(locator).nth(index).inner_text()
        else:
            return self.page.locator(locator).inner_text()

    def element_size(self, locator):
        return self.page.locator(locator).count()

    def scroll_into_view(self, locator=None, index=None):
        if locator is not None and index is not None:
            self.page.locator(locator).nth(index).scroll_into_view_if_needed()
        else:
            self.page.locator(locator).scroll_into_view_if_needed()

    def get_attribute(self, locator, attribute_name):
        return self.page.locator(locator).get_attribute(attribute_name)

    def upload_file(self, locator, file_name):
        self.page.locator(locator).set_input_files(file_name)

    def frame(self, locator):
        f = self.page.frame_locator(locator)
        return Actions(f)

    def double_click(self, locator):
        self.page.locator(locator).dblclick()

    def right_click(self, locator):
        self.page.locator(locator).click(button='right')

    def press_enter_key(self, locator):
        self.page.locator(locator).press('Enter')

    def press_tab_key(self, locator):
        self.page.locator(locator).press('Tab')

    def press_key(self, locator=None, key_name=None, index=None):
        if locator is not None and index is not None:
            self.page.locator(locator).nth(index).press(key_name)
        elif locator is not None and key_name is not None:
            self.page.locator(locator).press(key_name)

    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def is_hidden(self, locator):
        return self.page.locator(locator).is_hidden()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_disabled(self, locator):
        return self.page.locator(locator).is_disabled()

    def is_editable(self, locator):
        return self.page.locator(locator).is_editable()

    def drag_and_drop(self, source_locator, target_locator):
        self.page.drag_and_drop(source_locator, target_locator)

    def back(self):
        self.page.go_back()

    def forward(self):
        self.page.go_forward()

    def keyboard_key(self, key_name):
        self.page.keyboard.press(key_name)

    def type(self, text):
        self.page.keyboard.type(text)

    def scroll(self, horizontal, vertical):
        self.page.mouse.wheel(horizontal, vertical)

    def select_product(self, *products_hierarchy):
        a = 0
        for product in products_hierarchy:
            a = a + 1
            index_locator = "//*[text()=" + "'" + product + "'" + "]/parent::div/parent::div/parent::div/parent::td/parent::tr"
            if not a == len(products_hierarchy):
                locator = "//*[text()=" + "'" + product + "'" + "]/parent::div/parent::div/parent::div/span"
                self.press_key(locator, "ArrowDown")

                time.sleep(1)
                self.click(locator)
            if a == len(products_hierarchy) - 1:
                c = int(self.get_attribute(index_locator, "data-sap-ui-rowindex"))
            elif a == len(products_hierarchy):
                b = int(self.get_attribute(index_locator, "data-sap-ui-rowindex"))

        self.check_on_checkbox(
            "//div[@id='__table7-sapUiTableRowHdrScr']/div[@aria-level='" + str(a) + "']/span[@role='checkbox']",
            (b - c - 1))

    def select_date(self, str_date, locator):
        date = int(str_date.split("/")[0])
        month = int(str_date.split("/")[1])
        year = int(str_date.split("/")[2])
        self.click(locator)
        self.click(self.BUTTON_YEAR)

        is_year = True
        while is_year:
            count = self.element_size(self.YEARS)
            min_year = self.get_text(self.YEARS, 0)
            if (year >= int(min_year)) and (year <= (int(min_year) + count - 1)):
                i = year - int(min_year)
                print("years : ", self.get_text(self.YEARS, i))
                self.click(self.YEARS, i)
                is_year = False
            elif year < int(min_year):
                self.click(self.PREV_ARROW)
            else:
                self.click(self.NEXT_ARROW)

        self.click(self.BUTTON_MONTH)
        self.click(self.MONTHS, month - 1)
        self.click(self.DAYS, date - 1)
        self.click(self.BUTTON_OK)

    def get_project_detail(self, project_name, *column_names):
        row = (self.get_attribute("//*[text()='" + project_name + "']", "id")[-1])
        id_attribute = self.get_attribute("//*[text()='" + project_name + "']/parent::div/parent::td", "id")
        table = (id_attribute[len('__table')])
        project_detail = {}
        for column_name in column_names:
            column = \
                self.get_attribute("//*[text()='" + column_name + "']/parent::label/parent::div/parent::div", "id")[-1]
            project_detail[column_name] = {self.get_text("#__table{}-rows-row{}-col{}".format(table, row, column))}
        Log.loggen().info(project_detail)
        return project_detail

    def open_project(self, project_name, column_name):
        self.click("//*[text()='{}']".format(project_name))
        print("locator: ", "//*[text()='{}']".format(project_name))
        column = self.get_attribute("//*[text()='" + column_name + "']/parent::label/parent::div/parent::div",
                                    "data-sap-ui-colindex")
        print("column: ", column)
        locator = "//*[contains(@id,'col" + column + "-row')]"
        size = self.element_size(locator)
        i = 0
        column_list = []
        while size > i:
            print(self.get_text(locator, i))
            text = self.get_text(locator, i)
            if len(text) > 0:
                column_list.append(text)
            self.press_key(locator, "ArrowDown", i)
            time.sleep(1)
            i = i + 1
            if i == size - 1:
                while len(self.get_text(locator, i)) > 0:
                    column_list.append(self.get_text(locator, i))
                    i = 0
                    while size - 1 > i:
                        print("inside while ", i, self.get_text(locator, i))
                        text = self.get_text(locator, i)
                        if text not in column_list and len(text) > 0:
                            column_list.append(text)
                        self.press_key(locator, "ArrowDown", i)
                        time.sleep(1)
                        i = i + 1

        Log.loggen().info(column_list)
        print("Size of list: ", len(column_list))
        return column_list

    def select_specific_row(self, row_name):
        self.fill(self.TEXTBOX_FILTER, row_name)
        row_locator = "//*[text()='" + row_name + "']/parent::div/parent::td/parent::tr"
        self.click(row_locator)
        self.click(self.BUTTON_OK)

    def wait_for_locator(self, locator):
        self.page.locator(locator).wait_for()
