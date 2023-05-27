from bs4 import BeautifulSoup
import requests

url = "https://sites.google.com/view/alexandersando"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

list_element = ""

elements = soup.find_all("div", class_="hJDwNd-AhqUyc-II5mzb")  # Replace "class-name" with the actual class name you want to target
for element in elements:
    list_element.append(element)

for i in range(len(list_element)):
    while len(list_element) > 1:
         list_element.pop(0)

print(list_element)