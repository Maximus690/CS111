from byuimage import Image
import sys


def display_image(file):
    image = Image(file)
    image.show()


def validate_commands(arg):
    command = arg[1]
    if command == "-d":
        return len(arg) == 3
    elif command == "-k":
        return len(arg) == 5
    elif command == "-s":
        return len(arg) == 4
    elif command == "-g":
        return len(arg) == 4
    elif command == "-b":
        return len(arg) == 8
    elif command == "-f":
        return len(arg) == 4
    elif command == "-m":
        return len(arg) == 4
    elif command == "-c":
        return len(arg) == 8
    elif command == "-y":
        return len(arg) == 7
    return False


def sepia(infile, outfile):
    image = Image(infile)
    for pixel in image:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        pixel.red = true_red
        pixel.green = true_green
        pixel.blue = true_blue
    image.save(outfile)


def grayscale(infile, outfile):
    image = Image(infile)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    image.save(outfile)


def darken(infile, outfile, darken_value):
    image = Image(infile)
    # image2 = Image(outfile)
    percent = 1 - float(darken_value)
    for pixel in image:
        pixel.red = pixel.red * percent
        pixel.green = pixel.green * percent
        pixel.blue = pixel.blue * percent
    image.save(outfile)


def border(filename, outfile, thickness, red, green, blue):
    image = Image(filename)
    new_width = image.width + 2 * thickness
    new_height = image.height + 2 * thickness
    border_image = Image.blank(new_width, new_height)
    for y in range(0, new_height):
        for x in range(0, new_width):
            if x < thickness or x >= new_width - thickness or y < thickness or y >= new_height - thickness:
                new_pixel = border_image.get_pixel(x, y)
                new_pixel.red = red
                new_pixel.green = green
                new_pixel.blue = blue
    for y in range(0, image.height):
        for x in range(0, image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = border_image.get_pixel(x+thickness, y+thickness)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    border_image.save(outfile)


def flipped(filename, outfile):
    image = Image(filename)
    flipped_image = Image.blank(image.width, image.height)
    for y in range(0, image.height):
        for x in range(0, image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = flipped_image.get_pixel(x, image.height - y - 1)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    flipped_image.save(outfile)


def mirror(filename, outfile):
    image = Image(filename)
    mirror_image = Image.blank(image.width, image.height)
    for y in range(0, image.height):
        for x in range(0, image.width):
            pixel = image.get_pixel(x, y)
            new_pixel = mirror_image.get_pixel(image.width - x - 1, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    mirror_image.save(outfile)


def collage(image1, image2, image3, image4, outfile, border_thickness):
    image1 = Image(image1)
    image2 = Image(image2)
    image3 = Image(image3)
    image4 = Image(image4)
    new_width = image1.width * 2 + border_thickness * 3
    new_height = image1.height * 2 + border_thickness * 3
    collage_image = Image.blank(new_width, new_height)
    for pixel in collage_image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = 0
    for y in range(0, image1.height):
        for x in range(0, image1.width):
            pixel = image1.get_pixel(x, y)
            new_pixel = collage_image.get_pixel(x + border_thickness, y + border_thickness)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    for y in range(0, image2.height):
        for x in range(0, image2.width):
            pixel = image2.get_pixel(x, y)
            new_pixel = collage_image.get_pixel(x + image1.width + border_thickness * 2, y + border_thickness)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    for y in range(0, image3.height):
        for x in range(0, image3.width):
            pixel = image3.get_pixel(x, y)
            new_pixel = collage_image.get_pixel(x + border_thickness, y + image1.height + border_thickness * 2)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    for y in range(0, image4.height):
        for x in range(0, image4.width):
            pixel = image4.get_pixel(x, y)
            new_pixel = collage_image.get_pixel(x + image1.width + border_thickness * 2, y + image1.height + border_thickness * 2)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    collage_image.save(outfile)


def green_screen(foreground, background, outfile, threshold, factor):
    foreground = Image(foreground)
    background = Image(background)
    new_width = foreground.width
    new_height = foreground.height
    edited_image = Image.blank(new_width, new_height)
    for y in range(0, foreground.height):
        for x in range(0, foreground.width):
            pixel1 = foreground.get_pixel(x, y)
            pixel2 = background.get_pixel(x, y)
            new_pixel = edited_image.get_pixel(x, y)
            average = (pixel1.red + pixel1.green + pixel1.blue) / 3
            if pixel1.green > threshold and pixel1.green >= factor * average:
                new_pixel.red = pixel2.red
                new_pixel.green = pixel2.green
                new_pixel.blue = pixel2.blue
            else:
                new_pixel.red = pixel1.red
                new_pixel.green = pixel1.green
                new_pixel.blue = pixel1.blue
    edited_image.save(outfile)


def main(arg):
    if not validate_commands(arg):
        return
    command = arg[1]
    if command == "-d":
        display_image(arg[2])
    if command == "-k":
        darken(arg[2], arg[3], arg[4])
        display_image(arg[3])
    if command == "-s":
        sepia(arg[2], arg[3])
        display_image(arg[3])
    if command == "-g":
        grayscale(arg[2], arg[3])
        display_image(arg[3])
    if command == "-b":
        border(arg[2], arg[3], int(arg[4]), int(arg[5]), int(arg[6]), int(arg[7]))
        display_image(arg[3])
    if command == "-f":
        flipped(arg[2], arg[3])
        display_image(arg[2])
    if command == "-m":
        mirror(arg[2], arg[3])
        display_image(arg[2])
    if command == "-c":
        collage(arg[2], arg[3], arg[4], arg[5], arg[6], int(arg[7]))
        display_image(arg[6])
    if command == "-y":
        green_screen(arg[2], arg[3], arg[4], int(arg[5]), float(arg[6]))
        display_image(arg[4])


if __name__ == "__main__":
    main(sys.argv)
