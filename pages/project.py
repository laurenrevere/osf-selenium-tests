import settings
import urllib.parse
from pages.base import OSFBasePage
from selenium.webdriver.common.by import By


class ProjectPage(OSFBasePage):

    locators = dict(
        project_title=(By.ID, 'nodeTitleEditable'),
        identity=(By.CSS_SELECTOR, '#overview > nav#projectSubnav'),
        **OSFBasePage.locators
    )

    def __init__(self, driver, goto=True, guid=''):
        super(self.__class__, self).__init__(driver, goto)
        self.url = urllib.parse.urljoin(settings.OSF_HOME, guid)
