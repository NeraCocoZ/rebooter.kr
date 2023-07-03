// 모듈 선언
const express = require("express"); // Express
const router = express.Router(); // Express Router
const fs = require("fs"); // File System

router.get("/", (req, res) => {
	res.render("register")
});

router.post("/", (req, res) => {
	// 변수
	let result = {
		result: true
	};
	let {username, password, email} = req.body;
	let userdata_path = `./data/userdata/${username}.json`;
	let emaildata_path = `./data/email.json`;
	
	// 아이디 중복 확인
	let id_overlap_check = fs.existsSync(userdata_path);
	
	// 아이디 중복이면
	if(id_overlap_check){
		result.result = false;
		result.resultMessage = "id_overlap";
	}
	
	// 아이디 중복이 아니면
	else{
		// 이메일 중복 확인
		let email_overlap_check = JSON.parse(fs.readFileSync(emaildata_path).toString());
		
		// 이메일이 중복이면
		for(let emaildata in email_overlap_check){
			if(email_overlap_check[emaildata] == email){
				result.result = false;
				result.resultMessage = "email_overlap";
			}
		}
	}
	
	return result;
})

module.exports = router;