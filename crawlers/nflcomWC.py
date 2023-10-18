# N   N  FFFFF  L
# NN  N  F      L
# N N N  FFF    L
# N  NN  F      L
# N   N  F      LLLLLL 
# 
# WEB CRAWLER
import requests
from bs4 import BeautifulSoup

#URL
URL = 'https://www.nfl.com'

# STAT NAMES
STATS = ['PASSING', 'RUSHING', 'RECIIEVING', 'FUMBLES', 'TACKLES', 'INTERCEPTIONS', 'FIELD_GOALS', 'KICK_OFFS', 'KICK_OFF_RETURNS', 'PUNTING', 'PUNT_RETURNS']

def get(url): 
    table_data = []
    i = 0
    good = False
    response = requests.get(url)
    while True:
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find('table')

            if table is not None:
                for row in table.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    table_data.append(row_data)
                good = True

            #get next page
            next_page_link = soup.find('a', {'class': 'nfl-o-table-pagination__next'})
            if next_page_link is None:
                #end of data
                break
            else: 
                i += 1
                href = next_page_link['href']
                response = requests.get(URL + href)
                print(f'completed page {i}\t\tURL: {URL}{href}')
        else:
            good = False
            print(f'Failed to fetch content. Status code: {response.status_code}')
            return


    # after all pages...
    if good:
        i = 0
        new_table_data = [row for row in table_data if row[0] != 'Player']

        for row in new_table_data:
            print(row)


def generate_url(year, stat):
    #SPECIFIERS
    stat_urls = {
        'PASSING' : '/stats/player-stats/category/passing/{}/reg/all/passingyards/desc',
        'RUSHING' : '/stats/player-stats/category/rushing/{}/reg/all/rushingyards/desc',
        'RECIEVING' : '/stats/player-stats/category/receiving/{}/reg/all/receivingreceptions/desc',
        'FUMBLES' : '/stats/player-stats/category/fumbles/{}/reg/all/defensiveforcedfumble/desc',
        'TACKLES' : '/stats/player-stats/category/tackles/{}/reg/all/defensivecombinetackles/desc',
        'INTERCEPTIONS' : '/stats/player-stats/category/interceptions/{}/reg/all/defensiveinterceptions/desc',
        'FIELD_GOALS' : '/stats/player-stats/category/field-goals/{}/reg/all/kickingfgmade/desc',
        'KICK_OFFS' : '/stats/player-stats/category/kickoffs/{}/reg/all/kickofftotal/desc',
        'KICK_OFF_RETURNS' : '/stats/player-stats/category/kickoff-returns/{}/reg/all/kickreturnsaverageyards/desc',
        'PUNTING' : '/stats/player-stats/category/punts/{}/reg/all/puntingaverageyards/desc',
        'PUNT_RETURNS' : '/stats/player-stats/category/punt-returns/{}/reg/all/puntreturnsaverageyards/desc',
    }
    url = URL + stat_urls[stat].format(year)
    return url

def main():
    for stat in STATS:
        for year in range(1970,2023, 1): #UPDATE YEARLY: EXCLUSIVE TOP BOUND GO TO FOLLOWING YEAR
            get(generate_url(year, stat))


if __name__=='__main__':
    main()

    