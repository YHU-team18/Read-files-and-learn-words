//'use strict';//厳格モード
var error_text = "pdfを添付してください";
var fd = new FormData();

// drag and drop event
$(document).ready(function() {
    var obj = $("#dragandrophandler");
    obj.on('dragenter', function (e) {
        e.stopPropagation();//イベントの伝搬停止
        e.preventDefault();//デフォルトイベントの停止
        $(this).css('border', '2px solid #0B85A1');
    });
    obj.on('dragover', function (e) {
        e.stopPropagation();
        e.preventDefault();
    });
    obj.on('drop', function(e) {
        $(this).css('border', '2px dotted #0B85A1');
        e.preventDefault();

        var files = e.originalEvent.dataTransfer.files;

        // file error check
        err_chk(files, obj);
    });

    // Avoid opening in a browser if the file is dropped outside the div
    $(document).on('dragenter', function (e) {
        e.stopPropagation();
        e.preventDefault();
    });

    $(document).on('dragover', function (e) {
        e.stopPropagation();
        e.preventDefault();
        obj.css('border', '2px dotted #0B85A1');
    });

    $(document).on('drop', function (e) {
        e.stopPropagation();
        e.preventDefault();
    });
});

// file error check
function err_chk(files, obj) {
  for (  var i = 0;  i < files.length;  i++  ) {
    var filetype = files[i].type;
    var filename = files[i].name;

    // Validation

    // 1. File format
    if (!(filetype.match('(.pdf)$'))){
        document.getElementById('error_list').innerText = "ファイル形式が、pdf以外のものは使用できません。";
        document.getElementById('preview').innerText = "";
        error_text = "ファイル形式が、pdf以外のものは使用できません。";
        return false;
    }

    // 2. File size
    var sizeKB = files[0].size / 1024;
    if (parseInt(sizeKB) > 1024) {
      var sizeMB = sizeKB / 1024;
      // 修士論文の枚数制限→40~120枚程度なので120で計算
      // A4,解像度300,白黒→300kb なので(120*300)/1024+αの40mbでブレイクポイント設定
      if (sizeMB > 40) {
          document.getElementById('error_list').innerText = "pdfサイズが大きすぎます。40MBより小さいサイズのpdfをお願いします.";
          document.getElementById('preview').innerText = "";
          error_text = "pdfサイズが大きすぎます。40MBより小さいサイズのpdfをお願いします.";
          return false;
      };
    };

    document.getElementById('preview').innerText += filename;
    document.getElementById('error_list').innerText = "";
    error_text = "true";
    fd.set('file', files[0]);
   }
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

//error_text check
function check() {
  if (error_text != "true") {
    return false;
  }
  fd.append("csrfmiddlewaretoken", getCookie("csrftoken"));

  const xhr = new XMLHttpRequest();
  xhr.open("post", "/submit_pdf/", false);
  xhr.onload = function () {
    // 送信成功時の動作をここに記述する
    console.log(fd)
  };
  xhr.onreadystatechange = function(){
    if (this.readyState == 0) {
      console.log("UNSENT:初期状態");
    }
    if (this.readyState == 1) {
      console.log("OPENED:openメソッド実行");
    }
    if (this.readyState == 2) {
      console.log("HEADERS_RECEIVED:レスポンスヘッダー受信");
    }
    if (this.readyState == 3) {
      console.log("LOADING:データ受信中");
    }
    if (this.readyState == 4) {
      console.log("DONE:リクエスト完了");
    }
  }
  console.log(fd.getAll);
  xhr.send(fd);
}
