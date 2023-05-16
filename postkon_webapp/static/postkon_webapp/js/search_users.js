// Переменная для тестов
// let personData = [{"name":"Иван", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Павел", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}];

let btn = document.querySelector('.btn-search');
btn.addEventListener('click', async function(event){
    event.preventDefault();
    let response = await fetch(searchUrl, {
        method: "POST",
        body: new FormData(document.querySelector('.form-search'))
    })
    let response_json = await response.json();
    if (response_json){
        // Вывести пользователей из файла JSON
        let searchElems = document.querySelectorAll('.get-user');
        searchElems.forEach(element => {
            element.remove();
        });
        let avatar_img;
        // document.querySelectorAll('.get-user')
        for (var i = 0; i < response_json.length; i++) {
            let elem = document.createElement("li");
            if (response_json[i].avatar_img != null){
                avatar_img = response_json[i].avatar_img;
            }
            else {
                avatar_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/F1_light_blue_flag.svg/2560px-F1_light_blue_flag.svg.png";
            }
            elem.innerHTML = `
                    <div class="info-user">
                        <div class="change-avatar">
                            <img class="avatar_search" src="${avatar_img}" alt="альтернативный текст" style="width: 50px;
                            height: 50px;
                            border-radius: 50px;"/>
                        </div>
                        <div class="name-user">
                            <p><a href="${response_json[i].url}">${response_json[i].username}</a></p>
                        </div>
                    </div>`;
            elem.classList.add("get-user");
            document.querySelector('#add-user').appendChild(elem);
          }
    } else {
        // Вывести сообщение, что такого пользователя нет
        console.log("Пользователь не найден!");
    }

})