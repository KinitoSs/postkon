// Переменная для тестов
let personData = [{"name":"Иван", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Павел", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}, {"name":"Антон", "img_src": "img/work_space/avatar_mini.svg"}];

let btn = document.querySelector('.btn-search');
btn.addEventListener('click', async function(event){
    event.preventDefault();
    // let response = await fetch("/URL", {
    //     method: "POST",
    //     body: new FormData(document.querySelector('.form-search'))
    // })
    // let response_json = await response.json();
    if (personData){
        // Вывести пользователей из файла JSON
        let searchElems = document.querySelectorAll('.get-user');
        searchElems.forEach(element => {
            element.remove();
        });
        // document.querySelectorAll('.get-user')
        for (var i = 0; i < personData.length; i++) {
            let elem = document.createElement("li");
            elem.innerHTML = `
                    <div class="info-user">
                        <div class="change-avatar">
                            <img src="${personData[i].img_src}" alt="альтернативный текст" />
                        </div>
                        <div class="name-user">
                            <p>${personData[i].name}</p>
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