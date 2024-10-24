// Lesson 16

// Навигация по Dom древу

// parentElement - возвращает родительский элемент
// children - возвращает коллекцию дочерних элементов
// firstElementChild - возвращает первый дочерний элемент
// lastElementChild - возвращает последний дочерний элемент
// nextElementSibling - возвращает следующий соседний элемент
// previousElementSibling - возвращает предыдущий соседний элемент
// closest() - ищет ближайший родительский элемент, соответствующий селектору
// hasChildNodes() - проверяет наличие дочерних узлов
// querySelectorAll() - возвращает все подходящие элементы внутри текущего
// querySelector() - возвращает первый подходящий элемент
// parentNode - возвращает родительский узел (может быть не только элементом)
// childNodes - возвращает коллекцию всех дочерних узлов, включая текстовые
// nextSibling - возвращает следующий соседний узел
// previousSibling - возвращает предыдущий соседний узел


// Практика!  

// Выберите первую строку таблицы (не считая заголовок) и покрасьте её фон в светло-голубой цвет. Селектор: document.querySelector('tbody') Метод: .firstElementChild.style.backgroundColor = 'lightblue'

// Тут мы 

// document.querySelector('tbody').firstElementChild.style.backgroundColor = 'green';
// document.querySelector('tbody').firstElementChild.style.setProperty('background-color', 'lightblue', 'important');

// Тут нали Tbody
let tBody = document.querySelector("tbody");
console.log(tBody);

// Нашли первую полосу в Tbody 
let tBodyFirstElementChild = tBody.firstElementChild;
console.log(tBodyFirstElementChild);

// Покрасили фон в зеленый цвет (Не будет работать из за BS5)
tBodyFirstElementChild.style.backgroundColor = "green";

tBodyFirstRowChildren = tBodyFirstElementChild.children;
console.log(tBodyFirstRowChildren);

// Превратим это в массив и поштучно покрасим
// Array.from(tBodyFirstRowChildren).forEach((element) => {
//   element.style.backgroundColor = "lightblue";
// });

// Вариант в одну строку
Array.from(tBodyFirstElementChild.children).forEach((element) => {
  element.style.backgroundColor = "lightblue";
});


// 2. Найдите последнюю строку таблицы и сделайте текст в ней жирным. Селектор: document.querySelector('tbody') Метод: .lastElementChild.style.fontWeight = 'bold'

tableLastRow = document.querySelector("tbody").lastElementChild;

console.log("Последняя строка таблицы:", tableLastRow);
Array.from(tableLastRow.children).forEach((element) => {
  element.style.fontWeight = "bold";
});

// Выберите строку с id="3-row" и покрасьте текст во всех её ячейках в красный цвет. Селектор: document.getElementById('3-row') Метод: .children.forEach(cell => cell.style.color = 'red')

let trheeRow = document.querySelector("#row-3");
console.log("Третья строка:", trheeRow);
Array.from(trheeRow.children).forEach((element) => {
  element.style.backgroundColor = "red";
});

// Найдите ячейку с текстом "closest()" и покрасьте фон её родительской строки в желтый цвет. Селектор: document.querySelector('td:contains("closest()")') Метод: .parentElement.style.backgroundColor = 'yellow'

// Array.from(document.querySelectorAll('td')).find(td => td.textContent.includes('closest()')).parentElement.style.backgroundColor = 'yellow';

let allTD = document.querySelectorAll("td");
console.log("Все ячейки:", allTD);

let AllTdArray = Array.from(allTD);
console.log("Все ячейки в массиве:", AllTdArray);

let clostestTd = AllTdArray.find((td) => td.textContent.includes("closest()"));

console.log("Ячейка с текстом closest():", clostestTd);

parentClosestTd = clostestTd.parentElement;

Array.from(parentClosestTd.children).forEach((element) => {
  element.style.backgroundColor = "yellow";
});


// Выберите все чётные строки таблицы и установите для них светло-серый фон. Селектор: document.querySelectorAll('tbody tr:nth-child(even)') Метод: .forEach(row => row.style.backgroundColor = 'lightgray')

