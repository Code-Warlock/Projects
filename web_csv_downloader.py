""" CSV Crawler """
from urllib.request import urlopen
import string
import csv
import random
def url_name():
    """DOCSTRINGS : Random Name generator for crawled csv documents.
       PARAMETERS : None
       INPUT : None
       OUTPUT : None
       RETURN VALUE : A string of three lettered csv filename
    """
    letters = string.ascii_lowercase + string.ascii_uppercase
    random_no = random.randint(1,52)
    name = ""
    while len(name) < 4:
        name += letters[random_no]
        random_no = random.randint(1,52)
    return name + ".csv"
def crawl(url):
    """ Crawl CSV function """
    with urlopen(url) as response:
        data = response.read()
    main_data = []
    string_repr = str(data)
    rows = string_repr.split("\\n")
    for x in rows:
        cell = x.split(";")
        main_data.append(cell)
    destination_url = url_name()
    with open(destination_url,"a") as create_file:
        for line in main_data:
            create_file.write(line)
crawl("https://support.staffbase.com/hc/en-us/article_attachments/360009197011/username-password-recovery-code.csv")
# with open("Yeas.csv") as f:
#     x = enumerate(csv.reader(f))
#     for i,j in x:
#         print(i,j)
