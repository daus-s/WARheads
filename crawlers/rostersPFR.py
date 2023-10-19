# PPP   FFFF  RRR
# P  P  F     R  R
# PPP   FFF   RRR
# P     F     R  R
# P     F     R   R

#PRO FOOTBALL REFERENCE ROSTER WEBCRAWLER
import re                      #REGEX
import requests                #WEBREQUESTS
from bs4 import BeautifulSoup  #HTML PARSING

URL = 'https://www.pro-football-reference.com'
PFR_ABBREVIATIONS = ['buf', 'mia', 'nwe', 'nyj', 'cin', 'rav', 'pit', 'cle', 'jax', 'oti', 'clt', 'htx', 'kan', 'sdg', 'rai', 'den', 'phi', 'dal', 'nyg', 'was', 'min', 'det', 'gnb', 'chi', 'tam', 'car', 'nor', 'atl', 'sfo', 'sea', 'ram', 'crd']

def attr_2_id():
    #connect to my sql
    #query with name, DOB
    pass



def get(year, abbr):
    rost_ext = f'/teams/{abbr}/{year}_roster.htm'
    stat_ext = f'/teams/{abbr}/{year}.htm'
    #roster opertations
    roster_response = requests.get(URL+rost_ext)
    print(URL+rost_ext)
    roster_table_data = []
    roster_data = []
    if roster_response.status_code == 200:
        roster_html_content = roster_response.content.decode()
        roster_soup = BeautifulSoup(re.sub("<!--|-->","", roster_html_content), 'html.parser')
        roster_table = roster_soup.find('table', {'id':'roster'})
        if roster_table is not None:
            for row in roster_table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                roster_table_data.append(row_data)
            good = True 

            for row in roster_table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                roster_data.append(row_data)
            good = True 
    else: 
        pass
    #stat operations
    stat_response = requests.get(URL+stat_ext)
    stat_table_data = []
    stat_data = []
    if stat_response.status_code == 200:
        stat_html_content = stat_response.content.decode()
        stat_soup = BeautifulSoup(stat_html_content, 'html.parser')
        stat_table = stat_soup.find('table', {'id': 'games'})
        if stat_table is not None:
                for row in stat_table.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    stat_table_data.append(row_data)
                good = True
        for row in stat_table_data[2: stat_table_data.index(['', '', 'Playoffs', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])]:
            stat_data.append(row[5])
            record = row[7]
        stat_data.append(record)
    else: 
        pass
    print(stat_data)
    for i in roster_data:
         print(i)

def main():
    for year in range(1970, 2023):
        for team in PFR_ABBREVIATIONS:
            get(year=year, abbr=team)

if __name__ == '__main__':
    main()