import re
import string
import io
from collections import Counter

n=5

def get_statistic(data):
	lines=get_lines(data)
	words=get_words(lines)
	unique_words=remove_stopwords(words)
	top_n_words=get_top_n_words(unique_words,n)
	statistics = {'line_count': len(lines), 'word_count': len(words), 'unique_words': len(unique_words),
                  'top_words': top_n_words}
	
	return statistics


def remove_stopwords(words):
	final_list=get_stopwords()
	unique_word= [x for x in words if x not in final_list]
	return unique_word

def get_stopwords():
	my_file = open('stopwords.txt')
	all_the_lines = my_file.readlines()
	stopwordlist = []
	final_list=[]
	for i in all_the_lines:
		stopwordlist.append(i)
		for i in stopwordlist:
			final_list.append(i.strip())	
	return final_list


def get_words(lines):
	words=[]
	for line in lines:
		words.extend(line.split())
	return words	

def get_top_n_words(unique_words, n):
	top_n_words = Counter(unique_words).most_common(n)
	top_words = []
	for x, y in top_n_words:
		top_words.append(x)
	return top_words

def get_lines(data):
	lines =[]
	for para in data:
		para_lines=re.split('[.!?]+', para)
		lines.extend(para_lines)
	cleaned_lines=clean_string(lines)
	return cleaned_lines

def clean_string(lines):
	cleaned_lines=[]
	st=str.maketrans("","", string.punctuation)
	for line in lines:
	#	st = re.sub(r'[^\w\s]', '', lines)
		new_line=line.translate(st).lower().strip()
		if new_line:
			cleaned_lines.append(new_line)
	return cleaned_lines	 


