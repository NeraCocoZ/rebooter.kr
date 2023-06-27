from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userInventory = Blueprint("userInventory", __name__, url_prefix="/api/v1/userInventory")

@blue_userInventory.route("/<username>")
def userInventory(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        inventory_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        inventory_url_data_split = inventory_url_data.split("?")
        inventory_res = requests.get(f"https://maplestory.nexon.com{inventory_url_data_split[0]}/Inventory?{inventory_url_data_split[1]}")

        inventory_html = inventory_res.text
        inventory_soup = BeautifulSoup(inventory_html, "html.parser")
        
        inventory_equipment = inventory_soup.select("div.tab01_con_wrap > div > ul > li")
        inventory_equipment_count = len(inventory_equipment)
        
        inventory_equipment_list = {}
        
        for i in range(inventory_equipment_count):
            inventory_equipment_name = str(inventory_equipment[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            inventory_equipment_upgrade = str(inventory_equipment[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[2].split("<")[0].strip().replace("성 강화", "")
            inventory_equipment_image_url = inventory_equipment[i].select_one("div.inven_item_img > a > img").get("src")
            
            if inventory_equipment_upgrade == "":
                inventory_equipment_upgrade = 0
                
            inventory_equipment_upgrade = int(inventory_equipment_upgrade)
            
            inventory_equipment_list[i] = {
                "name": inventory_equipment_name,
                "upgrade": inventory_equipment_upgrade,
                "image_url": inventory_equipment_image_url
            }
            
        inventory_use = inventory_soup.select("div.tab02_con_wrap > div > ul > li")
        inventory_use_count = len(inventory_use)
        
        inventory_use_list = {}
        
        for i in range(inventory_use_count):
            inventory_use_name = str(inventory_use[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            inventory_use_item_count =int(str(inventory_use[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[2].split("<")[0].strip().replace("(", "").replace(")", "").replace("개", "")) 
            inventory_use_image_url = inventory_use[i].select_one("div.inven_item_img > a > img").get("src")
            
            inventory_use_list[i] = {
                "name": inventory_use_name,
                "count": inventory_use_item_count,
                "image_url": inventory_use_image_url
            }
            
        inventory_etc = inventory_soup.select("div.tab03_con_wrap > div > ul > li")
        inventory_etc_count = len(inventory_etc)
        
        inventory_etc_list = {}
        
        for i in range(inventory_etc_count):
            inventory_etc_name = str(inventory_etc[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            inventory_etc_item_count = int(str(inventory_etc[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[2].split("<")[0].strip().replace("(", "").replace(")", "").replace("개", ""))
            inventory_etc_image_url = inventory_etc[i].select_one("div.inven_item_img > a > img").get("src")
            
            inventory_etc_list[i] = {
                "name": inventory_etc_name,
                "count": inventory_etc_item_count,
                "image_url": inventory_etc_image_url
            }
            
        inventory_setup = inventory_soup.select("div.tab04_con_wrap > div > ul > li")
        inventory_setup_count = len(inventory_setup)
        
        inventory_setup_list = {}
        
        for i in range(inventory_setup_count):
            inventory_setup_name = str(inventory_setup[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            inventory_setup_item_count = int(str(inventory_setup[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[2].split("<")[0].strip().replace("(", "").replace(")", "").replace("개", ""))
            inventory_setup_image_url = inventory_setup[i].select_one("div.inven_item_img > a > img").get("src")
            
            inventory_setup_list[i] = {
                "name": inventory_setup_name,
                "count": inventory_setup_item_count,
                "image_url": inventory_setup_image_url
            }
            
        inventory_cash = inventory_soup.select("div.tab05_con_wrap > div > ul > li")
        inventory_cash_count = len(inventory_cash)
        
        inventory_cash_list = {}
        
        for i in range(inventory_cash_count):
            inventory_cash_name = str(inventory_cash[i].select_one("div.inven_item_memo > div.inven_item_memo_title > h1 > a")).split(">")[1].split("<")[0].strip()
            inventory_cash_image_url = inventory_cash[i].select_one("div.inven_item_img > a > img").get("src")
            
            inventory_cash_list[i] = {
                "name": inventory_cash_name,
                "image_url": inventory_cash_image_url
            }
            
            
        result["result"] = True
        result["inventory"] = {
            "equip": inventory_equipment_list,
            "use": inventory_use_list,
            "etc": inventory_etc_list,
            "setup": inventory_setup_list,
            "cash": inventory_cash_list
        }
        
    except Exception as err:
        result["result"] = False
        print(err)
        
    return result