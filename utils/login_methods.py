from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from configs import EMAIL, PASS
from utils.identifiers import facebook_ids as ids
import time

def handle_facebook_popup(driver):
    
    print("[BOOT] Trying to log in...")
    time.sleep(3)
    if len(driver.window_handles) == 1:
        return False
    driver.switch_to.window(driver.window_handles[1])

    # Click on cookies
    driver.find_element(By.XPATH, ids["cookies_btn"]).click()

    # Actually Login
    email_field = driver.find_element(By.XPATH, ids["username_field"])
    email_field.send_keys(EMAIL)

    pass_field = driver.find_element(By.XPATH, ids["pass_field"])
    pass_field.send_keys(PASS)
    driver.find_element(By.XPATH, ids["login_btn"]).click()

    driver.switch_to.window(driver.window_handles[0])
    return True






            
