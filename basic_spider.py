import requests
from bs4 import BeautifulSoup
def main_spider(url):
    urls = []
    request = requests.get(url)
    web_text = request.text
    soup = BeautifulSoup(str(web_text))
    for card in soup.find_all("a",{"class" : "dropdown-item"}):
        x = card.get("href")
        urls.append(url + x)
        return urls
def each_spider(*urls):
    for each_link in urls:
        request = requests.get(each_link)
        link_text = request.text
        soup = BeautifulSoup(str(link_text))
        for image_address in soup.find_all("img",{"class" : "img-fluid"}):
            each_link = each_link.replace("products.html#shirts","")
            print(each_link+image_address.get("src"))
def runner():
    values = main_spider("https://a1-uniforms.netlify.app/")
    each_spider(*values)
runner()
