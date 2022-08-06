
# Swiping Bot

This repository contains a python bot that automatically opens up your Tinder and/or Bumble account and starts swiping for you. 
It's been made with as much modularity as possible in mind, meaning that you can add and/or remove whatever platform
you want/can swipe on. 

## What does it do
1. Goes to the website and logs in.
2. Swipes on: \
    a. Tinder \
    b. Bumble \
    Until there are not more likes available. 
2. Sends a message to a match when it occurs (only on Tinder)
3. Sends you a message on Telegram with a report. 

## Setup
1. Clone the repo and open the directory:
    ```
    git clone git@github.com:AmirPliev/SwipingBot.git
    cd SwipingBot
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    Make sure to read the docs for the library: [telegram-send](https://www.rahielkasim.com/telegram-send/docs/#installation)
    This will help you set up a channel on Telegram for you to receive report messages. 

3. Rename the `configs.py.example` to `configs.py`
    ```
    mv configs.py.example configs.py
    ```

4. Open the `configs.py` file and fill in your facebook username and password, as well as an opener for when you hit a match.

5. Then just run the script:
    ```python run.py```

That's it! Now you could automate it using cron to run every day or at whatever regular time interval you want.


## Possible future improvements

- [ ] Implement Match handling for Bumble (right now there's nothing, it just breaks.)
- [ ] Login using different methods than Facebook.
- [ ] Additional platforms (They need to have webpages.)