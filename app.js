// 모듈 선언
const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

// 변수 선언
let port = 8080;

// 서버 생성
let app = express();

// 서버 설정
app.set("views", path.join(__dirname, "/views")); // view 폴더
app.set("view engine", "ejs"); // EJS 사용
app.use(express.static("public")); // Public 정적 폴더
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));


// 라우터
let index = require("./router/index");
let register = require("./router/register");
let usersearch = require("./router/usersearch");

app.use("/", index);
app.use("/register", register);
app.use("/usersearch", usersearch);

// 서버 실행
app.listen(port, () => {console.log("[ Rebooter.kr ] 서버가 실행되었습니다.")});