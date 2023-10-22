import re
import math
import json
import colorsys

colors_thing_text = """
Insert big text with colors
"""

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

                 
def color_similarity(rgb1, rgb2):
    rgb2 = hex_to_rgb(rgb2)
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def find_nearest_color(rgb, color_data):
    min_distance = float('inf')
    nearest_color = None
    for color_name, color_rgb in color_data.items():
        distance = color_similarity(rgb, color_rgb)
        if distance < min_distance:
            min_distance = distance
            nearest_color = color_name
    return nearest_color

with open('colors.txt', 'r') as file:
    lines = file.readlines()

xkcd_color_data = {}

for line in lines:
    match = re.match(r'(.+?)\s+#([0-9A-Fa-f]{6})', line)
    if match:
        color_name = match.group(1)
        hex_value = '#' + match.group(2)
        xkcd_color_data[color_name] = hex_value
        
with open('xkcd_color_data.json', 'w') as json_file:
    json.dump(xkcd_color_data, json_file, indent=4)

with open('xkcd_color_data.json', 'r') as file:
    xkcd_color_data_new = json.load(file)


hex_color_pattern = r'#[0-9A-Fa-f]{6}'

hex_colors = set(re.findall(hex_color_pattern, colors_thing_text))

named_colors = []
for hex_color in hex_colors:
    rgb_color = hex_to_rgb(hex_color)
    nearest_color_name = find_nearest_color(rgb_color, xkcd_color_data_new)
    named_colors.append((hex_color, nearest_color_name))
    

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

included_colors = []
for hex_color, named_color in named_colors:
    if named_color in included_colors:
        continue
    
    rgb = hex_to_rgb(hex_color)
    hsl = hex_to_hsl(hex_color)
    named_color = named_color.replace(" ", "_")
    print(f"{named_color.upper()} = Color(")
    print(f"    \"{named_color.lower()}\",")
    print(f"    {rgb},")
    print(f"    \"{hex_color.upper()}\",")
    print(f"    {hsl}")
    print(f")")
    print("")
    
print("LotusDark = ColorPalette(")
print("    name=\"LotusDark\",")
print("    colors_list=[")
for _, named_color in named_colors:
    named_color = named_color.replace(" ", "_").upper()
    print(f"        {named_color},")
print("    ]")
print(")")


