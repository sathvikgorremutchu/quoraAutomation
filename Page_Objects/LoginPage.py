from quoraAutomation.Page_Objects import BasePage
from quoraAutomation.Page_Objects import CredentialsPage
from appium.webdriver.common.mobileby import By

class LoginPage(BasePage):

    noneOption=(By.XPATH,'//android.widget.LinearLayout[@content-desc="Choose an Account"]/android.widget.LinearLayout/android.widget.Button')
    loginButton=(By.XPATH,"//android.view.View[@text='Login']")



    def logging(self):
        self.driver.find_element(*LoginPage.noneOption).click()
        self.driver.find_element(*LoginPage.loginButton).click()
        return CredentialsPage(self.driver)
