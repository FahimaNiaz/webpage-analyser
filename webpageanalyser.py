import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup
from webutils import get_html_content,parse_html_using_tag
from utils1 import get_statistic

sg.theme("Purple")

layout = [
    [sg.Text("WebPage Analyzer", font=("Arial", 30))],
    [sg.Text("Enter URL", font=("Arial, 14"))],[sg.InputText( font=("Arial", 14),size=(20,1),key="url", enable_events=True)], [sg.Button("Get data", font=("Arial",14), key="get_data")],
    [sg.Multiline("", font=("Time New Roman", 14), disabled=True,size=(70, 15), key='output')]
]

def display_output(url):
	html_content= get_html_content(url)
	data= parse_html_using_tag(html_content,'p')
	statistic=get_statistic(data)
	window['output'].print('\n'.join("{}: {}".format(k, v) for k, v in statistic.items()))
	

if __name__ == '__main__':
    window = sg.Window('Web Page Analyser', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
        	break
        elif event =='get_data':
        	display_output(values['url'])
    window.Close()    	
        	

