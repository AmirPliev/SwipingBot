

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from platform_bots.tinder_bot import TinderBot 
from platform_bots.bumble_bot import BumbleBot 
from utils.identifiers import bumble_ids, tinder_ids
from utils.enums import TinderDialogs, BumbleDialogs
from utils.package_message import format_results

import telegram_send as telegram


if __name__ == "__main__":
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.preferences["permissions.default.geo"]=1
    driver = webdriver.Firefox(options=opts)
    driver.implicitly_wait(10)

    bots = [
        TinderBot(driver=driver, blockades=TinderDialogs, identifiers=tinder_ids),
        BumbleBot(driver=driver, blockades=BumbleDialogs, identifiers=bumble_ids)
    ]

    results = {}
    for bot in bots:
        bot_name = bot.__class__.__name__
        print(f"\n------------STARTING {bot_name.upper()}------------\n")
        results[bot_name] = bot.run()
        print(f"------------DONE WITH {bot_name.upper()}------------\n")
    driver.quit()

    print("[RESULTS] All Swiping Bots have run. Done!")
    print(f"[RESULTS] Results: {results}")
    telegram.send(messages=[format_results(results)], parse_mode = "markdown")

