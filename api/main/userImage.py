from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_userImage = Blueprint("userImage", __name__, url_prefix="/api/v1/userImage")

@blue_userImage.route("/<username>")
def userImage(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
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