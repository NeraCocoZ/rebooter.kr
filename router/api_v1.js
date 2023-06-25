// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router
const request = require("request"); // Request
const cheerio = require("cheerio"); // Cheerio

router.get("/userImage/:username", async (req, res) => {
    let username = req.params.username;
    let result = {};

    // 사용자 이미지 요청
    request(`https://maplestory.nexon.com/N23Ranking/World/Total?c=${username}&w=254`, function(err, res, body){
        console.log(body)
    });

    res.end(username);
});

module.exports = router;