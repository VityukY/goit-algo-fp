import colorsys


def darken_hex_color(color, factor=1.3):

    r, g, b = (
        int(color[1:3], 16) / 255.0,
        int(color[3:5], 16) / 255.0,
        int(color[5:7], 16) / 255.0,
    )
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    v = min(1.0, v * factor)
    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    hex_color = "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))

    return hex_color
