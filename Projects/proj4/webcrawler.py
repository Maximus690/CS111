import sys
import requests
import shutil
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from RequestGuard import RequestGuard
from image_processing import sepia, grayscale, flipped, mirror


def validate_arguments(arg):
    # Implement argument validation logic here
    if not len(arg) == 5:
        print("invalid arguments")
        return False
    command = arg[1]
    valid_commands = ["-c", "-p", "-i"]
    if command not in valid_commands:
        print("invalid arguments")
        return False
    if arg[4] not in ['-s', '-g', '-f', '-m'] and arg[1] == "-i":
        print("invalid arguments")
        return False
    return True


def count_links(url, output_1, output_2):
    links = []
    domain = re.match(".+org|.+edu|.+com", url).group(0)
    RG = RequestGuard(domain)
    links.append(url)
    bin = {}
    while len(links) > 0:
        link = links.pop(0)
        if link in bin:
            bin[link] += 1
        if link not in bin:
            bin[link] = 1
            if RG.can_follow_link(link):
                page = requests.get(link)
                html = BeautifulSoup(page.content, 'html.parser')
                anchor_tags = html.find_all('a')
                for tag in anchor_tags:
                    if tag.get('href').startswith('#'):
                        bin[link] += 1
                    elif tag.get('href').startswith('/'):
                        if link[-1] == '/':
                            links.append(link[0:-1] + tag.get('href'))
                        else:
                            links.append(link + tag.get('href'))
                    elif tag.get('href').startswith('http'):
                        if "#" in tag.get("href"):
                            links.append(tag.get('href')[0:tag.get('href').index("#")])
                        else:
                            links.append(tag.get('href'))
                    else:
                        match = re.match("(.+)page\d\.html", link).group(1)
                        links.append(match + tag.get('href'))
    y, x, i = plt.hist(bin.values(), bins = [i for i in range(min(bin.values()),max(bin.values()) + 2)])
    plt.savefig(output_1)
    x = x[0:-1]
    with open(output_2, 'w') as file:
        for i in range(len(x)):
            file.write(f"{x[i]},{y[i]}\n")


def plot_data(url, output_1, output_2):
    domain = re.match(".+org|.+edu|.+com", url).group(0)
    RG = RequestGuard(domain)
    data = RG.make_get_request(url)
    x = []
    y = []
    y2 = []
    y3 = []
    y4 = []
    if data:
        soup = BeautifulSoup(data.content, "html.parser")
        table = soup.find_all("table")
        for i in table:
            if i.attrs["id"] == "CS111-Project4b":
                row = i.find_all("tr")
                for elements in row:
                    try:
                        column = elements.find_all("td")
                        x.append(float(column[0].text))
                        y.append(float(column[1].text))
                        y2.append(float(column[2].text))
                        y3.append(float(column[3].text))
                        y4.append(float(column[4].text))
                    except IndexError:
                        pass
    else:
        return f"This page don't exist none."

    if len(y4) > 0:
        plt.plot(x, y, 'blue', x, y2, "green", x, y3, 'red', x, y4, 'black')

    elif len(y3) > 0:
        plt.plot(x, y, 'blue', x, y2, "green", x, y3, 'red')

    elif len(y2) > 0:
        plt.plot(x, y, 'blue', x, y2, "green")

    elif len(y) > 0:
        plt.plot(x, y, 'blue')

    plt.savefig(output_1)

    with open(output_2, 'w') as file:
        for i in range(len(x)):
            if len(y4) > 0:
                file.write(f"{x[i]},{y[i]},{y2[i]},{y3[i]},{y4[i]}\n")
            elif len(y3) > 0:
                file.write(f"{x[i]},{y[i]},{y2[i]},{y3[i]}\n")
            elif len(y2) > 0:
                file.write(f"{x[i]},{y[i]},{y2[i]}\n")
            elif len(y) > 0:
                file.write(f"{x[i]},{y[i]}\n")


def image_thingy(url, output_prefix, image_filter):
    domain = re.match(".+org|.+edu|.+com", url).group(0)
    RG = RequestGuard(domain)
    data = RG.make_get_request(url)
    if data:
        soup = BeautifulSoup(data.content, "html.parser")
        images = soup.find_all("img", src=True)
        for i in images:
            response = requests.get(url[0:-11] + i.get("src"), stream=True)
            with open(f"{i.get('src')}", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            if image_filter == "-s":
                sepia(i.get("src"), output_prefix + i.get("src"))
            if image_filter == "-g":
                grayscale(i.get("src"), output_prefix + i.get("src"))
            if image_filter == "-f":
                flipped(i.get("src"), output_prefix + i.get("src"))
            if image_filter == "-m":
                mirror(i.get("src"), output_prefix + i.get("src"))


def main():
    # image_thingy('https://cs111.byu.edu/proj/proj4/assets/images.html', "butt", "fart")

    if validate_arguments(sys.argv):
        if sys.argv[1] == "-c":
            count_links(sys.argv[2], sys.argv[3], sys.argv[4])
        if sys.argv[1] == "-p":
            plot_data(sys.argv[2], sys.argv[3], sys.argv[4])
            # plot_data("https://cs111.byu.edu/proj/proj4/assets/data.html", "butt", "fart")
        if sys.argv[1] == "-i":
            image_thingy(sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == "__main__":
    main()