// Найдите первую ячейку в строке "nextElementSibling" и покрасьте следующую за ней ячейку в зелёный цвет. Селектор: document.querySelector('td:contains("nextElementSibling")') Метод: .nextElementSibling.style.backgroundColor = 'green'

// Выберите последнюю ячейку в предпоследней строке и покрасьте предыдущую ячейку в оранжевый цвет. Селектор: document.querySelectorAll('tbody tr') Метод: [length-2].lastElementChild.previousElementSibling.style.backgroundColor = 'orange'

// ** Найдите строку, содержащую "hasChildNodes()", и если у неё есть дочерние элементы, покрасьте их все в фиолетовый цвет. Селектор: document.querySelector('tr:contains("hasChildNodes()")') Метод: if (el.hasChildNodes()) Array.from(el.children).forEach(child => child.style.color = 'purple')


// ** Выберите первую ячейку первой строки и, двигаясь вниз по диагонали, покрасьте каждую следующую ячейку в синий цвет. Начальный селектор: document.querySelector('tbody tr:first-child td:first-child') Метод: Цикл с .nextElementSibling и .parentElement.nextElementSibling

// 9. Диагональ - синий фон
// По сложному селектору добыем первую ячейку таблицы и перебираем её соседей, пока не дойдём до конца диагонали.
let cell = document.querySelector('tbody tr:first-child td:first-child');
while (cell) {
    cell.style.backgroundColor = 'blue';
    cell = cell.parentElement.nextElementSibling?.firstElementChild.nextElementSibling;
}

// ПРИМЕРЫ И ПОЯСНЕНИЯ ПО ПОВОДУ ТЕРНАРНОГО (ОДНОСТРОЧНОГО) IF КОТОРЫЙ В JS ПИШЕТСЯ ЧЕРЕЗ ?

// // Начальный датасет
// const users = [
//     { name: 'Анна', age: 25, isAdmin: false },
//     { name: 'Борис', age: 30, isAdmin: true },
//     { name: 'Вера', age: 22, isAdmin: false },
//     { name: 'Григорий', age: 35, isAdmin: true }
//   ];
  
//   // Пример 1: Простой тернарный оператор
//   const firstUser = users[0];
//   const status = firstUser.isAdmin ? 'Администратор' : 'Пользователь';
//   console.log(`${firstUser.name} - ${status}`);
  
//   // Пример 2: Тернарный оператор с методом массива
//   const adminCount = users.filter(user => user.isAdmin).length;
//   const adminMessage = adminCount > 1 ? 'Есть несколько админов' : 'Админов мало';
//   console.log(adminMessage);
  
//   // Пример 3: Вложенные тернарные операторы
//   const ageCategory = firstUser.age < 18 ? 'Подросток' : (firstUser.age < 30 ? 'Молодой' : 'Взрослый');
//   console.log(`${firstUser.name} - ${ageCategory}`);
  
//   // Пример 4: Тернарный оператор с цепочкой методов строки
//   const greeting = firstUser.isAdmin 
//     ? `Приветствуем, админ ${firstUser.name}!`.toUpperCase() 
//     : `Здравствуй, ${firstUser.name}`.toLowerCase();
//   console.log(greeting);
  
//   // Пример 5: Тернарный оператор с методами массива и строки
//   const userList = users.length > 0 
//     ? users.map(user => user.name).join(', ') 
//     : 'Список пользователей пуст';
//   console.log(userList);
  
//   // Пример 6: Комбинация тернарного оператора и опциональной последовательности
//   const adminName = users.find(user => user.isAdmin)?.name ?? 'Админ не найден';
//   console.log(`Имя администратора: ${adminName}`);
  
//   // Пример 7: Сложный пример с цепочкой методов и тернарным оператором
//   const result = users
//     .filter(user => user.age > 25)
//     .map(user => user.name)
//     .sort()
//     .join(' и ');
  
//   const finalMessage = result.length > 0 
//     ? `Пользователи старше 25 лет: ${result}` 
//     : 'Нет пользователей старше 25 лет';
//   console.log(finalMessage);


// Найдите ячейку с текстом "querySelectorAll()" и, используя метод closest(), покрасьте границу всей таблицы в красный цвет. Селектор: document.querySelector('td:contains("querySelectorAll()")') Метод: .closest('table').style.border = '2px solid red'