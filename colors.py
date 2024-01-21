# We use the colored module to help us out a little.
from colored import Fore as _Fore
from colored import Back as _Back
from colored import Style as _Style

type _BaseColor = {"r": int, "g": int, "b": int}


class _Core:
    def __init__(self, color: _BaseColor):
        self.color = color
        self.fore = _Fore.rgb(color["r"], color["g"], color["b"])
        self.back = _Back.rgb(color["r"], color["g"], color["b"])

    def apply_f(self, string: str) -> str:
        return f"{self.fore}{string}{_Style.reset}"

    def apply_b(self, string: str) -> str:
        return f"{self.back}{string}{_Style.reset}"

    def remove(self, string: str) -> str:
        return string.replace(self.fore, "").replace(self.back, "").replace(_Style.reset, "")


_base = {
    "red": {"r": 245, "g": 78, "b": 66},
    "blue": {"r": 78, "g": 129, "b": 217},
    "yellow": {"r": 216, "g": 224, "b": 56},
    "green": {"r": 91, "g": 235, "b": 130},
    "purple": {"r": 199, "g": 91, "b": 235},
    "orange": {"r": 235, "g": 175, "b": 91},
    "pink": {"r": 218, "g": 91, "b": 235},
    "grey": {"r": 46, "g": 46, "b": 46},
    "black": {"r": 0, "g": 0, "b": 0},
    "white": {"r": 255, "g": 255, "b": 255}
}

red = _Core(_base["red"])
blue = _Core(_base["blue"])
yellow = _Core(_base["yellow"])
green = _Core(_base["green"])
purple = _Core(_base["purple"])
orange = _Core(_base["orange"])
pink = _Core(_base["pink"])
grey = _Core(_base["grey"])
black = _Core(_base["black"])
white = _Core(_base["white"])

_all_colors = [red, blue, yellow, green, purple, orange, pink, grey, black, white]


def remove_all_colors(string) -> str:
    new_string: str = string
    for color in _all_colors:
        new_string = color.remove(new_string)
    return new_string
