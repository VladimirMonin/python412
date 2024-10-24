// Lesson 19-1
// Хранилища в JS
// 1. Cookies - 4кб потолок. Данные о пользователях, корзина и т.п. отправляется с каждым запросом.
// Жизненый цикл настраивается.
// Авториация. Систма пользователей. Предпочтения. Системы отслеживания пользователей. Google Analytics. Яндекс Метрика. Пиксель ВК. Пиксель FB.
// 2. SessionStorage -5мб. Сессия.? Открытая вкладка браузера. Большое хранилище.
// 3. LocalStorage - 5мб.

// Куки. Где они живут? document.cookie
// Хранятся они в виде 1 строки

// Запишем простую куку ключ ourCookie="Hello!"
document.cookie = "ourCookie=Hello!";

// Получим все куки в виде строки
console.log(document.cookie); // ourCookie=Hello!

// Получим объект с кукми
// 1. Положим куки в переменную
let cookies = document.cookie;

// 2. Разбить на массив
cookies = cookies.split(";");

// 3. Перевести в объект
let cookiesObj = {};
cookies.forEach(function (item) {
    let cookieArr = item.trim().split("=");
     cookiesObj[cookieArr[0]] = cookieArr[1];
});

console.log(cookiesObj); // {ourCookie: "Hello!"}

cookiesObj.newCookie = "New-Cookie";
console.log(cookiesObj); // {ourCookie: "Hello!", newCookie: "New Cookie"}
// 4. Создадим строку куки из объекта
let newCookiesStr = "";

// Когда мы используем оператор присваивания = с document.cookie, мы действительно не переопределяем все куки, а добавляем новую или обновляем существующую куку.

// Это особенность работы с куками в JavaScript. Каждый раз, когда мы пишем document.cookie = "key=value", мы фактически добавляем или обновляем одну конкретную куку. Если куки с таким ключом уже существует, она будет обновлена. Если нет - будет создана новая.

// Таким образом, document.cookie работает как своего рода "аккумулятор" кук, где каждое присваивание добавляет или изменяет одну куку, не затрагивая остальные. Это позволяет управлять куками по отдельности, не влияя на весь набор кук сразу.

for ([key, value] of Object.entries(cookiesObj)) {
    document.cookie = `${key}=${value};`;
}
console.log(newCookiesStr); // ourCookie=Hello!;newCookie=New Cookie
document.cookie = newCookiesStr;
console.log(document.cookie); // ourCookie=Hello!;newCokie=New Cookie;



// LocalStorage. Запись в хранилище браузера.

const input = document.querySelector("#input");
const formButton = document.querySelector("#formButton");
const localP = document.querySelector("#localP");
const deleteButton = document.querySelector("#deleteButton");

// Листнер по клику на кнопку формы, записывает данные в хранилище браузера
formButton.addEventListener("click", function (event) {
    // Препятствуем отправке формы
    event.preventDefault();
    const inputValue = input.value;
    localP.textContent = inputValue;

});

formButton.addEventListener('click', function () {
    const inputValue = input.value;
    localStorage.setItem('inputValue', inputValue);
    // localStorage.setItem('inputValue', input.value);
    // localP.textContent = localStorage.getItem('inputValue');
});

// Листнер по загрузке документа, проверяет есть ли в хранилище данные inputValue
// если есть, поместит в параграф localP

document.addEventListener("DOMContentLoaded", function () {
    const inputValue = localStorage.getItem("inputValue");
    if (inputValue) {
        localP.textContent = inputValue;
    }
});

// Листнер для deleteButton удаляет данные из хранилища браузера
deleteButton.addEventListener("click", function () {
    localStorage.removeItem("inputValue");
    localP.textContent = "Данные не обнаружены";
});