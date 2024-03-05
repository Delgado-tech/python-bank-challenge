from enum import Enum
from colorama import Fore

class Fore_Style(Enum):
    PRIMARY = Fore.RESET  # type = ignore
    SECONDARY = Fore.CYAN  # type = ignore
    SUCCESS = Fore.LIGHTGREEN_EX
    DANGER = Fore.RED  # type = ignore
    WHITE = Fore.WHITE  # type = ignore
    GRAY = Fore.LIGHTBLACK_EX  # type = ignore
    RESET = Fore.RESET  # type = ignore