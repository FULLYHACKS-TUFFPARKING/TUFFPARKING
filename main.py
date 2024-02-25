import bs4
import httpx

from bs4 import BeautifulSoup

def Scrape():
    html = httpx.get("https://parking.fullerton.edu/parkinglotcounts/mobile.aspx").text
    soup = BeautifulSoup(html)
    #print(soup.prettify())
    table = soup.find("table")
    rows = table.find_all("tr")
    areas = {}
    for i in range(1, len(rows)):
        row = rows[i]
        #print(row)
        cols = row.find_all("td")
        #left_cols = cols[0].find_all("p")
        right_cols = cols[1]
        availability = right_cols.find_all('span')[0].text
        print(availability)
        #name = row.css.select("LocationName").text
        #print(left_cols)
        #print(right_cols)
        # areas[name] = {
        #     "available_spaces": int(row.find().text)
        # }
       # print(row)
    return areas
print(Scrape())

