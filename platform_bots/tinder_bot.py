from selenium.webdriver.common.by import By

from utils.enums import TinderDialogs
from platform_bots.bot_template import SwipingBot
from utils.identifiers import get_name_from_id
from utils.login_methods import handle_facebook_popup

from random import randint
from configs import OPENER
import sys

GEO_LIMIT = 500  # KMs


class TinderBot(SwipingBot):
    def __init__(self, **kwargs):
        super(TinderBot, self).__init__(**kwargs)
        self.website = "https://tinder.com"
        
    def _login(self):
        """Get the login button and enter our details."""
        login_button = self.driver.find_element(By.XPATH, self.ids["login_btn"])
        login_button.click()
        self.driver.find_element(By.XPATH, self.ids["facebook_login_btn"]).click()
        handle_facebook_popup(self.driver)
        print("[BOOT] Logged in!")

    def _handle_popups_before_swiping(self):
        """Deal with all the cookies popups and stuff."""
        popup_sequence = [
            self.ids["first_cookies_btn"],
            self.ids["second_cookies_btn"], 
            self.ids["allow_notifications_btn"],
            self.ids["allow_location_btn"],
            self.ids["1st_like_btn"]
        ]

        counter = 0
        while any(popup_sequence):
            for button in popup_sequence:
                try:
                    self.driver.find_element(By.XPATH, button).click()
                    popup_sequence.remove(button)
                except:
                    print(f"[WARNING] Couldn't find: {get_name_from_id(self.ids, button)}")
            if counter >= 2:
                if any(popup_sequence):
                    list_of_unfound_btns = [
                        get_name_from_id(self.ids, btn) for btn in popup_sequence
                    ]
                    print(f"[WARNING] The following buttons weren't found: {list_of_unfound_btns}, moving on but program might crash.")
                break

            counter += 1

        print("[BOOT] Setup complete. Ready to Swipe.")

    def _perform_swipe(self):
        
        location = self._get_location()
        print(f"[DEBUG] Found the following location: {location}", end="")

        if location == 0:
            return self._pick_randomly()
        else:
            return self._pick_on_location(location)

    def _pick_randomly(self):
        """Like randomly"""
        if randint(1, 10) == 1:
            self._dislike()
        else:
            self._like()

    def _pick_on_location(self, location: int):
        """Pick based on location, makin sure no likes for people far away."""
        if location < GEO_LIMIT and location != 0:
            self._like()
        else:
            self._dislike()

    def _get_location(self):
        """Try and find the location from the profile."""
        for loc_btn in ["loc_element", "loc_element2", "loc_element3"]:
            location = self.get_innerHTML(loc_btn)
            if location:
                return location 

        try:
            self.driver.find_element(By.XPATH, self.ids["more_info_expand"]).click()
            location = self._try_to_find_location_from_expanded_view()
            self.driver.find_element(By.XPATH, self.ids["undo_expand"]).click()
            return location
        except:
            print("[LOCATION] Could not find location, liking randomly.", end="")

        return 0

    def _try_to_find_location_from_expanded_view(self):
        rows_xpath = self.ids["info_rows"]
        all_rows = self.driver.find_elements(By.XPATH, f"{rows_xpath}")
        for div in all_rows:
            content = div.find_elements(By.XPATH, "./*")
            inner_text = content[1].get_attribute('innerHTML')
            if "kilometers" in inner_text:
                location = int(inner_text.split(" ")[0])
                return location

        return 0

    def get_innerHTML(self, element: str):
        try:
            location_element = self.driver.find_element(By.XPATH, self.ids[element])
            str_location = location_element.get_attribute('innerHTML')
            location = int(str_location.split(" ")[0])
            return location
        except:
            return None

    def _deal_with_match(self):
        """Event that handles the moment a match has been encountered."""
        print("[BLOCK] We got a match!")
        self.matches += 1
        message_field = self.driver.find_element(By.XPATH, self.ids["match_dialog"])
        message_field.send_keys(OPENER)
        self.driver.find_element(By.XPATH, self.ids["match_message_field"]).click()
        print("[BLOCK] Sent her a message!")
    
    def _handle_blockade(self, blockade):
        if blockade == TinderDialogs.MATCH:
            self._deal_with_match()
            return True
            
        elif blockade == TinderDialogs.END:
            print("[TERMINATION] Whoops, out of likes, initiating program end.")
            return False

        return False