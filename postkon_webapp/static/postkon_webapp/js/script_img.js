let url_img = ["https://imgur.com/9KQDrXw.jpg", "https://imgur.com/0pypwu2.jpg", "https://imgur.com/AOY0sky.jpg"];
let url_value = "img/info_about_profile/avatar_profile.svg";
let i = 0;
document.querySelector("#back").addEventListener('click', function() {
    i = i - 1;
    document.querySelector(".img-avatar").setAttribute('src', url_img[Math.abs(i)%url_img.length]);
    url_value = url_img[Math.abs(i)%url_img.length]
});

document.querySelector("#next").addEventListener('click', function() {
    i = i + 1;
    document.querySelector(".img-avatar").setAttribute('src', url_img[Math.abs(i)%url_img.length]);
    url_value = url_img[Math.abs(i)%url_img.length]
});