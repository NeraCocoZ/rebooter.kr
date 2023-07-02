// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router

router.get("/", (req, res) => {
	res.render("register")
});

module.exports = router;