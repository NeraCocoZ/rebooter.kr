let error_element = $("input#register_id").val();

$(document).ready(function(){
    // 회원가입 버튼 클릭
    $("button#register_button").click(function(){
		// 변수
		let username = $("input#register_id").val();
		let password = $("input#register_pw").val();
		let email = $("input#register_email").val();
		
        // 입력 확인
		let input_check_result = input_check();
		
		// 입력 오류
		if(!input_check_result) return;

		// 회원가입 요청
		sendAjax("/register", "POST", {username: username, password: password, email: email}, 
		// 요청 성공
		function(result){
			// 회원가입 성공
			if(result.result){
				error_modal_show("회원가입 성공", "회원가입에 성공했습니다.");
				error_element = "register_success";
			}
			// 회원가입 실패
			else {
				// 아이디 중복
				if(result.resultMessage == "id_overlap"){
					error_modal_show("회원가입 실패", "이미 사용중인 아이디 입니다.");
					error_element = $("input#register_id");
				}
				// 이메일 중복
				else if(result.resultMessage == "email_overlap"){
					error_modal_show("회원가입 실패", "이미 사용중인 이메일 입니다.");
					error_element = $("input#register_pw");
				}
			}
		},
		// 요청 실패
		function(){
			error_modal_show("회원가입 실패", "서버에 연결 할 수 없습니다.");
		},
		// 요청 대기
		function(){			
			// 회원가입 버튼 비활성화
			$("button#register_button").attr("disabled", true);

			// 회원가입 버튼 로딩
			$("button#register_button").html(`<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>`);
		},
		// 종료
		function(){
			// 회원가입 버튼 활성화
			$("button#register_button").attr("disabled", false);

			// 회원가입 버튼 로딩
			$("button#register_button").html(`회원가입`);
		});
    });
	
	// 모달 닫기 버튼 클릭
	$("#modal_close").click(function(){
		if(error_element == "register_success") window.location.href = "/login";
		else error_element.focus();
	})
});

function input_check(){
	// 변수 선언
	let result = true;
	
	// 요소 배열
	let element_array = [$("input#register_id"), $("input#register_pw"), $("input#register_pw_check"), $("input#register_email")];
	let element_message_array = ["아이디를 입력해주세요.", "비밀번호를 입력해주세요.", "비밀번호를 재입력 해주세요.", "이메일을 입력해주세요."]
	
	// 요소 빈칸 체크
	for(let element in element_array){
		if(element_array[element].val() == ""){
			error_modal_show("회원가입 실패", element_message_array[element]);
			error_element = element_array[element];
			
			return false;
		}
	}
	
	// 비밀번호 일치 확인
	if(element_array[1].val() != element_array[2].val()){
		error_modal_show("회원가입 실패", "비밀번호가 일치하지 않습니다.");
		error_element = element_array[2];

		result = false;
	}
	
	// 아이디 8자리 미만
	else if(element_array[0].val().length < 8){
		error_modal_show("회원가입 실패", "아이디가 8자리 미만 입니다.");
		error_element = element_array[0];

		result = false;
	}
	
	// 비밀번호 8자리 미만
	else if(element_array[1].val().length < 8){
		error_modal_show("회원가입 실패", "비밀번호가 8자리 미만 입니다.");
		error_element = element_array[1];

		result = false;
	}
	
	return result;
}

// ajax 전송
function sendAjax(url, type, data, success, error, wait, complete, async = true){
    $.ajax({
        url: url,
        type: type,
        data: data,
        async: async,
        success: success,
        error: error,
        beforeSend: wait,
		complete: complete
    });
}
