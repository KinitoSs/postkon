let count_click = 0;
document.querySelector("#Logo-bar").addEventListener('click', function() {
    count_click++;
    if (count_click >= 10){
      RotateLogoOn();
      // NaziOn();
    }
    if (count_click >= 20) {
      RotateLogoOff();
      // NaziOff();
      count_click = 0;
    }
});

function RotateLogoOn() {
  document.querySelector("#Logo-bar").classList.add('rotation');
}
function RotateLogoOff(){
  document.querySelector("#Logo-bar").classList.remove('rotation');
}
function NaziOn(){
   document.getElementById("Logo-bar").src = 'img/111.png';
   document.querySelector("nav").classList.add('nazi');
   document.querySelector("body").style.backgroundColor = "darkred";
   document.querySelector("nav").style.boxShadow = "0px 18px 20px 0px rgba(239, 0, 0, 1)";
   document.querySelector(".profile-card__img img").src = "img/123.jpg";
   document.querySelector("audio").play();

}
function NaziOff(){
   document.getElementById("Logo-bar").src = 'img/L_b.svg';
   document.querySelector("nav").classList.remove('nazi');
   document.querySelector("body").style.backgroundColor = "#EFFFFD";
   document.querySelector("nav").style.boxShadow = "0px 18px 20px 0px rgba(239, 255, 253, 1)";
   document.querySelector(".profile-card__img img").src = "img/info_about_profile/avatar_profile.svg";
   document.querySelector("audio").pause();
}