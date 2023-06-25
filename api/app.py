# 모듈 선언
from flask import Flask
import requests
from bs4 import BeautifulSoup
from urllib import parse


# 변수 생성
version = "v1"

# 서버 선언
app = Flask(__name__)

# GET /api/v1/userImage
@app.route(f"/api/{version}/userImage/<username>", methods=["GET"])
def userImage(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={parse.quote(username)}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        image = soup.select_one("tr.search_com_chk > td.left > span > img:nth-child(1)").get("src")

        result["result"] = True
        result["image"] = image

    except Exception as err:
        result["result"] = False
        result["image"] = "https://ssl.nexon.com/s2/game/maplestory/renewal/common/no_char_img_180.png"
        print(err)

    return result

# GET /api/v1/userRank
@app.route(f"/api/{version}/userRank/<username>", methods=["GET"])
def userRank(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={parse.quote(username)}&w=254"
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

# GET /api/v1/userInfo
@app.route(f"/api/{version}/userInfo/<username>", methods=["GET"])
def userInfo(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={parse.quote(username)}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        info_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        info_res = requests.get(f"https://maplestory.nexon.com{info_url_data}")

        info_html = info_res.text
        info_soup = BeautifulSoup(info_html, "html.parser")

        info_class = info_soup.select_one("div.char_info > dl:nth-child(2) > dd").text

        print(info_class)

        result["result"] = True

    except Exception as err:
        result["result"] = False
        print(err)

    return result

# GET /api/v1/test
@app.route(f"/api/{version}/test/<username>", methods=["GET"])
def test(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={parse.quote(username)}&w=254"
        res = requests.get(url)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        test_url_data = soup.select_one("tr.search_com_chk > td.left > dl > dt > a").get("href")
        test_url_data_split = test_url_data.split("?")
        test_res = requests.get(f"https://maplestory.nexon.com{test_url_data_split[0]}/?{test_url_data_split[1]}")

        test_html = test_res.text

        result["html"] = test_html

    except Exception as err:
        print(err)

    return result["html"]