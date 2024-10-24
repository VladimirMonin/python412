// Lesson 17: Изменение элементов DOM

// textContent - это свойство, которое позволяет получить или установить текстовое содержимое элемента
// innerHTML - свойство, которое позволяет получить или установить HTML-содержимое элемента
// setAttribute() - метод для установки значения атрибута элемента
// removeAttribute() - метод для удаления атрибута элемента
// getAttribute() - метод для получения значения атрибута элемента
// classList - свойство для работы с классами элемента (add, remove, toggle)
// style - свойство для изменения inline-стилей элемента
// createElement() - метод для создания нового элемента
// appendChild() - метод для добавления дочернего элемента
// removeChild() - метод для удаления дочернего элемента
// replaceChild() - метод для замены дочернего элемента
// insertBefore() - метод для вставки элемента перед указанным
// Метод insertBefore() используется для вставки нового узла перед существующим дочерним узлом родительского элемента. 

// Вот ключевые моменты его использования:
// Синтаксис: parentNode.insertBefore(newNode, referenceNode)
// parentNode - это родительский элемент, в который мы хотим вставить новый узел.
// newNode - это новый узел, который мы хотим вставить.
// referenceNode - это существующий дочерний узел, перед которым мы хотим вставить новый узел.
// Если referenceNode равен null, newNode будет вставлен в конец списка дочерних элементов parentNode.
// Метод возвращает вставленный узел.
// Если referenceNode не является дочерним элементом parentNode, метод выбросит ошибку.
// insertBefore() может использоваться для перемещения существующих элементов, а не только для вставки новых.
// Этот метод работает со всеми типами узлов, включая элементы, текстовые узлы и фрагменты документа.
// Важно помнить, что узел может существовать только в одном месте DOM. Если вы вставляете существующий узел, он будет удален с его текущей позиции и вставлен в новую.
// Использование insertBefore() дает вам точный контроль над тем, куда вы вставляете новые элементы в DOM, что делает его мощным инструментом для динамического изменения структуры страницы.



// cloneNode() - метод для клонирования элемента
// outerHTML - свойство, которое возвращает HTML-разметку элемента, включая сам элемент
// insertAdjacentHTML() - метод для вставки HTML-разметки в указанную позицию относительно элемента
// dataset - свойство для работы с пользовательскими data-* атрибутами
// closest() - метод для поиска ближайшего родительского элемента, соответствующего селектору
// matches() - метод для проверки, соответствует ли элемент заданному селектору
// scrollIntoView() - метод для прокрутки страницы к элементу

// Найдем тег боди
const body = document.querySelector('body');

// innerHTML 
body.innerHTML += '<h1>Создание элементов через JS</h1>';
// Внедрим JS через innerHTML текст по клику на котороый будет alert
// body.innerHTML += '<p onclick="alert(\'Кликните на этот текст!\')">Кликните на этот текст!</p>';

//  Это не очень безопасно. Потому что челвоек может внедрить вредоносный код через формы ввода данных.
// Более безопасный вариант - использовать createElement() textContent и appendChild()

const p = document.createElement('p');
p.textContent = 'Параграф создан при поддержке JS!';
console.log(p);

body.appendChild(p);

// Добываем первый попавшийся заголовок H2
const h2 = document.querySelector('h2');

// Извлекаем значение атрибута data и выводим его в консоль
h2Data = h2.getAttribute('data');
console.log(h2Data);

// Переназначим атрибут data
h2.setAttribute('data', 'hello hello');

// classList - свойство для работы с классами элемента (add, remove, toggle)
h2.classList.remove('text-bg-danger');
h2.classList.add('text-bg-success');

// toggle() - метод для переключения классов
h2.classList.toggle('text-bg-warning');

function toggleColor() {
    button = document.querySelector('button');
    button.classList.toggle('btn-dark')
}

function toggleTheme() {
    themeButton = document.querySelector('#btnTheme');
    htmlTag = document.querySelector('html');

    // Нам нужно проверить атрибут data-bs-theme
    // Он может быть равен light или dark
    // Наша задача переключить тему при клике на кнопку

    // Если тема равна light, тогда мы должны установить dark
    if (htmlTag.getAttribute('data-bs-theme') === 'light') {
        // Устанавливаем dark
        htmlTag.setAttribute('data-bs-theme', 'dark');
        themeButton.textContent = 'Темная тема';
    } else {
        // Если тема равна dark, тогда мы должны установить light
        htmlTag.setAttribute('data-bs-theme', 'light');
        themeButton.textContent = 'Светлая тема';
    }

}

// appendChild() - метод для добавления дочернего элемента
// removeChild() - метод для удаления дочернего элемента
// replaceChild() - метод для замены дочернего элемента
// insertBefore() - метод для вставки элемента перед указанным
// cloneNode() - метод для клонирования элемента

let productList = ['Коньки', 'Удочка', 'Коньяк', 'Палатка', 'Горелка'];
// let divProdictList = document.querySelector('#productList');
// let ul = document.createElement('ul');
// // let li = document.createElement('li');
// // li.textContent = productList[0];

// // ul.appendChild(li);
// // Повторить так много раз...

// for (let product of productList) {
//     let li = document.createElement('li');
//     li.textContent = product;
//     ul.appendChild(li);
// }

// // Добавить ul в divProdictList
// divProdictList.appendChild(ul);

// Функция принемает массив и id контейнера и отрисовывает список

function renderProductList(productList, containerId) {
    let div = document.querySelector('#' + containerId);
    let ul = document.createElement('ul');

    for (let product of productList) {
        let li = document.createElement('li');
        li.textContent = product;
        ul.appendChild(li);
    }

    div.appendChild(ul);

}

// Вызов функции
renderProductList(productList, 'productList');
