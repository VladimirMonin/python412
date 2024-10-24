// let message = "Открою свой луномодуль!";
// console.log(`Послание: ${message}`);

// // Функция для приведения к булевому типу
// // Boolean(value)

let zero = 0; // false
let one = 1; // true
let strZero = "0"; // true
let emptyStr = ""; // false
let strMessage = "Привет!"; // true
let emptyArr = []; // true
let arr = [1, 2, 3]; // true
let emptyObj = {}; // true
let obj = {
  // true
  name: "John",
  age: 25,
};

// Перепроверим пустую строку на bool
console.log(Boolean(emptyStr)); // false

// let nullWar = null;
// let undefinedWar = undefined;

// console.log(Boolean(zero)); // 0 = false
// console.log(Boolean(one)); // 1 = true
// console.log(Boolean(-1)); // -1 = true
// console.log(Boolean(strZero)); // "0" = true
// console.log(Boolean(emptyStr)); // '' = false
// console.log(Boolean(strMessage)); // "Привет!" = true
// console.log(Boolean(emptyArr)); // [] = true
// console.log(Boolean(arr)); // [1, 2, 3] = true
// console.log(Boolean(emptyObj)); // {} = true
// console.log(Boolean(obj)); // { name: "John", age: 25 } = true
// console.log(Boolean(nullWar)); // null = false
// console.log(Boolean(undefinedWar)); // undefined = false

// let message2 = prompt("Введите сообщение"); // Пустая строка или не пустая

// // Консоль может выводить не только логи, но и ошибки и предупреждения
// // console.error("Ошибка");
// // console.warn("Предупреждение");

// if (message2) {
//   console.log("Сообщение есть");
// } else {
//   console.log("Сообщение пустое");
// }

// //////////// Разница между if и else if ////////////
// // И серия IF и серия ELSE IF начинается с ключевого слова IF

// let integer = 10;

// if (integer < 1) {
//   console.log("Число меньше 1");
// }

// if (integer > 2) {
//   console.log("Число больше 2");
// }

// if (integer > 3) {
//   console.log("Число больше 3");
// }

// if (integer > 1 && integer > 2 && integer > 3) {
//   console.log("Число всех трех цифр");

//   if (integer < 20) {
//     console.log("Число меньше 20");
//   }
//   else {
//     console.log("Число больше 20");
//   }
// } else {
//   console.log("Число не всех трех цифр");
// }

// //// const - константа. Не можем изменять значение?

// const integer2 = 10;
// // integer2 = 20;

// const msg = 'hello';
// // msg = "bye";

// console.log(integer2);
// console.log(msg);

// const personObj = {
//     name: "John",
//     age: 25,
//     isMarried: false,
// }

// personObj.name = "Bob";

// console.log(personObj);

// // сделаем константу с div#result
// const divResult = document.querySelector("#result");
// divResult.innerHTML = "<h1>Hello</h1>";

// // Тернарный if - это сокращенная запись if else

let isMarried = false;

// Полная версия
if (isMarried) {
  console.log("Женат");
}
else {
  console.log("Не женат");
}

// // Сокращенная версия if остуствует
// // Выражение ? true : false
// isMarried ? console.log("Женат") : console.log("Не женат");

// // Попробуем на логическом выражении

// 2 + 2 == 4 ? console.log("ДА, 2+2=4") : console.log("НЕТ, 2+2!=4");
///////////////////////////////////////////////////////////////////////////////////

// Методы строк!

// Методы строк (от популярных к менее популярным)
// toLowerCase() - переводит в нижний регистр
// toUpperCase() - переводит в верхний регистр
// split() - разбивает строку на массив по разделителю
// join() - объединяет массив в строку
// includes() - проверяет, содержит ли строка подстроку
// replace() - заменяет одну подстроку на другую
// replaceAll() - заменяет все вхождения подстроки на другую
// slice() - вырезает подстроку из строки
// length - длина строки
// indexOf() - возвращает индекс первого вхождения подстроки в строку
// charAt() - возвращает символ по индексу
// trim() - удаляет пробелы в начале и конце строки
// substring() - возвращает подстроку из строки
// startsWith() - проверяет, начинается ли строка с подстроки
// endsWith() - проверяет, заканчивается ли строка подстрокой
// repeat() - повторяет строку заданное количество раз
// concat() - объединяет две строки
// search() - ищет подстроку в строке

// Примеры

let string = "Колбаса хЛеб, арбузб, банан";
let subString = "ХлеБ";
string.toLowerCase(); // Как вызывают методы?
console.log(string);
console.log(string.toLowerCase());
console.log(string.toUpperCase());
console.log(string.split()); // Разделитель по умолчанию - пробел
arr_string = string.split();
console.log(arr_string.join(" "));
console.log(string.includes(subString));
console.log(string.toLowerCase().includes(subString.toLowerCase()));
console.log(string.replaceAll("а", "о"));
console.log(string.length);
console.log(string.search(subString)); // -1 - не найдено
console.log(string.toLowerCase().search(subString.toLowerCase())); // 8 - найдено

// Строка - неизменямая упорядоченная итерируемая коллекция символов

let milkProducts = "молоко кефир сметана ряженка масло";
let meatProducts = "говядина свинина баранина курица колбаса сосиски";
let vegetableProducts = "картофель морковь лук помидоры огурцы";
let fruitProducts = "яблоко груша апельсин мандарин";

// trim = удаляет пробелы в начале и конце строки
let userInput = prompt("Введите продукт").trim();
let analisResult = undefined;
const divResult = document.querySelector("#result");

// Проверка на пустой ввод
if (userInput === "" || userInput === " ") {
  console.log("Вы ничего не ввели");

  // Блоки проверки на вхождения в категори продуктов
} else if (milkProducts.includes(userInput.toLowerCase())) {
  console.log(`${userInput} есть в списке молочных продуктов`);
  analisResult = "Молочные продукты";
} else if (meatProducts.includes(userInput.toLowerCase())) {
  console.log(`${userInput} есть в списке мясных продуктов`);
  analisResult = "Мясные продукты";
} else if (vegetableProducts.includes(userInput.toLowerCase())) {
  console.log(`${userInput} есть в списке овощей`);
  analisResult = "Овощи";
} else if (fruitProducts.includes(userInput.toLowerCase())) {
  console.log(`${userInput} есть в списке фруктов`);
  analisResult = "Фрукты";
}

// Если продукт не найден
else {
  console.log(`${userInput} не найден в нашей базе`);
}

// Вывод результата
analisResult
  ? (divResult.innerHTML = `<h1>${analisResult}</h1>`)
  : (divResult.innerHTML = `<h1>Продукт не найден</h1>`);
