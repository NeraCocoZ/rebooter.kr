from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userRank = Blueprint("userRank", __name__, url_prefix="/api/v1/userRank")

@blue_userRank.route("/<username>")
def userRank(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        rank_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        rank_url_data_split = rank_url_data.split("?")
        rank_res = requests.get(f"https://maplestory.nexon.com{rank_url_data_split[0]}/Ranking?{rank_url_data_split[1]}")

        rank_html = rank_res.text
        rank_soup = BeautifulSoup(rank_html, "html.parser")

        rank_total = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(1) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())
        rank_world = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(2) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())
        rank_class = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(3) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())
        rank_pop = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(4) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())
        rank_union = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(5) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())
        rank_achievement = int(rank_soup.select_one("ul.n_rank_list > li:nth-child(6) > dl > dd:nth-child(3)").text.replace("위", "").replace(",", "").strip())

        result["result"] = True
        result["Rank"] = {
            "total": rank_total,
            "world": rank_world,
            "class": rank_class,
            "pop": rank_pop,
            "union": rank_union,
            "achievement": rank_achievement
        }

    except Exception as err:
        result["result"] = False
        print(err)
    
    return result