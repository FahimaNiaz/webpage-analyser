import requests
from bs4 import BeautifulSoup

def get_html_content(url):
	html= requests.get(url)
	return html.content
	
#	paras= soup.findAll('t')
#	for t in paras:
#		return t.text

def parse_html_using_tag(html_content, tag):
	soup=BeautifulSoup(html_content,'html.parser')
	data=[para.text for para in soup.find_all(tag)]
	return data