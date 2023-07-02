// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router
const request = require("request"); // Request
const cheerio = require("cheerio"); // Cheerio

router.get("/", (req, res) => {
    // 유저 이름
    let username = req.query.username;

    if(username == undefined)
        res.redirect("/");
	
	res.end(username)
});

module.exports = router;