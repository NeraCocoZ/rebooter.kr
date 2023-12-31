from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userInfo = Blueprint("userInfo", __name__, url_prefix="/api/v1/userInfo")

@blue_userInfo.route("/<username>")
def userInfo(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        info_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        info_res = requests.get(f"https://maplestory.nexon.com{info_url_data}")

        info_html = info_res.text
        info_soup = BeautifulSoup(info_html, "html.parser")

        info_username = info_soup.select_one("div.char_name > span").text.replace("님", "")
        info_level = info_soup.select_one("div.char_info > dl:nth-child(1) > dd").text
        info_class = info_soup.select_one("div.char_info > dl:nth-child(2) > dd").text
        
        info_server_icon = info_soup.select_one("div.char_info > dl:nth-child(3) > dd > img").get("src")
        info_server_name = info_soup.select_one("div.char_info > dl:nth-child(3) > dd").text
        
        info_exp = int(info_soup.select_one("div.level_data > span:nth-child(1)").text.replace("경험치", "").replace(",", ""))
        info_pop = int(info_soup.select_one("span.pop_data").text.replace("인기도", "").replace(",", ""))
        
        info_meso = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(2) > span").text.replace(",", ""))
        info_maplepoint = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(4) > span").text.replace(",", ""))
        
        info_stat_damage = info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2) > span").text
        info_stat_damage_min = int(info_stat_damage.split("~")[0].replace(",", "").strip())
        info_stat_damage_max = int(info_stat_damage.split("~")[1].replace(",", "").strip())
        
        info_stat_hp = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text.replace(",", ""))
        info_stat_mp = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > span").text.replace(",", ""))
        
        info_stat_str = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4) > span").text.replace(",", ""))
        info_stat_dex = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(2) > span").text.replace(",", ""))
        info_stat_int = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(4) > span").text.replace(",", ""))
        info_stat_luk = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(2) > span").text.replace(",", ""))
        
        info_stat_crit_damage = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(4) > span").text.replace("%", ""))
        
        info_stat_boss_damage = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(2) > span").text.replace("%", ""))
        info_stat_ignore_def = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(4) > span").text.replace("%", ""))
        
        info_stat_status_res = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(6) > td:nth-child(2) > span").text)
        info_stat_knockback_res = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(6) > td:nth-child(4) > span").text.replace("%", ""))
        
        info_stat_def = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(7) > td:nth-child(2) > span").text.replace(",", ""))
        info_stat_speed = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(7) > td:nth-child(4) > span").text.replace("%", ""))
        info_stat_jump = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(8) > td:nth-child(2) > span").text.replace("%", ""))
        
        info_stat_star_force = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(8) > td:nth-child(4) > span").text)
        info_stat_arcane_force = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(9) > td:nth-child(4) > span").text.replace(",", ""))
        
        info_stat_honor = int(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(9) > td:nth-child(2) > span").text.replace(",", ""))
        
        info_stat_ablity = info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(10) > th > span").text
        info_stat_ablity_count = info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(10) > td").get("colspan")
        
        info_stat_ablity_option = str(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(10) > td > span")).replace("<span>", "").replace("</span>", "").split("<br/>")
        info_stat_ablity_option.pop()
        
        info_stat_hyper_stat = str(info_soup.select_one("div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(11) > td > span")).replace("<span>", "").replace("</span>", "").split("<br/>")
        info_stat_hyper_stat.pop()
        
        info_traits_ambition_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(1) > div > h2").text
        info_traits_ambition_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(1) > div > div.graph_wrap > div > span").text)
        info_traits_ambition_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(1) > div > div.graph_wrap > span > em").text)
        info_traits_ambition_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(1) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_ambition_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(1) > div > div.today_point_count > em").text)
        info_traits_ambition_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[0]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_traits_insight_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(2) > div > h2").text
        info_traits_insight_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(2) > div > div.graph_wrap > div > span").text)
        info_traits_insight_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(2) > div > div.graph_wrap > span > em").text)
        info_traits_insight_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(2) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_insight_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(2) > div > div.today_point_count > em").text)
        info_traits_insight_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[1]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_traits_willpower_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(3) > div > h2").text
        info_traits_willpower_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(3) > div > div.graph_wrap > div > span").text)
        info_traits_willpower_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(3) > div > div.graph_wrap > span > em").text)
        info_traits_willpower_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(3) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_willpower_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(3) > div > div.today_point_count > em").text)
        info_traits_willpower_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[2]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_traits_dilligence_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(4) > div > h2").text
        info_traits_dilligence_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(4) > div > div.graph_wrap > div > span").text)
        info_traits_dilligence_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(4) > div > div.graph_wrap > span > em").text)
        info_traits_dilligence_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(4) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_dilligence_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(4) > div > div.today_point_count > em").text)
        info_traits_dilligence_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[3]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_traits_empathy_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(5) > div > h2").text
        info_traits_empathy_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(5) > div > div.graph_wrap > div > span").text)
        info_traits_empathy_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(5) > div > div.graph_wrap > span > em").text)
        info_traits_empathy_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(5) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_empathy_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(5) > div > div.today_point_count > em").text)
        info_traits_empathy_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[4]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_traits_charm_name = info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(6) > div > h2").text
        info_traits_charm_level = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(6) > div > div.graph_wrap > div > span").text)
        info_traits_charm_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(6) > div > div.graph_wrap > span > em").text)
        info_traits_charm_max_exp = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(6) > div > div.graph_wrap > span").text.split("/")[1])
        info_traits_charm_today = int(info_soup.select_one("div.tab02_con_wrap > div > ul > li:nth-child(6) > div > div.today_point_count > em").text)
        info_traits_charm_option = str(info_soup.select("div.total_effect_wrap:nth-child(1) > ul")[5]).replace("<ul>", "").replace("</ul>", "").replace("<li>", "").replace("</li>", "").strip().split("\n")
        
        info_etc_marry = info_soup.select_one("div.tab03_con_wrap > table:nth-child(2) > tbody > tr > td > span").text
        
        info_etc_monster_village_name = info_soup.select_one("div.tab03_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(2) > span").text
        info_etc_monster_village_level = int(info_soup.select_one("div.tab03_con_wrap > table:nth-child(4) > tbody > tr:nth-child(1) > td:nth-child(4) > span").text)
        info_etc_monster_village_waru = int(info_soup.select_one("div.tab03_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(2) > span").text.replace(",", ""))
        info_etc_monster_village_clover = int(info_soup.select_one("div.tab03_con_wrap > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4) > span").text.replace(",", ""))
        info_etc_monster_village_gem = int(info_soup.select_one("div.tab03_con_wrap > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(2) > span").text.replace(",", ""))
        
        result["result"] = True
        result["info"] = {
            "username": info_username,
            "level": info_level,
            "class": info_class,
            "server": {
                "name": info_server_name,
                "icon": info_server_icon
            },
            "exp": info_exp,
            "pop": info_pop,
            "meso": info_meso,
            "maplepoint": info_maplepoint,
            "stat": {
                "damage_min": info_stat_damage_min,
                "damage_max": info_stat_damage_max,
                "hp": info_stat_hp,
                "mp": info_stat_mp,
                "str": info_stat_str,
                "dex": info_stat_dex,
                "int": info_stat_int,
                "luk": info_stat_luk,
                "crit_damage": info_stat_crit_damage,
                "boss_damage": info_stat_boss_damage,
                "ignore_def": info_stat_ignore_def,
                "status_res": info_stat_status_res,
                "knockback_res": info_stat_knockback_res,
                "def": info_stat_def,
                "speed": info_stat_speed,
                "jump": info_stat_jump,
                "star_force": info_stat_star_force,
                "arcane_force": info_stat_arcane_force,
                "honor": info_stat_honor,
                "ablity": {
                    "grade": info_stat_ablity,
                    "count": info_stat_ablity_count,
                    "option": info_stat_ablity_option
                },
                "hyper_stat": info_stat_hyper_stat
            },
            "traits": {
                "ambition": {
                    "name": info_traits_ambition_name,
                    "level": info_traits_ambition_level,
                    "exp": info_traits_ambition_exp,
                    "max_exp": info_traits_ambition_max_exp,
                    "today": info_traits_ambition_today,
                    "option": info_traits_ambition_option
                },
                "insight": {
                    "name": info_traits_insight_name,
                    "level": info_traits_insight_level,
                    "exp": info_traits_insight_exp,
                    "max_exp": info_traits_insight_max_exp,
                    "today": info_traits_insight_today,
                    "option": info_traits_insight_option
                },
                "willpower": {
                    "name": info_traits_willpower_name,
                    "level": info_traits_willpower_level,
                    "exp": info_traits_willpower_exp,
                    "max_exp": info_traits_willpower_max_exp,
                    "today": info_traits_willpower_today,
                    "option": info_traits_willpower_option
                },
                "dilligence": {
                    "name": info_traits_dilligence_name,
                    "level": info_traits_dilligence_level,
                    "exp": info_traits_dilligence_exp,
                    "max_exp": info_traits_dilligence_max_exp,
                    "today": info_traits_dilligence_today,
                    "option": info_traits_dilligence_option
                },
                "empathy": {
                    "name": info_traits_empathy_name,
                    "level": info_traits_empathy_level,
                    "exp": info_traits_empathy_exp,
                    "max_exp": info_traits_empathy_max_exp,
                    "today": info_traits_empathy_today,
                    "option": info_traits_empathy_option
                },
                "charm": {
                    "name": info_traits_charm_name,
                    "level": info_traits_charm_level,
                    "exp": info_traits_charm_exp,
                    "max_exp": info_traits_charm_max_exp,
                    "today": info_traits_charm_today,
                    "option": info_traits_charm_option
                }
            },
            "etc": {
                "marry": info_etc_marry,
                "monster_village": {
                    "name": info_etc_monster_village_name,
                    "level": info_etc_monster_village_level,
                    "waru": info_etc_monster_village_waru,
                    "clover": info_etc_monster_village_clover,
                    "gem": info_etc_monster_village_gem
                }
            }
        }

    except Exception as err:
        result["result"] = False
        result["message"] = err
        print(err)

    return result