from bs4 import BeautifulSoup
import requests




def study_market(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    a_tags = soup.find_all('a', {'data-test': 'link-offer'})  
    for i in range(len(a_tags)):
        href = a_tags[i]['href']
        print(href)
#make a list with the href's and run a loop with the scan function over the lsit

    '''url = href

        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        print(soup.prettify)'''  #this must be with a library for java


    
study_market("https://it.pracuj.pl/praca/data%20analyst;kw/warszawa;wp?rd=30")