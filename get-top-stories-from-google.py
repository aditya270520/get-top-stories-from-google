import urllib.request
import xml.etree.ElementTree

news_url = "https://news.google.com/news/rss"
with urllib.request.urlopen(news_url) as page:
    xml_page = page.read()

# Parse XML page
e = xml.etree.ElementTree.fromstring(xml_page)

# Get the item list
for it in e.iter('item'):
    print(it.find('title').text)
    print(it.find('link').text)
    print(it.find('pubDate').text, '\n')