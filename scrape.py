import requests
from bs4 import BeautifulSoup

url = "http://800notes.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
content = BeautifulSoup(response.content, 'lxml')

oos_content = content.find('div', {"id": "oos_content"})
list_item = oos_content.find_all('li', {"class": "oos_listItem"})

def construct_entries():
	entries = []
	print("making entries")
	print(list_item)
	for i in range(len(list_item)):
		entry = {}
		entry['id'] = i
		entry['area'] = get_area_code(list_item[i])
		entry['number'] = get_full_number(list_item[i])
		entry['comment'] = get_comment(list_item[i])
		entries.append(entry)
	return entries

def get_full_number(entry):
	#return entry.find('a', {"class": "oos_previewTitle"}).get_text()
	return entry.find('a').get_text()

def get_area_code(entry):
	full_number = get_full_number(entry)
	return full_number[:3]

def get_comment(entry):
	comment = {}
	comment['count'] = get_comment_number(entry)
	comment['content'] = get_comment_content(entry)
	return comment

def get_comment_number(entry):
	return entry.find('span', {"class": "postCount"}).getText()

def get_comment_content(entry):
	return entry.find('div', {"class": "oos_previewBody"}).getText()
