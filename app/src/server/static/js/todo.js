var cookie = document.cookie;
var suffix = "Cookie:remember_token=".length;
var user_id = cookie.substring(suffix-7, suffix);
document.getElementById("user").innerHTML = "USER:" + user_id;

// 初期表示の時の処理
$(function(){
    // 初期表示で警告表示領域を非表示にする
    clearDivAlert();

    // 期限のカレンダー表示を日本語にする
    $('#inputLimit').datepicker({
        language: 'ja'
    });

});

// 追加ボタンを押した時の処理
$("#btnAdd").on("click", function(){
    clearDivAlert();

    // 入力チェック
    if($('#inputTask').val().trim().length == 0){
        $('#divAlert').css('display', 'block');
        $('#inputAlert').text('タスク内容を入力してください');
        return;
    };

    if($('#inputLimit').val().trim().length == 0){
        $('#divAlert').css('display', 'block');
        $('#inputAlert').text('期限を入力してください');
        return;
    };

    
    // タスクと期限テキストの値を、表に追加する
    $.ajax({
        url: "127.0.0.1/task",
        type: "POST",
        data = {
            user_id: user_id,
            content: $('#inputTask').val().trim(),
            _limit: $('#inputLimit').val().trim()
        }
    }).done(function (data) {
        $('#todoList').append(
            '<tr><td><button type="button" class="btn btn-outline-danger btn-sm mx-0 btnDel" id="btnDel">OK</button></td>' 
            + '<td>' + data['content'] + '</td>' 
            + '<td>' + data['_limit'] + '</td></tr>');
    }).fail(function (data) {
        alert("failed");
    })

    $('#todoList').append(
        '<tr><td><button type="button" class="btn btn-outline-danger btn-sm mx-0 btnDel" id="btnDel">OK</button></td>' 
        + '<td>' + $('#inputTask').val() + '</td>' 
        + '<td>' + $('#inputLimit').val() + '</td></tr>');

    // タスクと期限テキストをブランクにする
    $('#inputTask').val('');
    $('#inputLimit').val('');

});

// tableが動的な要素のため静的な親要素を入れている
$(document).on("click", ".btnDel", function () {
    $(this).closest("tr").remove();
    clearDivAlert();
});

// 警告部の初期化
function clearDivAlert(){
    $('#divAlert').css('display', 'none');
    $('#inputAlert').text('');
}