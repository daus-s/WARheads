# N   N  FFFFF  L
# NN  N  F      L
# N N N  FFF    L
# N  NN  F      L
# N   N  F      LLLLLL 
# 
# WEB CRAWLER
import requests

URL = 'https://www.nfl.com/stats/player-stats/category/passing/2022/reg/all/passingyards/desc'
TABLE_START = '<table class="d3-o-table d3-o-table--detailed d3-o-player-stats--detailed d3-o-table--sortable">'
TABLE_END = '</table>'

def main():
    #run
    html = requests.get(URL)
    rawtext = html.text


if __name__=='__main__':
    main()

    