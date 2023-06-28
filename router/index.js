// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router
const request = require("request"); // Request
const cheerio = require("cheerio"); // Cheerio

router.get("/", async (req, res) => {
    let username = req.query.username;
    let result = {};
	
	let url = `http://127.0.0.1:5000/api/v1/userImage/${encodeURI(username)}`

	console.log(url)
    // 사용자 이미지 요청
    request(url, function(err, res, body){
        console.log(JSON.parse(body))
    });

    res.end(username);
});

module.exports = router;