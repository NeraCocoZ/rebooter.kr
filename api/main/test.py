from flask import Blueprint
import requests
from bs4 import BeautifulSoup

blue_test = Blueprint("test", __name__, url_prefix="/api/v1/test")

@blue_test.route("/<username>")
def test(username):
    result = {}

    try:
        url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={username}&w=254"
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