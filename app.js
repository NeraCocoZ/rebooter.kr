// 모듈 선언
const express = require("express");
const path = require("path");

// 변수 선언
let port = 8080;

// 서버 생성
let app = express();

// 서버 설정
app.set("views", path.join(__dirname, "/views")); // view 폴더
app.set("view engine", "ejs"); // EJS 사용
app.use(express.static("public")); // Public 정적 폴더

// 라우터
let api_v1 = require("./router/api_v1");

app.use("/api/v1", api_v1);

app.get("/", function(req, res){
    res.redirect("/api/v1/userImage/학살자문별이")
})

// 서버 실행
app.listen(port, () => {console.log("[ Rebooter.kr ] 서버가 실행되었습니다.")});