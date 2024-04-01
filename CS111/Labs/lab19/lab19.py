import requests
from bs4 import BeautifulSoup


def download(url, output_file):
    """Write your code here"""
    stuff = requests.get(url)
    with open(output_file, 'w') as file:
        file.write(stuff.text)


def make_pretty(url, output_file):
    """Write your code here"""
    stuff = requests.get(url)
    soup = BeautifulSoup(stuff.text, 'html.parser')
    with open(output_file, 'w') as file:
        file.write(soup.prettify())


def find_paragraphs(url, output_file):
    """Write your code here"""
    stuff = requests.get(url)
    soup = BeautifulSoup(stuff.content, "html.parser")
    paragraphs = soup.find_all('p')
    with open(output_file, 'w') as file:
        for paragraph in paragraphs:
            file.write("<p>" + paragraph.get_text() + "</p>" + '\n')


def find_links(url, output_file):
    """Write your code here"""
    stuff = requests.get(url)
    soup = BeautifulSoup(stuff.text, 'html.parser')
    links = soup.find_all('a')
    with open(output_file, 'w') as file:
        for link in links:
            file.write(link['href'] + "\n")

