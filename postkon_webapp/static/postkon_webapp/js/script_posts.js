var calculateHeight = function() {
  var ta = document.getElementById("ta"),
      style = (window.getComputedStyle) ?
          window.getComputedStyle(ta) : ta.currentStyle,
      taLineHeight = parseInt(style.lineHeight, 10),
      taHeight = calculateContentHeight(ta, taLineHeight),
      numberOfLines = Math.ceil(taHeight / taLineHeight);
      // alert(numberOfLines);
  return numberOfLines;
};

var calculateContentHeight = function( ta, scanAmount ) {
  var origHeight = ta.style.height,
      height = ta.offsetHeight,
      scrollHeight = ta.scrollHeight,
      overflow = ta.style.overflow;
  if ( height >= scrollHeight ) {
      ta.style.height = (height + scanAmount) + 'px';
      ta.style.overflow = 'hidden';
      if ( scrollHeight < ta.scrollHeight ) {
          while (ta.offsetHeight >= ta.scrollHeight) {
              ta.style.height = (height -= scanAmount)+'px';
          }
          while (ta.offsetHeight < ta.scrollHeight) {
              ta.style.height = (height++)+'px';
          }
          ta.style.height = origHeight;
          ta.style.overflow = overflow;
          return height;
      }
  } else {
      return scrollHeight;
  }
}

calculateHeight();
if (ta.addEventListener) {
  ta.addEventListener("mouseup", calculateHeight, false);
  ta.addEventListener("keyup", calculateHeight, false);
} else if (ta.attachEvent) { // IE
  ta.attachEvent("onmouseup", calculateHeight);
  ta.attachEvent("onkeyup", calculateHeight);
};

$('.delete-post-btn').click(function() {
  var post_id = $(this).data('post-id');
  $.ajax({
    url: '/delete_post/',
    type: 'POST',
    data: {'post_id': post_id},
    success: function(response) {
      if (response.success) {
        // Перезагрузить страницу для обновления списка постов
        location.reload();
      } else {
        alert('Не удалось удалить пост.');
      }
    },
    error: function() {
      alert('Не удалось удалить пост.');
    }
  });
});


$(function () {
  $("#post-form").submit(function (e) {
    e.preventDefault();
    var textarea = this.getElementsByTagName("textarea")[0],
      taHeight = textarea.offsetHeight,
      taWidth = textarea.offsetWidth,
      taTop = textarea.offsetTop,
      taLeft = textarea.offsetLeft,
      taText = textarea.value;
      postTop = document.getElementsByClassName("post")[0].offsetTop;
    var $hoverDiv = $("<div>").addClass("hover").text(taText).css({
      height: taHeight,
      width: taWidth,
      top: taTop,
      left: taLeft
    });

    
    // Начало запроса
    let btn = document.querySelector('.btn');
    btn.addEventListener('click', async function(event){
      event.preventDefault();
      let response = await fetch(addPostUrl, {
          method: "POST",
          body: taText
      })
      let response_json = await response.json();
      if (response_json){

        let d = new Date().getDate();
        if (d < 10) {
          d = String(d);
          d = '0' + d;
        }
        let mm = new Date().getMonth() + 1;
        if (mm < 10) {
          mm = String(mm);
          mm = '0' + mm;
        }
        let hour = new Date().getHours();
        if (hour < 10) {
          hour = String(hour);
          hour = '0' + hour;
        }
        let min = new Date().getMinutes();
        if (min < 10) {
          min = String(min);
          min = '0' + min;
        }
        var $postTimestamp = $("<p>")
          .addClass("post-timestamp")
          .text('Создано ' + response_json.date_uploaded) // ввввввввввввввввввввввввввввввввввввввв
          .css("visibility", "hidden");
        var $postt = $("<div>")
          .addClass("post-t")
          .append($postTimestamp);
    
        var $namepost = $("<p>")
          .addClass("name-post")
          .text(response_json.creator_username); // Имя создателя ввввввввввввввввввввввввввввввв
    
        var $namep = $("<div>")
          .addClass("name-p")
          .append($namepost);
    
        var $nameandtime = $("<div>")
          .addClass("name-and-time")
          .append($namep)
          .append($postt);
    
        var $avatarimagemini = $('<img>')
          .attr("src", response_json.creator_avatar_img); // ввввввввввввввввввввввввввввввввввввв
    
        var $avatarmini = $("<div>")
          .addClass("avatar-mini")
          .append($avatarimagemini);
    
        var $postinfo = $("<div>")
          .addClass("post-info")
          .append($avatarmini)
          .append($nameandtime);
    
        var $postContent = $("<p>")
          .addClass("post-content")
          .text(taText);
        var $readmore = $("<div>")
        .addClass("read-more")
        .attr('style', "overflow: hidden;")
        .append($postContent);
        var $readnext = $("<div>")
          .addClass('read-next')
          .addClass('read-next-style')
          .attr('onclick', "ShowMore(event);")
          .text("Читать далее...");
        var $post = $("<li>")
          .addClass("post")
          .append($postinfo)
          .append($readmore)
          .hide();
        let ch = calculateHeight();
        if (ch >= 5){
          $post.append($readnext);
        };
        //textarea.value = "";
        $post.prependTo("#feed");
        $hoverDiv
          .delay(300)
          .animate({ top: postTop }, 1000, "swing")
          .queue(function () {
            $hoverDiv.delay(200).stop().fadeOut();
            $postTimestamp.hide().css("visibility", "visible").fadeIn();
          });
        $post.delay(300).slideDown(1000);
        console.log("123")
      } else {
          console.log("Пост не создан!");
      }

    })
  });
});



function ShowMore(elem) {
  var postX = elem.currentTarget;
  if (postX.classList.contains('read-next')) {
    postX.innerHTML = "Скрыть";
    postX.parentNode.querySelector('.read-more').style = "overflow: visible; height: auto;"
    postX.classList.remove('read-next');
    postX.classList.add('read-next-none');
  }
  else {
    postX.innerHTML = "Показать полностью...";
    postX.parentNode.querySelector('.read-more').style = "overflow: hidden; height: 100px;"
    postX.classList.add('read-next');
    postX.classList.remove('read-next-none');
  }
}


// var invocation = new XMLHttpRequest();
// var url = 'https://evilinsult.com/generate_insult.php?lang=en&type=xml';
