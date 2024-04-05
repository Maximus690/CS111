import sys
import requests
from bs4 import BeautifulSoup


def scavenger_hunt(url, html_element, attribute, output_file):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print('Error fetching {url}: {e}')
            sys.exit(1)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        # print("searching for", html_element, "with attribute", attribute)
        elements = soup.find(html_element, {attribute: True})
        # print(elements)
        if elements is None:
            print('no elements found, this is stupid')
            sys.exit(1)
        next_url, next_element, next_attribute = elements[attribute].split(',')
        if next_attribute.strip() == 'final':
            with open(output_file,'w') as file:
                file.write(elements[attribute])
            print("Congratulations! You found final")
            break
        else:
            url = next_url.strip()
            html_element = next_element.strip()
            attribute = next_attribute.strip()



def main():
    if len(sys.argv) != 5:
        print("Usage: python lab21.py <URL> <HTML element> <Attribute> <Output file>")
        sys.exit(1)

    url = sys.argv[1]
    html_element = sys.argv[2]
    attribute = sys.argv[3]
    output_file = sys.argv[4]

    scavenger_hunt(url, html_element, attribute, output_file)


if __name__ == "__main__":
    main()
