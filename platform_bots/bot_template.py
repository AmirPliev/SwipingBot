from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

import time

class SwipingBot(ABC):
    def __init__(self, driver, blockades, identifiers):
        self.driver = driver
        self.blockades = blockades
        self.ids = identifiers
        
    def run(self):
        """Initiate the overall process."""
        print(f"[BOOT] Starting up {self.__class__.__name__}")
        self._go_to_website()
        self._login()
        self._handle_popups_before_swiping()
        self._swiping()
        return self._create_results_dict()

    def _go_to_website(self):
        """Open website and wait."""
        self.driver.get(self.website)
        time.sleep(2)
        print("[BOOT] Opened website.")

    def _swiping(self):
        """
        Perform the main swiping loop:
        1. We try to swipe.
        2. If that doesn't work, we look for possible blocks.
        3. If we find a block we have anticipated, we deal with it (aka: matches, no more likes)
        4. If we don't know what is happening, we break off anyway.
        """
        self.likes = 0
        self.swipes = 0
        self.matches = 0

        time.sleep(5)
        while True:
            print("[RUN] Swiping")

            try:
                self._perform_swipe()
                self.swipes +=1 
            except:
                print("[BLOCK] Couldn't swipe, finding out why.")
                blockade = self._check_blockades()

                if blockade:
                    continue_program = self._handle_blockade(blockade)
                    if not continue_program:
                        print("[TERMINATION] Breaking Off.")
                        break
                        
                else:
                    print("[TERMINATION] Something went wrong? Investigate here!")
                    break
                
            time.sleep(2)

    def _create_results_dict(self):
        """Package up our results after swiping."""
        results = {
            "Likes": self.likes,
            "Swipes": self.swipes,
            "Matches": self.matches,
        }
        return results

    def _like(self):
        """Perform a like, and increase the likes counter."""
        self.driver.find_element(By.XPATH, self.ids["like_btn"]).click()
        print("[RUN] Liked!")
        self.likes += 1

    def _dislike(self):
        """Perform a dislike."""
        self.driver.find_element(By.XPATH, self.ids["dislike_btn"]).click()
        print("[RUN] Disliked!")

    def _check_blockades(self):
        """Loop through the given blockades and check if they are what is blocking us."""
        print(f"[BLOCK] Looking for blockades: {[block.name for block in self.blockades]}")
        for dialog_type in self.blockades:
            try:
                self.driver.find_element(By.XPATH, dialog_type.value)
                print(f"[BLOCK] Found the following block {dialog_type.name}")
                return dialog_type
            except:
                print(f"[BLOCK] {dialog_type} not found, moving on")
                pass
        print("[BLOCK] Nothing found, continuing")
        return None

    @abstractmethod
    def _login(self):
        pass

    @abstractmethod
    def _handle_popups_before_swiping(self):
        pass

    @abstractmethod
    def _perform_swipe(self):
        pass

    @abstractmethod
    def _handle_blockade(self, blockade):
        pass
