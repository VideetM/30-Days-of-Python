import os
import sys
import datetime
import requests
import pandas as pd
from requests_html import HTML

def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None

url = 'https://www.boxofficemojo.com/year/world/2020'

html_text = url_to_txt(url)
table_data =[]
r_html = HTML(html=html_text)
table_class = '.imdb-scroll-table'
r_table = r_html.find(table_class)
parsed_table = r_table[0]
rows = parsed_table.find('tr')
header_rows = rows[0]
header_cols = header_rows.find('th')
header_names = [x.text for x in header_cols]
for row in rows[1:]:
    cols = row.find('td')
    row_data = []
    for i, col in enumerate(cols):
        header_name = header_names[i]
        row_data.append(col.text)
    table_data.append(row_data)
df = pd.DataFrame(table_data,columns=header_names)
df.to_csv('2020.csv',index=False)