# Source: https://github.com/birdlinux/lotus-vscode

from ..base import ColorPalette, Color

BLACK = Color(
    "black",
    (24, 24, 24),
    "#181818",
    (0, 0, 9.41),
)

BACKGROUND = Color(
    "background",
    (24, 24, 24),
    "#181818",
    (0, 0, 9.41),
)

BROWN = Color(
    "brown",
    (143, 103, 70),
    "#8f6746",
    (27.12, 34.27, 41.76),
)

ORANGE = Color(
    "orange",
    (222, 152, 64),
    "#DE9840",
    (222, 152, 64),
)
RED = Color(
    "red",
    (244, 72, 133),
    "#F44885",
    (338.72, 88.66, 61.96),
)

PINK = Color(
    "pink",
    (191, 111, 193),
    "#BF6FC1",
    (191, 111, 193),
)
PURPLE = Color(
    "purple",
    (158, 119, 184),
    "#9E77B8",
    (276, 31.4, 59.41),
)

BLUE = Color(
    "blue",
    (111, 161, 221),
    "#6FA1DD",
    (212.73, 61.8, 65.1),
)

CYAN = Color(
    "cyan",
    (46, 219, 220),
    "#2EDBDC",
    (180.34, 71.31, 52.16),
)

GREEN = Color(
    "green",
    (143, 215, 128),
    "#8FD780",
    (109.66, 52.1, 67.25),
)


LotusDark = ColorPalette(
    name="LotusDark",
    colors_list=[
        BLACK,
        BACKGROUND,
        BROWN,
        ORANGE,
        RED,
        PINK,
        PURPLE,
        BLUE,
        CYAN,
        GREEN,
    ]
)