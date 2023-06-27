from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userEquipment = Blueprint("userEquipment", __name__, url_prefix="/api/v1/userEquipment")

@blue_userEquipment.route("/<username>")
def userEquipment(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        equipment_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        equipment_url_data_split = equipment_url_data.split("?")
        equipment_res = requests.get(f"https://maplestory.nexon.com{equipment_url_data_split[0]}/Equipment?{equipment_url_data_split[1]}")

        equipment_html = equipment_res.text
        equipment_soup = BeautifulSoup(equipment_html, "html.parser")
        
        equipment_item_name_list = ["cap", "fore_head", "eyeacc", "clothes", "pants", "gloves", "cape", "shoes", "sub_weapon", "weapon", "ring1", "ring2", "ring3", "ring4", "pendant1", "pendant2", "earacc", "belt", "shoulder", "emblem", "pocket", "badge", "medal", "android", "heart"]
        equipment_item_num_list = [3, 8, 13, 18, 23, 24, 25, 28, 20, 17, 1, 6, 11, 16, 7, 12, 14, 22, 19, 5, 21, 10, 15, 29, 30]
        
        equipment_cash_name_list = ["cap", "fore_head", "eyeacc", "clothes", "pants", "gloves", "cape", "shoes", "sub_weapon", "weapon", "ring1", "ring2", "ring3", "ring4", "earacc", "hair", "face"]
        equipment_cash_num_list = [3, 8, 13, 18, 23, 24, 25, 28, 20, 17, 1, 6, 11, 16, 14, 5, 10]
        
        equipment_arcane_name_list = ["vanishing_journey", "chuchu_island", "lachelein", "arcana", "morass", "esfera"]
        equipment_arcane_num_list = [1, 2, 3, 4, 5, 6]
        
        equipment_item = {}
        equipment_cash = {}
        equipment_arcane = {}
        
        for i in range(len(equipment_item_name_list)):
            equipment_item_name = equipment_soup.select_one(f"div.weapon_wrap > ul > li:nth-child({equipment_item_num_list[i]}) > img").get("alt")
            equipment_item_image_url = equipment_soup.select_one(f"div.weapon_wrap > ul > li:nth-child({equipment_item_num_list[i]}) > img").get("src")
            
            equipment_item[equipment_item_name_list[i]] = {
                "name": equipment_item_name,
                "image_url": equipment_item_image_url
            }
            
        for i in range(len(equipment_cash_name_list)):
            equipment_cash_name = equipment_soup.select_one(f"div.cash_weapon_wrap > ul > li:nth-child({equipment_cash_num_list[i]}) > img").get("alt")
            equipment_cash_image_url = equipment_soup.select_one(f"div.cash_weapon_wrap > ul > li:nth-child({equipment_cash_num_list[i]}) > img").get("src")
            
            equipment_cash[equipment_cash_name_list[i]] = {
                "name": equipment_cash_name,
                "image_url": equipment_cash_image_url
            }
            
        for i in range(len(equipment_arcane_name_list)):
            equipment_arcane_name = equipment_soup.select_one(f" div.arcane_weapon_wrap > ul > li:nth-child({equipment_arcane_num_list[i]}) > img").get("alt")
            equipment_arcane_image_url = equipment_soup.select_one(f" div.arcane_weapon_wrap > ul > li:nth-child({equipment_arcane_num_list[i]}) > img").get("src")
            
            equipment_arcane[equipment_arcane_name_list[i]] = {
                "name": equipment_arcane_name,
                "image_url": equipment_arcane_image_url
            }

        result["result"] = True
        result["equipment"] = {
            "equipment": equipment_item,
            "cash_equipmant": equipment_cash,
            "arcane_equipment": equipment_arcane
        }

    except Exception as err:
        result["result"] = False
        print(err)
    
    return result