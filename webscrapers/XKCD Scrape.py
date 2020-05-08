from time import sleep
import os
import requests
import urllib.request
from lxml import html


def main():
    try:
        page = requests.get("https://www.xkcd.com")
        page = html.fromstring(page.content)
        image_src = "https:" + str(page.xpath(".//*[@id='comic']/img/@src")[0])
    except requests.exceptions.RequestException as e:
        print("Can't reach the xkcd site")
        sleep(3)
        exit()

    # Parses xkcd page
    # Scrape the comic name from the image url
    comic_name = image_src.split('/')[-1]
    comic_location = os.getcwd() + '/XKCD Comics/'

    # Checks if comic folder exists else creates it
    if not os.path.exists(comic_location):
        os.makedirs(comic_location)

    # Creates the final comic location and downloads the comic
    comic_location = comic_location + comic_name
    urllib.request.urlretrieve(image_src, comic_location)

    print("The file: " + comic_name + " has been downloaded")
    sleep(3)


if __name__ == "__main__":
    main()
