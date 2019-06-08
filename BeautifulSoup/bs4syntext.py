from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')


# Direct
# print(soup.body) # gives body
# print(soup.head) # gives head
# print(soup.head.title) # gives title

# find()
# el = soup.find('div')

# find_all() or findAll()
# el = soup.findAll('div')

# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello": "hi"})

# select
# el = soup.select('#selection-1')

# get_text()
# el = soup.select('.item')[0].get_text()

# Navigation
# el = soup.body.contents[1].contents[1].find_next_sibling()
# el = soup.find(id='section-2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()
el = soup.find('h3').find_next_sibling('p')

print(el)