from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userGuild = Blueprint("userGuild", __name__, url_prefix="/api/v1/userGuild")

@blue_userGuild.route("/<username>")
def userGuild(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        guild_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        guild_url_data_split = guild_url_data.split("?")
        guild_res = requests.get(f"https://maplestory.nexon.com{guild_url_data_split[0]}/Guild?{guild_url_data_split[1]}")

        guild_html = guild_res.text
        guild_soup = BeautifulSoup(guild_html, "html.parser")
        
        guild_icon = guild_soup.select_one("div.tab01_con_wrap > h1:nth-child(1) > span > img").get("src")
        guild_name = guild_soup.select_one("div.tab01_con_wrap > h1:nth-child(1)").text
        
        guild_level = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > span").text.replace("Lv.", ""))
        
        guild_exp = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text.split("/")[0].replace(",", "").strip())
        guild_exp_max = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text.split("/")[1].split("(")[0].replace(",", "").strip())
        guild_exp_persent = float(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text.split("/")[1].split("(")[1].replace(")", "").replace("%", "").strip())
        
        guild_master = guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2) > span").text
        guild_member_count = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(4) > span").text.replace(",", ""))
        
        guild_honor = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(2) > span").text.replace(",", ""))
        guild_gp = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(4) > span").text.replace(",", ""))
        
        guild_rank = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(4) > td:nth-child(2) > span").text.replace(",", ""))
        
        guild_my_class = guild_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2) > span").text
        guild_my_honor = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text.replace(",", ""))
        guild_my_gp = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > span").text.replace(",", ""))
        guild_my_rank = int(guild_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4) > span").text.replace(",", ""))
        
        guild_skill = guild_soup.select("div.tab02_con_wrap > div > ul > li")
        guild_skill_count = len(guild_skill)
        
        guild_skill_list = {}
        
        for i in range(guild_skill_count):
            guild_skill_icon = guild_skill[i].select_one("h2 > img").get("src")
            guild_skill_name = guild_skill[i].select_one("h2").text
            guild_skill_master_level = int(guild_skill[i].select_one("div > div > table > thead > tr > th:nth-child(1)").text.replace("마스터 레벨 : ", ""))
            guild_skill_level = int(guild_skill[i].select_one("div > div > table > thead > tr > th:nth-child(2)").text.replace("현재 레벨 : ", ""))
            
            guild_skill_info = guild_skill[i].select_one("div > div > table > tbody > tr > td:nth-child(1) > span").text.strip().replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
            guild_skill_effect = guild_skill[i].select_one("div > div > table > tbody > tr > td:nth-child(2) > span").text.strip().replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
            
            guild_skill_list[i] = {
                "icon": guild_skill_icon,
                "name": guild_skill_name,
                "master_level": guild_skill_master_level,
                "level": guild_skill_level,
                "info": guild_skill_info,
                "effect": guild_skill_effect
            }
            
            result["result"] = True
            result["guild"] = {
                "icon": guild_icon,
                "name": guild_name,
                "level": guild_level,
                "exp": guild_exp,
                "exp_max": guild_exp_max,
                "exp_persent": guild_exp_persent,
                "master": guild_master,
                "member_count": guild_member_count,
                "honor": guild_honor,
                "gp": guild_gp,
                "rank": guild_rank,
                "my": {
                    "class": guild_my_class,
                    "honor": guild_my_honor,
                    "gp": guild_my_gp,
                    "rank": guild_my_rank
                },
                "skill": guild_skill_list
                
            }
        
        
    except Exception as err:
        result["result"] = False
        print(err)
    
    return result