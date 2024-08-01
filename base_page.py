class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://bashadventure.ru/activities/gory/"
        self.cookies_message = ("//div[contains(@class, 'marketing-popup')]"
                                "//span[contains(text(), 'Принимаю')]")

    def open_site(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def go_to_back(self):
        self.driver.back()

    def close_modal_cookies_massage(self):
        self.driver.find_elemrnt(By.XPATH, self.cookies_message).click()
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located(By.XPATH, self.cookies_message))
        #     )
        #     element.click()
        # finally:
        #     pass