from bz2 import _WriteBinaryMode
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver")
browser.get(start_url)
time.sleep(100)
def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitdude", "discovery_date"]
    planet_data=[]
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        litags=ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(litags):
            if index==0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")

