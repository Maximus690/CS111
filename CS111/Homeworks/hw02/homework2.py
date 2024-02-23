from byuimage import Image
import sys


def flipped(filename):
    original_image = Image(filename)
    flipped_original_image = Image.blank(original_image.width, original_image.height)
    for y in range(0, original_image.height):
        for x in range(0, original_image.width):
            pixel = original_image.get_pixel(x, y)
            new_pixel = flipped_original_image.get_pixel(x, original_image.height - y - 1)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    return flipped_original_image


def make_borders(filename, thickness, red, green, blue):
    original_image = Image(filename)
    new_width = original_image.width + 2 * thickness
    new_height = original_image.height + 2 * thickness
    border_image = Image.blank(new_width, new_height)
    for y in range(0, new_height):
        for x in range(0, new_width):
            if x < thickness or x >= new_width - thickness or y < thickness or y >= new_height - thickness:
                new_pixel = border_image.get_pixel(x, y)
                new_pixel.red = red
                new_pixel.green = green
                new_pixel.blue = blue
    for y in range(0, original_image.height):
        for x in range(0, original_image.width):
            pixel = original_image.get_pixel(x, y)
            new_pixel = border_image.get_pixel(x+thickness, y+thickness)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    border_image.show()
    return border_image


if __name__ == "__main__":
    pass
