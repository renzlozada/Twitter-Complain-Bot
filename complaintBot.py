import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

my_email = os.environ["my_email"]
my_pass = os.environ["my_pass"]
my_phone = os.environ["my_phone"]


class InternetSpeedXBot:
    def __init__(self):
        self.up = ""
        self.down = ""
        edge_option = webdriver.EdgeOptions()
        edge_option.add_experimental_option(name='detach', value=True)

        self.driver = webdriver.Edge(options=edge_option)
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.maximize_window()

    def get_internet_speed(self):
        """
        Opens up the browser to go to SpeedTest.net to get the Download and Upload Speed.
        :return: prints the DOWN and UP speed
        """
        self.driver.get("https://www.speedtest.net/")
        start_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "start-text")))
        start_button.click()
        self.check_for_modal()
        down_speed = self.wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        self.down = float(down_speed.text)
        up_speed = self.wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.up = float(up_speed.text)
        print(f"Download Speed: {self.down} Mbps\n"
              f"Upload Speed:   {self.up} Mbps\n")

    def check_for_modal(self):
        """
        Method created since there's a dialogue box pop up before getting the results+
        """
        try:
            #  Check if there's a modal window for 'Try Speedtest for Windows/Mac'
            back2test_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')))
            back2test_button.click()
        except NoSuchElementException:
            pass

    def tweet_at_provider(self):
        """
        Opens up a new tab, and visit the Twitter website.
        """
        self.driver.execute_script("window.open('https://twitter.com/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')))
        sign_in_button.click()
        email_field = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        email_field.send_keys(my_email)
        email_field.send_keys(Keys.ENTER)  # This opens up a new modal dialogue where password shows up
        phone_field = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
        phone_field.send_keys(my_phone)
        phone_field.send_keys(Keys.ENTER)
        time.sleep(2)  # Stop-gap
        pass_field = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        pass_field.send_keys(my_pass)
        pass_field.send_keys(Keys.ENTER)

        #  2FA enabled in my account, hence the various self.wait methods

        #  Enters the complaint string using the values from SpeedTest
        text_field_click_first = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        text_field_click_first.click()
        text_field = self.wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        text_field.send_keys(
            f'Hey ISP, why is my internet speed only {self.down} down and {self.up} UP when I pay for 200 down / 200 up?\n'
            f'\n'
            f'- This is created using Python Auto Bot, please ignore\n'
            f'- Teku')
        post_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()

        print('Complaint Posted\n'
              'Program Done')
