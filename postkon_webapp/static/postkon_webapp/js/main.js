let count_click = 0;
document.querySelector("#Logo-bar").addEventListener('click', function() {
    count_click++;
    if (count_click >= 10){
      RotateLogoOn();
    }
    if (count_click >= 20) {
      RotateLogoOff();
      count_click = 0;
    }
});

function RotateLogoOn() {
  document.querySelector("#Logo-bar").classList.add('rotation');
}
function RotateLogoOff(){
  document.querySelector("#Logo-bar").classList.remove('rotation');
}