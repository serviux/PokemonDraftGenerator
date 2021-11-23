"""The purpose of this script is to get a list of legendary, mythical, and sub-legendary pokemon from serebii"""

from bs4 import BeautifulSoup
import requests

SEREBII_URL = "https://www.serebii.net/pokemon/legendary.shtml"


def get_page(url):
        resp = requests.get(url)
        page = resp.content
        soup = BeautifulSoup(page, "html.parser")
        return soup

def get_legendaries(page):
        names = []
        tables = page.find_all("table", class_="trainer")
        legendary_table = tables[1] #the second table on the page is the legendary table
        pokemon = legendary_table.find_all("table")
        for table in pokemon:
                ts = table.find_all("td")
                table_data2 = ts[1]
                name = table_data2.text
                names.append(name)

        return names
                
def get_mythicals(page):
        names = []
        tables = page.find_all("table", class_="trainer")
        legendary_table = tables[2] #the second table on the page is the legendary table
        pokemon = legendary_table.find_all("table")
        for table in pokemon:
                ts = table.find_all("td")
                table_data2 = ts[1]
                name = table_data2.text
                names.append(name)

        return names

def get_sub_legendaries(page):
        names = []
        tables = page.find_all("table", class_="trainer")
        legendary_table = tables[0] #the first table on the page is the sub-legendary and ultra beast table
        pokemon = legendary_table.find_all("table")
        for table in pokemon:
                ts = table.find_all("td")
                table_data2 = ts[1]
                ability_td = ts[3]
                ability = ability_td.text.strip()
                if ability != "Beast Boost":
                        name = table_data2.text
                        names.append(name)

        return names



def get_ultra_beasts(page):
        names = []
        tables = page.find_all("table", class_="trainer")
        legendary_table = tables[0] #the first table on the page is the sub-legendary and ultra beast table
        pokemon = legendary_table.find_all("table")
        for table in pokemon:
                ts = table.find_all("td")
                table_data2 = ts[1]
                ability_td = ts[3]
                ability = ability_td.text.strip()
                if ability == "Beast Boost":
                        name = table_data2.text
                        names.append(name)

        return names


def main():
        soup = get_page(SEREBII_URL)
        legendaries = get_legendaries(soup)
        mythicals = get_mythicals(soup)
        sub_legendaries = get_sub_legendaries(soup)
        ultra_beasts = get_ultra_beasts(soup)
        print("done")

if __name__ == "__main__":
        main()