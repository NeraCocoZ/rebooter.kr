from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userStorage = Blueprint("userStorage", __name__, url_prefix="/api/v1/userStorage")

@blue_userStorage.route("/<username>")
def userStorage(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        storage_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        storage_url_data_split = storage_url_data.split("?")
        storage_res = requests.get(f"https://maplestory.nexon.com{storage_url_data_split[0]}/Storage?{storage_url_data_split[1]}")

        storage_html = storage_res.text
        storage_soup = BeautifulSoup(storage_html, "html.parser")
        
        storage_meso = int(storage_soup.select_one("div.money_txt").text.replace("창고메소 : ", "").replace(",", ""))
        
        storage_item = storage_soup.select("div.contents_wrap > div > div > div > ul > li")
        storage_item_count = len(storage_item)
        
        storage_item_list = {}
        
        for i in range(storage_item_count):
            storage_item_name = str(storage_item[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            storage_item_count = int(str(storage_item[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[2].split("<")[0].strip().replace("(", "").replace(")", "").replace("개", ""))
        
            storage_item_list[i] = {
                "name": storage_item_name,
                "count": storage_item_count
            }
        
        result["result"] = True
        result["storage"] = {
            "meso": storage_meso,
            "item": storage_item_list
        }
        
    except Exception as err:
        result["result"] = False
        print(err)
    
    return result