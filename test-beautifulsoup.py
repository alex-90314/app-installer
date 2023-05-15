import requests
from bs4 import BeautifulSoup
# Initialize the beautifulsoup object
page = requests.get("http://somewebpage.com....").text
soup = BeautifulSoup(page, 'html.parser')
soup_alt = BeautifulSoup(page.text, 'html.parser')

# Access a tag
tag_obj = soup.title # The first title tag

# Child Tag inside that tag
child_tag  = tag_obj.div # The first div tag inside title

# Access the parent tag 
parent_tag = child_tag.parent # the title tag

# Access the sibling tag 
sibling_tag = child_tag.next_sibling # the sibling tag next to the child tag 

# Access the child tag attributes
child_tag_att = child_tag.attrs # the title tag attributes as dictionary

# Access the contents of child tag
child_contents = child_tag.string # var.tag_name.string

# Filter for specific items
table_rows = soup.find_all(name='tr') # Produce list of <tr> tags