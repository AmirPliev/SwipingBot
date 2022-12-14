from selenium.webdriver.common.by import By

from platform_bots.bot_template import SwipingBot
from utils.login_methods import handle_facebook_popup
from utils.enums import BumbleDialogs

from utils.identifiers import *

import time
from random import randint


class BumbleBot(SwipingBot):
    def __init__(self, **kwargs):
        super(BumbleBot, self).__init__(**kwargs)
        self.website = "https://am1.bumble.com"

    def _get_rid_of_cookies(self):
        try:
            frame = self.driver.find_element(By.XPATH, self.ids["cookie_frame"])
            self.driver.switch_to.frame(frame)
            self.driver.find_element(By.XPATH, self.ids["cookie_accept"]).click()
        except:
            print("[BOOT] Cookie banner not found? Continuing carefully?")

        self.driver.switch_to.default_content()
        time.sleep(1)

    def _login(self):

        self._get_rid_of_cookies()        
        self.driver.find_element(By.XPATH, self.ids["sign_in_button"]).click()
        self._get_rid_of_cookies()   
        self.driver.find_element(By.XPATH, self.ids["facebook_signin1"]).click()
        handle_facebook_popup(self.driver)

        try:
            print("[BOOT] Trying to press continue")
            self.driver.find_element(By.XPATH, self.ids["continue_button"]).click()
            time.sleep(5)
            print("[BOOT] Trying to press facebook button")
            self.driver.find_element(By.XPATH, self.ids["facebook_signin2"]).click()
        except:
            print("[BOOT] No need to relogin? Continuing carefully.")

    def _handle_popups_before_swiping(self):
        print("[BOOT] No popups handling necessary, moving on.")

    def _perform_swipe(self):
        self._like()

        # probability_limit = int(10 - (self.swipes * 0.2))
        # random_number = randint(0, probability_limit)
        # print(f"[DEBUG] Random number generated: {random_number}, from limit: {probability_limit}")
        # if random_number == 1:
        #     self._dislike()
        # else:
        #     self._like()

    def _handle_blockade(self, blockade):
        if blockade == BumbleDialogs.PLEASE_PAY:
            self.driver.find_element(By.XPATH, self.ids["exit_pay_btn"]).click()
            self.driver.find_element(By.XPATH, self.ids["second_like_btn"]).click()
            return True

        if blockade == BumbleDialogs.MATCH:
            self.driver.find_element(By.XPATH, self.ids["continue_after_match_btn"]).click()
            return True
        
        return False