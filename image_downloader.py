""" Image Web Crawler with Python"""
# Module Imports
import random
import string
import time
from urllib import request as r
import requests
from bs4 import BeautifulSoup
def main_spider(url):
    urls = []
    request = requests.get(url)
    web_text = request.text
    soup = BeautifulSoup(str(web_text), "html.parser")
    for card in soup.find_all("a",{"class" : "dropdown-item"}):
        x = card.get("href")
        urls.append(url + x)
        return urls
def each_spider(*urls):
    links = []
    for each_link in urls:
        request = requests.get(each_link)
        link_text = request.text
        soup = BeautifulSoup(str(link_text))
        for image_address in soup.find_all("img",{"class" : "img-fluid"}):
            each_link = each_link.replace("products.html#shirts","")
            links.append(each_link+image_address.get("src"))
    return links
# def runner():
#     values = main_spider("https://a1-uniforms.netlify.app/")
#     each_spider(*values)
# runner()


def urls():
    """DOCSTRINGS : URL's Collector
       PARAMETERS : None
       INPUT : Any number of url from the user.
       OUTPUT : None
       RETURN VALUE : List of accepted URLS for further processing
    """
    urls_list = []
    num_of_val = input("How many urls do you want to type or you don't know : ")

    if num_of_val in "I don't not know":
        while True:
            url = input("Enter your url : ")
            urls_list.append(url)
            stopper = input("Do you want to continue : ")
            if stopper not in ("yes","y","yh","yeah"):
                break
    else:
        for _ in range(int(num_of_val)):
            url = input("Enter your url : ")
            urls_list.append(url)
    return urls_list
def url_name():
    """DOCSTRINGS : Random Name generator for crawled images.
       PARAMETERS : None
       INPUT : None
       OUTPUT : None
       RETURN VALUE : A string of three lettered jpg image filename
    """
    letters = string.ascii_lowercase + string.ascii_uppercase
    random_no = random.randint(1,52)
    name = ""
    while len(name) < 4:
        name += letters[random_no]
        random_no = random.randint(1,52)
    return name + ".jpg"
def crawler(*args):
    """DOCSTRINGS : Function utilizing the urllib module to scrape images from web pages.
       PARAMETERS : Any number of url
       INPUT : None
       OUTPUT : None
       RETURN VALUE : A list of three lettered image files
    """
    file_name = args[-1]()
    items = list()
    for each in args:
        items.append(r.urlretrieve(str(each),file_name))
    return items
def main_crawler_func(urls_func,url_name_gen_func,links,crawler_func):
    """Docstring : Remote executor for complete running of program sectors
       PARAMETERS : function(more details later)
       INPUT : None
       OUTPUT : None
       RETURN VALUE : None
    """
    try:
        vals = urls_func("https://a1-uniforms.netlify.app/")
        name_gen = url_name_gen_func
        url_name_gen_func()
        values = links(vals)
        crawler_func(*values,name_gen)
    except ValueError:
        print("Closing Program",end="")
        time.sleep(0.5)
        print(".",end="")
        time.sleep(0.5)
        print(".",end="")
        time.sleep(0.5)
        print(".",end="\n")
        time.sleep(0.4)
        print("Program Closed : No internet connection to reach address.\n" +
        "Connect to the internet and try again.")
main_crawler_func(main_spider,url_name,each_spider,crawler)
