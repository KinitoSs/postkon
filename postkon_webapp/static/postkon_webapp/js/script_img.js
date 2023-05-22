const url_img = ["https://imgur.com/9KQDrXw.jpg", "https://imgur.com/0pypwu2.jpg", "https://imgur.com/AOY0sky.jpg"];
let i = 0;
const imgAvatar = document.querySelector(".img-avatar");
let url_value = url_img[i];

document.querySelector("#back").addEventListener('click', function() {
    i = (i - 1 + url_img.length) % url_img.length;
    imgAvatar.src = url_img[i];
    url_value = url_img[i];
});

document.querySelector("#next").addEventListener('click', function() {
    i = (i + 1) % url_img.length;
    imgAvatar.src = url_img[i];
    url_value = url_img[i];
});