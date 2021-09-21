from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")

html_text = html_page.read().decode("utf-8")
soup = BeautifulSoup(html_text, "html.parser")
soup

link_list = soup.find_all("a")

for link in link_list:
    print("{0}{1}".format(base_url, link['href']))