from enum import Enum
from utils.identifiers import tinder_ids, bumble_ids

class TinderDialogs(Enum):
    MATCH = tinder_ids["match_dialog"]
    END = tinder_ids["tinder_plus_dialog"]

class BumbleDialogs(Enum):
    END = bumble_ids["end_of_line"]

