#importing libraries
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Opening th eurl
page = urlopen('https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches')

#Parsing the extracted page using BeautifulSoup
soup = BeautifulSoup(page, 'lxml')
dabba = soup.find_all('div', class_="_3liAhj _2Vsm67")
items = []
for i in range(dabba.__len__()):
    each = list()
    each.append(dabba[i].find('a', class_="_2cLu-l").text)
    each.append(dabba[i].find('div', class_="_1vC4OE").text)
    if dabba[i].find('div', class_="VGWI6T"):
        each.append(dabba[i].find('div', class_="VGWI6T").text)
    else:
        each.append("NAN")
    items.append(each)
df = pd.DataFrame(items, columns = ["Name", "Price", "Discount"])

#writing dataframe to csv
df.to_csv('watches.csv')
print(df)