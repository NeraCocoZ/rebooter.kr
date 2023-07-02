$(document).ready(function(){
    // 검색 버튼 클릭
    $("button#usersearch_button").click(function(){
        // 검색 입력창 확인
        let input = $("input#usersearch").val();

        if(input == "")
              return;

        // 검색 결과 페이지 이동
        window.location.href = `/usersearch?username=${input}`;
    })
});