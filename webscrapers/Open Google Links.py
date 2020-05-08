import pyperclip
import requests
import sys
import webbrowser
from time import sleep
from bs4 import BeautifulSoup as bs


def main():
    tabs_to_open = input("How many links do you want to open? ")
    try:
        tabs_to_open = int(tabs_to_open)
    except:
        print("Number of tabs must be an integer. Closing the program")
        sleep(3)
        sys.exit()
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        """ if no keyword is entered, the script would search for the keyword
        copied in the clipboard """
        try:
            keyword = input("What do you want to search? ")
        except:
            keyword = pyperclip.paste()
    res = requests.get('http://google.com/search?q=' + keyword)
    res.raise_for_status()
    soup = bs(res.text)
    link_elements = soup.select('.r a')
    num_open = min(tabs_to_open, len(link_elements))  # opens the first 5 results

    for i in range(num_open):
        webbrowser.open('http://google.com' + link_elements[i].get('href'))
    print("I hope one of the" + keyword + " tabs shows what you are looking for")
    sleep(3)
    sys.exit()


if __name__ == '__main__':
    main()
