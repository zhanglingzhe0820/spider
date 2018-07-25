from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def login(browser, url, username, password):
    browser.get(url+"/x#/login")
    username_input = browser.find_element_by_class_name(
        'input-username')
    password_input = browser.find_element_by_class_name(
        'input-password')
    login_button = browser.find_element_by_id('submitLogin')
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()


class Browser():
    def create(self, url, username, password):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_argument('-headless')
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(chrome_options=options)
        login(browser, url, self.username, self.password)
        sleep(3)
        browser.get(url + "/x#/lottery/ssc/txffc/cg")
        wait = WebDriverWait(browser, 10)
        wait.until(lambda dr: dr.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[1]/div[1]/ul/li[4]').is_displayed())
        target_game_tab = browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[1]/div[1]/ul/li[4]')
        target_game_tab.click()
        target_game_tab_sub = browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[1]/div[2]/dl[1]/dd[2]')
        target_game_tab_sub.click()
        self.browser = browser

    def bet(self, kind, multiple, str):
        target_textArea = self.browser.find_element_by_xpath('//*[@id="bet-input-codearea"]')
        submit_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[3]/div[1]/input[1]')
        yuan_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[1]/div/span[1]')
        jiao_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[1]/div/span[2]')
        fen_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[1]/div/span[3]')
        add_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[2]/div/span[2]')
        minus_btn = self.browser.find_element_by_xpath(
            '//*[@id="componentContainer"]/div/div[1]/div[2]/div[2]/div[2]/span/div/div[1]/div/div[3]/div[2]/div/span[1]')
        target_textArea.send_keys(str)
        if kind == 'yuan':
            yuan_btn.click()
        elif kind == 'jiao':
            jiao_btn.click()
        else:
            fen_btn.click()
        for i in range(multiple - 1):
            add_btn.click()
        sleep(1)
        submit_btn.click()
        for i in range(multiple - 1):
            minus_btn.click()
        sleep(5)
        self.browser.execute_script("document.getElementsByClassName('submit')[1].click()")
        return "success"

    def close(self):
        self.browser.close()
        self.browser.quit()


b = Browser()
