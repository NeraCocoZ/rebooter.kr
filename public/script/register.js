let error_element;

$(document).ready(function(){
    // 회원가입 버튼 클릭
    $("button#register_button").click(function(){
        // 입력 확인
		let input_check_result = input_check();
		if(!input_check_result) return;
    });
	
	// 모달 닫기 버튼 클릭
	$("#modal_close").click(function(){
		error_element.focus();
	})
});

function input_check(){
	// 변수
	let result = true;
	let register_id = $("input#register_id");
	let register_pw = $("input#register_pw");
	let register_pw_check = $("input#register_pw_check");
	let register_email = $("input#register_email");
	
	// 아이디 입력 확인
	if(register_id.val() == ""){
		error_modal_show("회원가입 실패", "아이디를 입력해주세요.");
		error_element = register_id;
		result = false;
	}
	// 비밀번호 입력 확인
	else if(register_pw.val() == ""){
		error_modal_show("회원가입 실패", "비밀번호를 입력해주세요.");
		error_element = register_pw;
		result = false;
	}
	// 비밀번호 재 입력 확인
	else if(register_pw_check.val() == ""){
		error_modal_show("회원가입 실패", "비밀번호를 다시 입력해주세요.");
		error_element = register_pw_check;
		result = false;
	}
	// 이메일 입력 확인
	else if(register_email.val() == ""){
		error_modal_show("회원가입 실패", "이메일을 입력해주세요.");
		error_element = register_email;
		result = false;
	}
	
	// 비밀번호 일치 확인
	else if(register_pw.val() != register_pw_check.val()){
		error_modal_show("회원가입 실패", "비밀번호가 일치하지 않습니다.");
		error_element = register_pw_check;
		result = false;
	}
	
	// 아이디 8자리 확인
	else if(register_id.val().length < 8){
		error_modal_show("회원가입 실패", "사용할 수 없는 아이디 입니다.");
		error_element = register_id;
		result = false;
	}
	// 아이디 16자리 확인
	else if(register_id.val().length > 16){
		error_modal_show("회원가입 실패", "사용할 수 없는 아이디 입니다.");
		error_element = register_id;
		result = false;
	}
	// 비밀번호 8자리 확인
	else if(register_pw.val().length < 8){
		error_modal_show("회원가입 실패", "사용할 수 없는 비밀번호 입니다.");
		error_element = register_pw;
		result = false;
	}
}