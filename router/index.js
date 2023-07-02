// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router
const request = require("request"); // Request
const cheerio = require("cheerio"); // Cheerio

router.get("/", (req, res) => {
    res.render("index");
});

module.exports = router;