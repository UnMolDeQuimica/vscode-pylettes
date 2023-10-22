import colorsys

def hex_to_rgb(hex_color):
    # Remove the "#" character if present
    hex_color = hex_color.lstrip('#')

    # Check if the hex color code is valid
    if not all(c in '0123456789ABCDEFabcdef' for c in hex_color) or len(hex_color) != 6:
        raise ValueError("Invalid hexadecimal color code")

    # Convert the hex values to integers
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)



def hex_to_hsl(hex_color):
    # Remove the "#" character if present
    hex_color = hex_color.lstrip('#')

    # Check if the hex color code is valid
    if not all(c in '0123456789ABCDEFabcdef' for c in hex_color) or len(hex_color) != 6:
        raise ValueError("Invalid hexadecimal color code")

    # Convert the hex values to integers
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0

    # Convert RGB to HSL
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    
    # Scale H, S, and L to the typical HSL range
    h = int(h * 360)
    s = int(s * 100)
    l = int(l * 100)

    return (h, s, l)
 
def hex_to_class(name: str, hex: str) -> str:
    rgb = hex_to_rgb(hex)
    hsl = hex_to_hsl(hex)
    print(f"{name.upper()} = Color(")
    print(f"    \"{name.lower()}\",")
    print(f"    {rgb},")
    print(f"    \"{hex.upper()}\",")
    print(f"    {hsl}")
    print(f")")
    print("")

hex_to_class("dark2", "#131313")
hex_to_class("dark1", "#191919")
hex_to_class("background", "#222222")
hex_to_class("text", "#f7f1ff")
hex_to_class("accent1", "#fc618d")
hex_to_class("accent2", "#fd9353")
hex_to_class("accent3", "#fce566")
hex_to_class("accent4", "#7bd88f")
hex_to_class("accent5", "#5ad4e6")
hex_to_class("accent6", "#948ae3")
hex_to_class("dimmed1", "#bab6c0")
hex_to_class("dimmed2", "#8b888f")
hex_to_class("dimmed3", "#69676c")
hex_to_class("dimmed4", "#525053")
hex_to_class("dimmed5", "#363537")

