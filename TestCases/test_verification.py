import unittest
from appium import webdriver
from quoraAutomation.Page_Objects import LoginPage


class LoginLogout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=
                                           {
                                               "platformName": "Android",
                                               "platformVersion": "6.0.1",
                                               "deviceName": "android",
                                               "appPackage": "com.quora.android",
                                               "appActivity": "com.quora.android.components.activities.LauncherActivity",
                                               "udid": "320849220ee571bd"
                                           }
                                       )
        self.driver.implicitly_wait(30)


    def test_main(self):

        credentialsPage= LoginPage(self.driver).logging()

        credentialsPage.enterEmail().send_keys('lodestoneq@gmail.com')
        credentialsPage.enterPassword().send_keys('Asdf#123')
        credentialsPage.clicikngDone().click()

        credentialsPage.retrievingStatus()
        credentialsPage.goBack().click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
