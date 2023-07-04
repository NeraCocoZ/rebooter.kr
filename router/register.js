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
	
	// 아이디 중복 확인
	let id_overlap_check = id_overlap(username);
	
	// 아이디 중복이면
	if(id_overlap_check){
		result.result = false;
		result.resultMessage = "id_overlap";
	}
	
	// 아이디 중복이 아니면
	else{
		// 이메일 중복 확인
		let email_overlap_check = email_overlap(email)
		
		// 이메일이 중복이면
		if(email_overlap_check){
			result.result = false;
			result.resultMessage = "email_overlap";
		}
		// 이메일이 중복이 아니면
		else {
			// 유저 정보
			let userdata = {
				id: username,
				password: password,
				email: email,
				api_key: null
			}

			// 유저 정보 저장
			fs.writeFileSync(`./data/userdata/${username}.json`, JSON.stringify(userdata, null, "\t"), "utf-8");
		}
	}
	
	console.log(result)
	res.json(result);
});

// 아이디 중복 확인
function id_overlap(id){
	// 변수 선언
	let result = false;
	let id_overlap_check = fs.existsSync(`./data/userdata/${id}.json`);

	// 아이디 중복 확인
	if(id_overlap_check)
		result = true;
	
	return result;
}

// 이메일 중복 확인
function email_overlap(email){
	// 변수 선언
	let result = false;
	let email_overlap_check = JSON.parse(fs.readFileSync(`./data/email.json`).toString());

	// 이메일 중복 확인
	for(let emaildata in email_overlap_check){
		if(email_overlap_check[emaildata] == email)
			result = true;
	}

	return result;
}

module.exports = router;