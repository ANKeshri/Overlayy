import requests
from bs4 import BeautifulSoup
import json

# Taking the URL as input from the user
url = input("Enter the URL of the website: ")

# Sending a GET request to the specified URL
r = requests.get(url)
htmlContent = r.content

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(htmlContent, 'html.parser')

# Prettifying the soup object (optional)
#print(soup.prettify())

# Finding all anchor tags
anchors = soup.find_all('a')
all_links = set()

# Extracting and printing all links
for link in anchors:
    href = link.get('href')
    if href and href != '#':
        # If the link is relative, convert it to an absolute URL
        if not href.startswith('http'):
            href = url.rstrip('/') + '/' + href.lstrip('/')
        all_links.add(href)
        print(href)
links_list=list(all_links)
with open('scrapped_links.json','w')as file:
    json.dump(links_list,file,indent=4)
print(f"All links have been saved to 'scraped_links.json'")


# Load the links from the JSON file
with open('scrapped_links.json', 'r') as file:
    links_list = json.load(file)

# Print the links
for link in links_list:
    print(link)