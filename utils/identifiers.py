tinder_ids  = {
    "like_btn": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'),
    "like_btn2": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'),
    "dislike_btn": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button'),    
    "login_btn": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'),
    "facebook_login_btn": str('//*[@aria-label="Log in with Facebook"]'),
    "first_cookies_btn": str('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span'),
    "second_cookies_btn": str('//*[@aria-label="Allow"]'),
    "allow_location_btn": str('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button'),
    "allow_notifications_btn": str('//*[@aria-label="Enable"]'),
    "1st_like_btn": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'),
    "tinder_plus_dialog": str('/html/body/div[2]/main/div/div[3]/button[1]'),
    "match_dialog": str("//*[@placeholder='Say something nice!']"),
    "match_message_field": str("//*[@type='submit']"),
    "loc_element": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div/div[2]/div[2]'),
    "loc_element2": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]'),
    "loc_element3": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/div/div[2]/div/div[2]/div/div[2]'),
    "more_info_expand": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div[3]/button'),
    "undo_expand": str('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a'),
    "info_rows": str("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div")
}

bumble_ids  = {
    "like_btn": str('/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'),
    "dislike_btn": str('/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span'),
    "cookie_frame": str('//*[@id="sp_message_iframe_635134"]'),
    "cookie_accept": str("//*[@title='Accept All']"),
    "sign_in_button": str('/html/body/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a'),
    "facebook_signin1": str('/html/body/div/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span'),
    "facebook_signin2": str('/html/body/div/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[1]/div/span/span[2]/span'),
    "continue_button": str('/html/body/div/div/div[1]/div[1]/div/div[2]/div/div/div/section/div/div/div/div/div/span/span/span/span'),
    "end_of_line": str('/html/body/div/div/div[1]/main/div[2]/div/div/span/div/section/div/div[2]/div/span/span/span/span'),
    "exit_pay_btn": str('/html/body/div/div/div[1]/div[1]/div/div[2]/div/div[2]'),
    "continue_after_match_btn": str('/html/body/div/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div/span/span/span/span'),
    "second_like_btn": str('/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[4]/div/div[1]/span'),
}

facebook_ids = {
    "cookies_btn": str('//*[@title="Only allow essential cookies"]'),
    "username_field": str('//*[@id="email"]'),
    "pass_field": str('//*[@id="pass"]'),
    "login_btn": str('//*[@name="login"]'),
}


def get_name_from_id(dictionary, identifier):
    """Get the name of the button when only id is known."""
    return list(dictionary.keys())[list(dictionary.values()).index(identifier)]
